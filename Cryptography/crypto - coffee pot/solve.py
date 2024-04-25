from pwn import *

r = remote('localhost', 7777)
r.recvuntil(b'here\'s your flag: ')
cip_flag = r.recvline().strip().decode()
for i in range(128, 0, -32):
	r.sendline(cip_flag[i-32:i])
	r.recvuntil(b'>> ')
	dec = r.recvline().strip().decode()
	print(xor(bytes.fromhex(dec), bytes.fromhex(cip_flag[i-64:i-32])))
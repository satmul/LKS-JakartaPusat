from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

AES_KEY = os.urandom(16)

def encrypt_giga(message):
	iv = os.urandom(16)
	cipher = AES.new(AES_KEY, AES.MODE_CBC, iv=iv)
	enc = cipher.encrypt(pad(message, 16))
	return (iv + enc).hex()

def decrypt_giga(enc):
	enc = bytes.fromhex(enc)
	cipher = AES.new(AES_KEY, AES.MODE_ECB)
	message = cipher.decrypt(enc)
	return message.hex()

flag = b'LKSJakpus{d1ff3r3nt_m0de_s4me_c0de}'
enc = encrypt_giga(flag)
print("here's your flag:", enc)
for _ in range(4):
	try:
		msg = input(">> ")
		print(decrypt_giga(msg))
	except Exception as e:
		print("Error lur. Jangan diulangi lagi ya")
		pass

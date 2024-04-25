from Crypto.Util.number import *

flag = b"LKSJakpus{RSA_1sn't_4lw4ys_t3xtb00k}"

p = getPrime(512)
q = getPrime(512)
n = p * q
m = bytes_to_long(flag)
e = 65537
c = pow(m, e, n)
big = pow(p, 2) + pow(q, 2)

print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")
print(f"big: {big}")


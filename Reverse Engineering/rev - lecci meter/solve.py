from z3 import *

s = Solver()
key = [Int(i) for i in range(24)]
s.add(key[12] == (key[2] * 2) - 3) 
s.add(key[3] == key[4]) 
s.add(key[0] == key[21] + 1) 
s.add(key[8] == key[12]) 
s.add(key[2] == key[5]) 
s.add(key[1] - 2 == key[6]) 
s.add(key[23] / 2 == key[22]) 
s.add((key[18] * 2) + 2 == key[17]) 
s.add(key[16] == key[0] + 1) 
s.add(key[7] * 2 == key[11] + 107) 
s.add(key[2] == key[13]) 
s.add(key[15] == key[8]) 
s.add(key[8] == key[19]) 
s.add(key[7] + 7 == key[20] - 6) 
s.add(key[9] - 2 == key[14])
s.add(key[14] == 110)
s.add(key[9] + 3 == key[0])
s.add(key[5] == (key[9] / 2) - 7)
s.add(key[8] + 13 == key[4])
s.add(key[11] - 1 == key[13] * 2)
s.add(key[5] + 2 == key[18])
s.add(key[23] == key[11])
s.add(key[1] == key[20] - 4)
s.add(key[10] == key[0] + 6)

print(s.check())
model = s.model()
print(model)
flagga = ''.join([chr(int(str(model[key[i]]))) for i in range(len(model))])
print(flagga)

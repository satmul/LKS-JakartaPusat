import random
from pwn import *

cip = [69, 28, 55, 16, 67, 44, 37, 2, 46, 48, 106, 45, 74, 71, 50, 6, 93, 122, 68, 13, 111, 74, 40, 40, 83, 78, 12, 23, 36, 23, 123, 8, 119, 17, 20, 72, 116, 21, 105, 91, 17, 61, 44]
for x in range(3000):
	random.seed(x)
	randseed_two = random.randint(1, 300000)
	random.seed(randseed_two)
	randseed_three = random.randint(1, 300000)
	random.seed(randseed_three)
	randseed_four = random.randint(1, 300000)
	random.seed(randseed_four)
	randseed_five = random.randint(1, 300000)
	random.seed(randseed_five)
	randseed_six = random.randint(1, 300000)
	random.seed(randseed_six)
	randseed_seven = random.randint(1, 300000)
	random.seed(randseed_seven)
	randseed_eight = random.randint(1, 300000)
	random.seed(randseed_eight)
	randseed_nine = random.randint(1, 300000)
	random.seed(randseed_nine)
	randseed_ten = random.randint(1, 300000)
	random.seed(randseed_ten)
	randseed_eleven = random.randint(1, 300000)
	random.seed(randseed_eleven)
	randseed_twelve = random.randint(1, 300000)
	random.seed(randseed_twelve)
	randseed_thirteen = random.randint(1, 300000)
	random.seed(randseed_thirteen)
	randseed_fourteen = random.randint(1, 300000)
	random.seed(randseed_fourteen)
	randseed_fifteen = random.randint(1, 300000)
	random.seed(randseed_fifteen)
	randseed_sixteen = random.randint(1, 300000)
	random.seed(randseed_sixteen)
	randseed_seventeen = random.randint(1, 300000)
	random.seed(randseed_seventeen)
	randseed_eighteen = random.randint(1, 300000)
	random.seed(randseed_eighteen)
	randseed_nineteen = random.randint(1, 300000)
	random.seed(randseed_nineteen)
	randseed_twenty = random.randint(1, 300000)
	random.seed(randseed_twenty)
	rand_key = [random.randint(1, 123) for _ in range(len(cip))]
	flag = ""
	for i in range(len(cip)):
		flag+=(chr(cip[i] ^ rand_key[i]))

	if "LKS" in flag:
		print(flag, x, randseed_twenty)
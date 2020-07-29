import math

def count_coprimes(limit):
	count = 0
	for i in range (2, limit+1):
		for x in range (2, limit+1):
			if (i < x and math.gcd(i,x) == 1):
				count+=1
	print("Answer = " + str(count))

limit = input("Enter limit: ")
count_coprimes(int(limit))
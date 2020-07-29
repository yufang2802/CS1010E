import math

count = 0

def count_prime(limit):
	count = 0
	for i in range(1, limit+1):
		if (is_prime(i) == True):
			count += 1
	return count
		

def is_prime(integer):
		for i in range(2, math.ceil(math.sqrt(integer))+1):
			if integer%i == 0:
				return False #not prime
		return True #prime, after looping through everything

limit = input("Enter limit ")

print("Number of primes = " + str(count_prime(int(limit))))
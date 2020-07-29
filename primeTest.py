import math

def is_prime(integer):
		for i in range(2, math.ceil(math.sqrt(integer))):
			if integer%i == 0:
				return False #not prime
		else: 
			return True #prime

number = input("Enter positive integer ")
print(is_prime(int(number)))
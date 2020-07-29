integer = input("Enter positive integer ")

def check_order(integer):
	previous = 0
	while (integer > 0 and integer > previous):
		previous = integer
		integer = int(input("Enter positive integer "))
	if integer == 0:
		print("Data are in increasing order.")
	else: 
		print("Data are not in increasing order.")

check_order(int(integer))
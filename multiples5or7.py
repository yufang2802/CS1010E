def count_multiples(integer):
	count = 0
	for i in range(1,integer+1):
		if (i%5 == 0 or i%7 == 0):
			count+=1
	if count > 1:		
		print("There are " + str(count) + " multiples of 5 or 7 in [1, " + str(integer) + "].")
	elif count == 1:
		print("There is " + str(count) + " multiple of 5 or 7 in [1, " + str(integer) + "].")
	else:
		print("There is no multiple of 5 or 7 in [1, " + str(integer) + "].")

integer = input("Enter positive integer: ")
count_multiples(int(integer))
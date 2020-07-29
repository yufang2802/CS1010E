def validate():

	attempts = 0
	integer = -1
	
	while integer <1 or integer>100:
		integer = int(input("Enter number ")) #enter number again
		attempts += 1
	
	print("Your age is " + str(integer) + ".")
	print("Number of attempts = " + str(attempts))

	#don't need to use break because return alr allows you to exit the function while carrying the value you're returning with

validate()
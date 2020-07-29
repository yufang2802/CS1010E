def computeHappyNumbers(lower, upper):
	happy = 0
	total = 0
	newTotal = 0
	for x in range(lower, upper+1):
		digits = [int(digits) for digits in str(x)]
		print(digits) # i stopped here, managed to split the number into its digits
		
		while total != 1:
			for y in range(len(digits)):
				total = int(digits[y])**2
				print(total)
				# newDigits = [int(newDigits) for newDigits in str(total)]
				# digits = newDigits
				# if total == 1:
				# 	happy += 1
				# total = 0
					
		
	# return "None"


# def compute(lower1, upper1, lower2, upper2):



lower1 = int(input("Enter lower number 1: "))
upper1 = int(input("Enter upper number 1: "))
# lower2 = input("Enter lower number 2: ")
# upper2 = input("Enter upper number 2: ")

print(computeHappyNumbers(lower1,upper1))
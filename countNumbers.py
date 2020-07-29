divisor1 = int(input("Enter divisor 1 "))
divisor2 = int(input("Enter divisor 2 "))

def countNumbers(divisor1, divisor2, limit1, limit2):
	count = 0
	for x in range(limit1, limit2+1):
		if x%divisor1 != 0 and x%divisor2 != 0:
			count += 1
	
	print("Answer = " + str(count))
	return count

def checkDivisors(divisor1, divisor2):
	while (divisor1 <= 0 or divisor2 <= 0 or divisor1 == divisor2):
		divisor1 = int(input("Enter divisor 1 "))
		divisor2 = int(input("Enter divisor 2 "))
	
	limit1 = int(input("Enter limit 1 "))
	limit2 = int(input("Enter limit 2 "))

	while limit1 <= 0 or limit2 <= 0 or limit1 == limit2 or limit1 > limit2:
		limit1 = int(input("Enter limit 1 "))
		limit2 = int(input("Enter limit 2 "))
		
	countNumbers(divisor1, divisor2, limit1, limit2)

checkDivisors(divisor1,divisor2)
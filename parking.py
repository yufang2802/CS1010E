import math

def computeFee(day, timeIn, timeOut):
	totalFare = 0

	if (timeOut - timeIn <= 10):
		totalFare = 0
		return totalFare

	elif (1 <= day <= 5): #weekdays
		if timeIn <= 700:
			if timeOut <= 700:
				totalFare = totalFare + math.ceil((timeOut - timeIn)/100)*2
			elif 700 < timeOut <= 1800:
				totalFare = totalFare + math.ceil((700 - timeIn)/100)*2 + math.ceil((timeOut - 700)/30)*1.2
			elif timeOut > 1800:
				totalFare = totalFare + math.ceil((700 - timeIn)/100)*2 + 26.4 + 5

		elif 700 < timeIn <= 1800:
			if 700 < timeOut <= 1800:
				totalFare = totalFare + math.ceil((timeOut - timeIn)/50)*1.2
			elif timeOut > 1800:
				totalFare = totalFare + math.ceil((1800 - timeIn)/50)*1.2 + 5

		elif timeIn > 1800:
			totalFare = totalFare + 5
		
		if timeOut - timeIn > 1000:
			totalFare = totalFare * 1.1

		if timeOut > 2200:
			totalFare = totalFare + 3

		return totalFare

	elif (day == 6): #saturday
		if timeIn <= 700:
			if timeOut <= 700:
				totalFare = totalFare + math.ceil((timeOut - timeIn)/100)*2.5
			elif 700 < timeOut <= 1800:
				totalFare = totalFare + math.ceil((700 - timeIn)/100)*2.5 + math.ceil((timeOut - 700)/30)*1.5
			elif timeOut > 1800:
				totalFare = totalFare + math.ceil((700 - timeIn)/100)*2.5 + 33 + 7

		elif 700 < timeIn <= 1800:
			if 700 < timeOut <= 1800:
				totalFare = totalFare + math.ceil((timeOut - timeIn)/50)*1.5
			elif timeOut > 1800:
				totalFare = totalFare + math.ceil((1800 - timeIn)/50)*1.5 + 7

		elif timeIn > 1800:
			totalFare = totalFare + 7
		
		if timeOut - timeIn > 1000:
			totalFare = totalFare * 1.2

		if timeOut > 2200:
			totalFare = totalFare + 3

		return totalFare

	elif (day == 7): #sunday
		totalFare = totalFare + 5
		if timeOut > 2200:
			totalFare = totalFare + 3
		
		return totalFare


day = int(input("Enter day: "))
timeIn = int(input("Enter time in: "))
timeOut = int(input("Enter time out: "))
print("The total fare is $" + str(format(computeFee(day,timeIn,timeOut),'.2f')))
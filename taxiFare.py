import math

def computeFare(daytype, boardtime, dist):
	totalFare = 3.40

	#calculate basic cost from distance first
	if dist <= 1000:
		totalFare += 0
	elif dist <= 10200:
		extraCost = math.ceil((dist-1000)/400)*0.22
		totalFare += extraCost
	else: #dist > 10200
		previousCost = (9200/400)*0.22
		print(previousCost)
		extraCost = math.ceil((dist-10200)/350)*0.22
		print(extraCost)
		totalFare = totalFare + previousCost + extraCost

	#calculate total cost including surcharge
	if boardtime < 360:
		totalFare *= 1.5
	elif boardtime < 570:
		if daytype == 0:
			totalFare *= 1
		else:
			totalFare *= 1.25
	elif boardtime >= 1080:
		totalFare *= 1.25

	return totalFare

dayType = input("Enter day type ")
print(dayType)

boardHour = input("Enter board hour ")
boardMin = input("Enter board min ")

boardTime = (int(boardHour)*60) + int(boardMin)
print(boardTime)

distance = input("Enter distance ")
print(distance)

print(computeFare(int(dayType), int(boardTime), int(distance)))








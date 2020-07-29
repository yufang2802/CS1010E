def computeDays(day, month):
	if month == 1:
		return day
	if month == 2:
		return day + 31
	if month == 3:
		return day + 59
	if month == 4:
		return day + 89
	if month == 5:
		return day + 120
	if month == 6:		
		return day + 150
	if month == 7:
		return day + 181
	if month == 8:
		return day + 212
	if month == 9:
		return day + 242
	if month == 10:
		return day + 273
	if month == 11:
		return day + 303
	if month == 12:	
		return day + 334

day = input("Enter day ")
month = input("Enter month ")

print("Day " + day + " of month " + month + " is the " + str(computeDays(int(day),int(month))) + "th day of 2017.")

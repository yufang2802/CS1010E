def printSuffix(integer):
	if integer%100 == 11 or 12 or 13:
		return str(integer)+"th"
	if integer%10 == 1:
		return str(integer)+"st"
	if integer%10 == 2:
		return str(integer)+"nd"
	if integer%10 == 3:
		return str(integer)+"rd"
	else:
		return str(integer)+"th"

number = input("Enter integer ")

print(printSuffix(int(number)))
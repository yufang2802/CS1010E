def printOrdinal(century):
	if century%100 == 11 or century%100 == 12 or century%100 == 13:
		return str(century)+"th"
	elif century%10 == 1:
		return str(century)+"st"
	elif century%10 == 2:
		return str(century)+"nd"
	elif century%10 == 3:
		return str(century)+"rd"
	else:
		return str(century)+"th"

def printCentury(year):
	century = (year//100)+1
	return printOrdinal(century)

year = int(input("Enter year "))
print("The year " + str(year) + " falls in the " + printCentury(year) + " century.")
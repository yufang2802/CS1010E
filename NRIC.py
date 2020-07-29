def generateCode(nric):
	total = (int(nric[0])*2) + (int(nric[1])*7) + (int(nric[2])*6) + (int(nric[3])*5) + (int(nric[4])*4) + (int(nric[5])*3) + (int(nric[6])*2)
	remainder = total % 11
	subtract = 11 - remainder
	if subtract == 1:
		return 'A'
	if subtract == 2:
		return 'B'
	if subtract == 3:
		return 'C'
	if subtract == 4:
		return 'D'
	if subtract == 5:
		return 'E'
	if subtract == 6:
		return 'F'
	if subtract == 7:
		return 'G'
	if subtract == 8:
		return 'H'
	if subtract == 9:
		return 'I'
	if subtract == 10:
		return 'J'
	if subtract == 11:
		return 'K'

enter = input("Enter NRIC ")
print(generateCode(enter))
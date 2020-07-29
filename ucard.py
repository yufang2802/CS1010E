def issued(uCard):
	if 31 <= int(uCard[:2]) <= 35:
		print("Issued by East branch")
	elif 51 <= int(uCard[:2]) <= 55:
		print("Issued by West branch")
	else:
		print("Issued by Central branch")

def luhnah(uCard):
	uCard = [uCard] #putting into a list
	uCard = list(uCard[0]) #split the list
	uCard = [int(x) for x in uCard] #change all elements in list to integers
	uCard[-2::-2] = [2*x for x in uCard[-2::-2]] #double every other element from the back
	print(uCard)

	str1 = ''.join(str(e) for e in uCard) #convert back to string
	list1 = list(str1) #convert back to list
	list1 = [int(y) for y in list1] #converting all elements in list to integers
	print(list1)
	
	checkNumber = 0
	for i in range(0, len(list1)): #iterating through the whole list
		checkNumber = checkNumber + list1[i] #adding every element of the list 

	print("The check number is " + str(checkNumber))
	return checkNumber

uCard = input("Enter uCard Number: ")
# converted_uCard = list(map(int, uCard.split()))

if luhnah(uCard) % 7 == 0:
	print("Valid")
	issued(uCard)
else: 
	print("Invalid")

def winners(factor, musthave, participants):
	count = 0
	for i in range(1,participants+1):
		if i%factor == 0 and i%10 == musthave:
			count += 1
		elif i%factor == 0 and (i//10)%10 == musthave:
			count += 1
		elif i%factor == 0 and (i//100)%10 == musthave:
			count += 1
	return count

factor = int(input("Enter factor-digit: "))
musthave = int(input("Enter must-have-digit: "))
participants = int(input("Enter number of participants: "))
print("Number of winners: " + str(winners(factor,musthave,participants)))
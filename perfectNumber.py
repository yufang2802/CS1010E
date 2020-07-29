def is_perfect(integer):
	total = 0
	for i in range (1,integer):
		if (integer%i == 0):
			total = total + i

	if total == integer:
		return 1
	if total != integer:
		return 0

integer = input("Enter number: ")

while (int(integer) != 0):
	if (is_perfect(int(integer)) == 1):
		print(str(integer) + " is a perfect number.")
	if (is_perfect(int(integer)) == 0):
		print(str(integer) + " is not a perfect number.")
	integer = input("Enter number: ")
else:
	KeyboardInterrupt
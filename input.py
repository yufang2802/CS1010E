#case 1: total input values known

def inputfunc():
	count = 0
	while count < int(values_to_read):
		values_to_enter = input("Enter values ")
		count += 1

values_to_read = input("How many input values to read? ")

inputfunc()

print("Number of values entered = " + values_to_read)

#case 2: total input values unknown, terminate with negative integer

def inputfunc2():
	count = 0
	values_to_enter = 0
	while int(values_to_enter) >= 0:
		values_to_enter = input("Enter values ")
		count += 1

	print("Number of values entered = " + str(count-1))

print("Enter integers, terminate with a negative integer")

inputfunc2()

#case 3: total input values unknown, terminate with ctrl + C

def inputfunc3():
	count = 0
	values_to_enter = 0
	try:
		while True:
			values_to_enter = input("Enter values ")
			count += 1

	except KeyboardInterrupt:
		print("Number of values entered = " + str(count))

print("Enter integers, terminate with ctrl + C")

inputfunc3()
def countJumps(rocks,number):
	currPos = 0
	newPos = 0
	maxValue = 50
	totalNumJumps = 0
	
	for jumps in range(1, number+1):
		while (rocks[currPos] + maxValue >= rocks[newPos]):
			newPos += 1
			if (newPos > number):
				return totalNumJumps + 1
		newPos -= 1
		totalNumJumps += 1
		currPos = newPos
	return -1

number = int(input("Enter number of rocks "))
rocks = list(map(int, input("Enter rock positions ").split()))
# list -> creates array
# map(function, iterables) -> function that executes a specified function for each item in a iterable
# int -> convert string to integers
# split() -> splits a string into a list

rocks.insert(0, 0)
print(countJumps(rocks,number))
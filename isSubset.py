def isSubset(arrA, arrB):
	if(set(arrA).issubset(set(arrB))): 
		return 1
	else:
		return 0

print("1st array:")
arrayA = list(map(int, input("Enter 4 values ").split()))
print("2nd array:")
arrayB = list(map(int, input("Enter 7 values ").split()))

if isSubset(arrayA,arrayB) == 1:
	print("arrayA[" + str(arrayA) + "] is a subset of arrayB[" + str(arrayB) + "].")
elif isSubset(arrayA,arrayB) == 0:
	print("arrayA[" + str(arrayA) + "] is not a subset of arrayB[" + str(arrayB) + "].")
def sumArray(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sumArray(array[1:])

elements = int(input("Enter number of elements: "))
array = list(map(int, input("Enter " + str(elements) + " numbers: ").split()))
print("Array read: " + str(array))
print("Sum = " + str(sumArray(array)))
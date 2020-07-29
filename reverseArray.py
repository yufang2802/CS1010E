def reverse_array(array):
    if len(array) == 0:
        return []
    else:
        return [array.pop()] + reverse_array(array)


integers = int(input("Enter number of integers: "))
array = list(map(int, input("Enter integers: ").split()))
print("Reversed array: " + str(reverse_array(array)))
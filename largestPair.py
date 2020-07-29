def largest_pair(integer, maximum):
    if integer == 0:
        return maximum
    else:
        if integer%100 > maximum:
            maximum = integer%100
        return largest_pair(integer//100, maximum)


# faster method:
# def largest_pair(integer, maximum):
#     if integer == 0:
#         return maximum
#     else:
#         return largest_pair(integer // 100, max(integer % 100, maximum))

integer = int(input("Enter positive integer: "))
maximum = int(input("Maximum: "))
print("Largest pair of digits in " + str(integer) + " is " + str(largest_pair(integer, maximum)))
def present_on_day(n):
    if n == 1:
        return 1
    else:
        return n + present_on_day(n-1)

def present_thru_days(n):
    if n == 1:
        return present_on_day(n)
    else:
        return present_on_day(n) + present_thru_days(n-1)

day = int(input("Please enter the number of days: "))
print("You have entered the number of days as: ")
print("The number of presents received on day " + str(day) + " is " + str(present_on_day(day)) + ".")
print("The number of presents received in " + str(day) + " days is " + str(present_thru_days(day)) + ".")

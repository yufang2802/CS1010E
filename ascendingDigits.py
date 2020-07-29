def isAscending(int1,int2,int3):
	hundreds1 = (int1//100)%10
	hundreds2 = (int2//100)%10
	hundreds3 = (int3//100)%10
	if hundreds3 > hundreds2 > hundreds1:
		return 'Yes'
	else:
		return 'No'

int1 = input("Enter integer 1 ")
int2 = input("Enter integer 2 ")
int3 = input("Enter integer 3 ")

print(isAscending(int(int1), int(int2), int(int3)))
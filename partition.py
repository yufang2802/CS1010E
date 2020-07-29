import numpy as np

def partition(array, pivot):
	for i in array:
		if array[i] < pivot:
			np.where(array[i])




number = input("Enter the number of elements: ")
array = np.array(map(int, input("Enter " + number + " integers: ").split()))
pivot = input("Enter pivot: ")
def maxCherries(slices, cherries):
    totalCherries = sum(cherries)
    wholelist = cherries + cherries #so that we can start from any starting point in the pie 
    
    maxCherry = 0
    
    for round in range(slices): #for each starting point
        current = 0
        for slice in range(slices): #for each individual round, obtain maximum cherries
            if wholelist[slice + round] + current <= (totalCherries/2):
                current = current + wholelist[slice + round]
            else:
                if current > maxCherry:
                    maxCherry = current
    return maxCherry

slices = int(input("Enter number of slices: "))
cherries = list(map(int, input("Enter numbers of cherries: ").split()))
print("The maximum number of cherries Alice can get is " + str(maxCherries(slices, cherries)) + ".")

#max number of cherries is always <= total number of cherries
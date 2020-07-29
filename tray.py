# subtask 1

def min_unused_area(traySize, slabSize):
	vert = traySize[0] // slabSize[0]
	hori = traySize[1] // slabSize[1]
	trayArea = traySize[0] * traySize[1]
	minUnusedArea = trayArea - (slabSize[0]*slabSize[1]*vert*hori)
	return minUnusedArea
	

traySize = list(map(int, input("Enter tray size: ").split()))
slabSize = list(map(int, input("Enter slab size: ").split()))

traySize.sort()
slabSize.sort()

print("Minimum unused area: " + str(min_unused_area(traySize, slabSize)))


# subtask 2

def min_perimeter(traySize):
	for i in range(3):
		traySize[1] = traySize[1]/2
		traySize.sort()
	return (traySize[0]*2) + (traySize[1]*2)

print("Minimum perimeter after folding: " + str(min_perimeter(traySize)))

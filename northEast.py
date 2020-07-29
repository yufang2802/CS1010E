def ne(rowsColumns):
    if rowsColumns[0] == 0 or rowsColumns[1] == 0:
        return 1
    else: 
        return ne([rowsColumns[0]-1, rowsColumns[1]]) + ne([rowsColumns[0], rowsColumns[1]-1])

rowsColumns = list(map(int, input("Enter rows and columns apart: ").split()))
print("Rows and columns apart: " + str(rowsColumns))
print("Number of NE paths: " + str(ne(rowsColumns)))
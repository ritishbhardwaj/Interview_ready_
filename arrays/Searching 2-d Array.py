def search2dSortedMatrix(matrix,target):
    i=0 # number of rows in a matrix
    j=len(matrix[0])-1 #number of columns in a matrix
    n=len(matrix)
    while (i<n and j>=0):
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]>target:
            j-=1
        else:
            i+=1

    return False






matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=51
result=search2dSortedMatrix(matrix,target)
print(result)
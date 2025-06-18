#counting the no. of negative elements in the 2D matrix
def countNegatives(grid):
    count = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]<0:
                count+=1
    return count
m = int(input("enter the no. of rows "))
n = int(input("enter the no. of cols "))
for i in range(m):
    for j in range(n):
      grid = int(input("enter the element"))
countNegatives(grid)
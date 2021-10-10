## Solution : [paths-in-a-maze](./paths-in-a-maze.py)

# Feeling adventurous Kumar decides to explore a maze which is in the form of a matrix . The matrix's cells are numbered as (r,c) where r is the row number and c is the column number.

# The dimensions of the matrix are N x M (having N rows and M columns) . The maze consists of a total of N*M rooms. From a room you can only move to any room to its right or below it.

# So if you are present in a room (i,j) , you can move only to either room (i + 1, j ) or ( i , j + 1). You can not make any move that will take you out of the maze at any point . Some rooms in this maze are blocked and cannot be accessed so you cannot pass throught them even if you want to. Kumar , through sheer luck finds a map of the maze when he is in the starting room of the maze (1,1) (the topmost left cell) and the exit to the maze is at (N,M) (bottomost right cell) . Instead of actually navigating the maze he decides to find the number of ways there is to navigate the maze successfully from (1,1) to (N,M)

#  The maze will be given to you as a binary matrix. Output the total number of paths modulo 1000000007

### Input Description:
# First line contains two integers : N M denoting the no of rows and the no of columns of the matrix The next N lines contain M integers each . Each of these integers are either 0 or 1. 0 means that the room is free to pass through 1 means that the room is blocked and cannot be accessed

### Output Description:
# Output must consist of a single integer , the total number of paths modulo 1000000007

### Sample Input : 
# 2 2 
# 0 0 
# 1 0 
### Sample Output : 
# 1

## Solution :


r, c = map(int,input().split())
m1 = []
for i in range(r):
    m1.append(list(map(int,input().split())))
for i in range(r):
    for j in range(c):
        if m1[i][j] == 1:
            m1[i][j] = -1
if m1[0][0] == -1:
    print(0%1000000007)
else:
    for i in range(r):
        if m1[i][0] == 0:
            m1[i][0] = 1
        else:
            break
    for j in range(1, c):
        if m1[0][j] == 0:
            m1[0][j] = 1
        else:
            break

    for i in range(1, r):
        for j in range(1, c):
            if m1[i][j] == -1:
                continue
            if m1[i-1][j] > 0:
                m1[i][j] = m1[i][j] + m1[i-1][j]
            if m1[i][j-1] > 0:
                m1[i][j] = m1[i][j] + m1[i][j-1]
    if m1[r-1][c-1] > 0:
        print(m1[r-1][c-1]%1000000007) 
    else:
        print(0%1000000007)       
        
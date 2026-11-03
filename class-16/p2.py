# ho3 to take m x n matrix as input from user and store it in a list of lists
m = int(input())
n = int(input())
l = []          # our 2d list, m x n
i = 0
while i < m:
    j = 0
    l.append([])
    while j < n:
        x = int(input())
        l[i].append(x)
        j += 1
    i += 1
    print(l[i-1])



m = int(input())
n = int(input())
matrix = []          # our 2d list, m x n
i = 0
while i < m:
    tmp = []
    j = 0
    while j < n:
        x = int(input())
        tmp.append(x)
        j += 1
    matrix.append(tmp)
    i += 1
print(matrix)


i = 0
while i < m:   
    j = 0
    while j < n:
        print(matrix[i][j], end=" ")
        j += 1
    print()
    i += 1
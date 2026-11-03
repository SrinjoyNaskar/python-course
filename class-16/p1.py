l = [[1, 2, 3], [0,8], [7, 6, 5, 4]]
sum = 0
i = 0
while i < len(l):
    j = 0
    while j < len(l[i]):
        sum += l[i][j]
        j += 1
    i += 1
print(sum)
r,c = map(int,input().split())          #row and column sum
print("Row sums:")
l = []
i = 0
while i < r:
    w = list(map(int,input().split()))
    l.append(w)
    i += 1

row = 0
while row < r:
    col = 0
    sum = 0
    while col < c:
        sum += l[row][col]
        col += 1
    print(sum)
    row += 1

print("Column sums:")
col = 0
while col < c:
    row = 0
    sum = 0
    while row < r:
        sum += l[row][col]
        row += 1
    print(sum)
    col += 1
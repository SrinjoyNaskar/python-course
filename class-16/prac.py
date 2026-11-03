l = []
n = int(input())
i = 0
while i < n:
    x = int(input())
    l.append(x)
    i += 1

print(l)

sum = 0
i = 0
while i < len(l):
    sum += l[i]
    i += 1
print(sum)
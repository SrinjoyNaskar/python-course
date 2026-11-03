n = int(input())
l = []
sum = 0
i = 0
while i < n:
    l.append(int(input()))
    i += 1

while i < len(l):
    sum += l[i]
    i += 1
average = sum / len(l)
print(average)
cnt = 0
i = 0
while i < n:
    if l[i] > average:
        cnt += 1
    i += 1
print(cnt)
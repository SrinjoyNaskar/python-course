l = [3, 8, 1, 9, 4, 100]

# l.sort()
# print(l[0],l[-1])         using sort function to find max and min

# print(max(l), min(l))     using max and min function to find max and min

i = 0
max = l[0]
min = l[0]
while i < len(l):
    if l[i] > max:
        max = l[i]
    if l[i] < min:
        min = l[i]
    i += 1
print(max, min)

# i = 0 
# while i < len(l):
#     if l[i] == max:
#         l.remove(l[i])
#     i += 1

# sec_max = l[0]
# i = 1
# while i < len(l):
#     if l[i] > sec_max:
#         sec_max = l[i]
#     i += 1
# print(sec_max)

i = 0
curr = -99999999999999999999999999
while i < len(l):
    if l[i] > curr and l[i] < max:
        curr = l[i]
    i += 1
print(curr)

i = 0
max1 = l[0]
max2 = l[0]
while i < len(l):
    if l[i] > max1:
        max2 = max1
        max1 = l[i]
    elif l[i] > max2 and l[i] != max1:
        max2 = l[i]
    i += 1
print(max1, max2)


f_max = max(l[0], l[1])
s_max = min(l[0], l[1])
i = 2
while i < len(l):
    if l[i] > f_max:
        s_max = f_max
        f_max = l[i]
    elif l[i] > s_max and l[i] != f_max:
        s_max = l[i]
    i += 1
print(f_max, s_max)
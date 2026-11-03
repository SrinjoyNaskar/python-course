# a = int(input())
# b = int(input())
# gcd = 1
# i = 1
# while i <=min(a, b):
#     if a % i == 0 and b % i == 0:
#         gcd = i
#     i += 1
# print(gcd)

# a = int(input())
# b = int(input())
# if a == 0 or b == 0:
#     print(max(a, b))
# else:
#     limit = min(a, b)
#     i = 1
#     gcd = 1
#     while i <= limit:
#         if a % i == 0 and b % i == 0:
#             gcd = i
#         i += 1
#     print(gcd)

# a = int(input())
# b = int(input())
# i = min(a, b)
# while i >=1:
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break
# i -= 1


a = int(input())
b = int(input())
c = max(a, b) 
if a == 0 or b == 0:
    print(0)
else:    
    while c <= a * b: 
        if c % a == 0 and c % b == 0:
            print(c)
            break
        c += 1


a = int(input())
b = int(input()) 
while b != 0:
    r = a % b
    a = b
    b = r
print(a)
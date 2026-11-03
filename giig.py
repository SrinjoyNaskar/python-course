# m, n = map(int, input().split())
# print(m * n//2)                 #floor division as we need to find the number of dominoes that can be placed in the grid

# c = input()
# if c in "codeforces":
#     print("YES")                        #c was in uppercase, so it was not found in the string "codeforces"
# else:
#     print("NO")

# n, a, b = map(int, input().split())

# if 2 * a < b:
#    print(n * a)
# else:
#     print((n // 2) * b + (n % 2) * a)

# a, b = map(int, input().split())
# if a == 1 and b == 1:
#         print(a+b)
# else:
#         print(max(a, b))

# n = int(input())

# if n % 2 == 0:
#     print(-n// 2)
# else:
#     print((n + 1) // 2)

# a, b = map(int, input().split())

# x = min(a, b)
# y = max(a, b)

# print(max(y, 2 * x) ** 2)


# n, m, a = map(int, input().split())
# print((n // a) * (m // a))

# b1, b2, b3 = map(int, input().split())
# print((b1 + b2 - b3)//2, (b1 + b3 - b2)//2, (b2 + b3 - b1)//2)

# n = int(input())
# if n % 2 == 1:
#     print("Alice")
# else:
#     print("Bob")



# score = int(input())
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")



# unit=int(input())
# if unit<=100:
#     print(unit*2.5)
# else:
#     print(100*1.5+(unit-100)*2.5)



# # Write your reference solution here
# unit=int(input())
# if unit<=100:
#     print(f"{100*1.5:.2f}")
# else:
#     print(f"{100*2.5:.2f}")

# n=int(input())
# if average > 80 and score1 >= 60 and score2 >= 60 and score3 >= 60:
#     print("Distinction awarded.")
# else:
#     print("No distinction awarded.")


# n = int(input())

# location = set()
# i=1
# while i <= n:
#     x, y = map(int, input().split())
#     location.add((x,y))

#     print(len(location))
# for x,y in sorted(location):
#     print(x,y)

# n = int(input())
# banned = set(input().split())
# q = int(input())
# names = input().split()

# for username in names:
#     if username in banned:
#         print("YES")
#     else:
#         print("NO")

# n = input().split()

# longest = max(n, key=len)
# print(longest)


# n = int(input())

# h = n // 3600
# n = n % 3600

# m = n // 60
# n = n % 60

# print(f"{h} hours, {m} minutes, {n} seconds")

# n = int(input())

# f = n // 500
# n = n % 500

# h = n // 100
# n = n % 100

# t = n // 50

# print(f"500s: {f}, 100s: {h}, 50s: {t}")

# n = int(input())

# if n < 5:
#     print(0)

# elif n <= 12:
#     print(100)

# elif n <= 59:
#     print(200)

# else:
#     print(120)

# n = int(input())

# if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# reading = int(input())
# express = int(input())

# if reading <= 1:
#     base = 40 

# elif reading <= 5:
#     base = 80

# else:
#     base = 150

# total = base
# if express == 1:
#     total = total + 50

# print(base)
# print(total)

# units = int(input())

# if units <= 100:
#     bill = units * 5

# elif units <= 200:
#     bill = 100*5 + (units-100) * 7

# else:
#     bill = 100*5 + 100 * 7 + (units - 200) * 10

# print(bill)

# a = int(input())
# b = int(input())
# c = int(input())

# if a == b == c:
#     print("eqilateral")

# elif a == b or b == c or a == c:
#     print("isoscles")

# else:
#     print("scalene")

goal = int(input())
savings = int(input())

months = 0
total_savings = 0

while total_savings < goal:
    total_savings += savings
    months += 1



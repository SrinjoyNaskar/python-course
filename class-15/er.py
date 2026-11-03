# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1

#-------------------------------------

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n-i:
#         print(" ", end=" ")
#         j+= 1
#     j = 1
#     while j<= i:    
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1

#-------------------------------------

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n-i:
#         print(" ", end=" ")
#         j+= 1
#     j = i
#     while j > 0:    
#         print(j, end=" ")
#         j -= 1
#     print()
#     i += 1

#-------------------------------------



n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n-i:
        print(" ", end=" ")
        j += 1

    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1

    j = i-1
    while j >= 1:
        print(j, end=" ")
        j -= 1

    print()
    i += 1


# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j >=i and j <= n-i+1:
#         print(" ", end=" ")
#         j += 1
#     j = 1
#     while j <= 2*i-1:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1


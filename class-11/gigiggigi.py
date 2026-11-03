# x=int(input())

# if x%2==0:
#     print("Even")
# if x%2!=0:
#     print("Odd")



# x=int(input("enter a number: "))
# if x%3==0 and x%5!=0:
#     print("fizz")
# if x%5==0 and x%3!=0:                      #consider all the cases use != 
#     print("buzz")
# if x%3==0 and x%5==0:
#     print("fizzbuzz")


#     x=int(input())
# if x%3==0:
#     print("fizz", end=" ")
# if x%5==0:                     #consider all the cases use != 
#     print("buzz")



# x = int(input())

# if x > 20:
#     x = x + 20
# elif x > 10:
#     x = x + 10


# x=int(input())
# if x>=18:
#     print("you can vote")

# x=int(input())
# if x%4==0 and x%100!=0 or x%400==0:
#     print("leap year")

# #25-31 hw

# x=float(input())

# if x>1000:
#     d=x-(x*0.1)
#     print(f"{d:.2f}")

# x = int(input())

# percentage = (x / 150) * 100

# if percentage >= 90:
#     print(f"Merit scholarship awarded. Percentage: {percentage:.2f}%")


# x = int(input())
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")

x=float(input())
if x==0.0:
    print("No trip.")
elif x<=2.0:
    print(f"fare: Rs.{50.00:.2f}",sep="")
else:
    amnt= 50+15*(x-2)
    print(f"fare: Rs.{amnt:.2f}",sep="")
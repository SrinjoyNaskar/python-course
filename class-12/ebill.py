units = int(input())
if units <= 100:
    print(f"Bill: Rs.{units * 3:.2f}")
elif units <= 200:
    print(f"Bill: Rs.{100 * 3 + (units - 100) * 5:.2f}")
elif units <= 300:
    print(f"Bill: Rs.{100 * 3 + 100 * 5 + (units - 200) * 7:.2f}")
else:
    print(f"Bill: Rs.{100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10:.2f}")

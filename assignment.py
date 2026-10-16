tickets = int(input("Enter the number of tickets: "))
student = input("Are you a student? (yes/no): ")
money = int(input("Enter the money you have: "))

if student == "yes" and tickets >= 8:
    price = 7
elif student == "yes" and tickets < 8:
    price = 10
elif student == "no" and tickets >= 8:
    price = 10
else:
    price = 13

total_cost = tickets * price

print(f"Price per ticket: {price}")
print(f"Total cost: {total_cost}")

if money > total_cost:
    money_left = money - total_cost
    print(f"Money left: {money_left}")
elif money == total_cost:
    print("Exactly enough money.")
else:
    money_needed = total_cost - money
    print(f"Money needed: {money_needed}")
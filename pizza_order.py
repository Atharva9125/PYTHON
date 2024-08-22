print("Welcome to Pizza Hut")
size = input("What size do you want?S,L or M ")
wants_pepperoni = input("Do you want pepperoni on your pizza?Yes or No")
wants_extra_cheese = input("Do you want extra cheese?Yes or No")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if wants_pepperoni == "Yes":
    if size == "S":
        bill += 2
    else:
        bill += 3
if wants_extra_cheese == "Yes":
    bill += 1

print(f"Your bill is: ${bill}")

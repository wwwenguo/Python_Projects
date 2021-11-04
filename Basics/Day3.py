# Odd or Even
num = input("Please enter an int number: ")
num = int(num)
if num % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")

# Leap year
year_num = input("Please enter the year: ")
year_num = int(year_num)
if year_num % 4 == 0:
    if year_num % 100 == 0:
        if year_num % 400 == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")

# Pizza Order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is {bill}.")


# Love Calculator - can combine two strings first, then use the count() method.
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
name1_lower = name1.lower()
name2_lower = name2.lower()
score = (name1_lower.count("t") + name1_lower.count("r") + name1_lower.count("u") + name1_lower.count("e") + name2_lower.count("t") + name2_lower.count("r") + name2_lower.count("u") + name2_lower.count("e")) * \
    10 + name1_lower.count("l") + name1_lower.count("o") + name1_lower.count("v") + name1_lower.count(
        "e") + name2_lower.count("l") + name2_lower.count("o") + name2_lower.count("v") + name2_lower.count("e")
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# Treasure island
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_right = input("Turn left or right? ")
if left_right.lower().find("left") > -1:
    swim_wait = input("Swin or Wait? ")
    if swim_wait.lower().find("swin") > -1:
        print("Game Over!")
    else:
        door = input(
            "Which color you choose for the door? red, blue or yellow? ")
        if door.lower().find("yellow") > -1:
            print("You Win!")
        else:
            print("Game Over!")
else:
    print("Game Over!")

# multi-block
print('''aaaaaaaaaa
bbbbbbbbbb
cccccccccc''')

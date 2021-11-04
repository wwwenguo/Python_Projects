import random

# Flip a Coin
num = random.randint(1, 2)
if num == 1:
    print("Heads")
else:
    print("Tails")

# Who pays the bill
name = input("Candidates seperated by comma\n")
names = name.split(", ")
num = random.randint(1, len(names))
print(f"{names[num-1]} pays the bill.")
# A simple way to do that using build-in function "random.choice()"
person = random.choice(names)
print(f"{person} pays the bill.")

# Which block you want to place treasure
row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]
print(f"{row1}\n{row2}\n{row3}")
num = input("Please pick a spot:\n")
col = int(num[0]) - 1
row = int(num[1]) - 1
rows = [row1, row2, row3]
rows[row][col] = "X"
print(f"{rows[0]}\n{rows[1]}\n{rows[2]}")

# Scissors Game
num1 = input(
    "What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
num1 = int(num1)
# Fix a bug of beyond range
if num1 > 2 or num1 < 0:
    print("Invalid Number. You Lose!")
num2 = random.randint(0, 2)
l = ["Rock", "Paper", "Scissors"]
print(f"The computer choose {l[num2]}.")
if num1 > num2:
    if (num1 - num2) == 1:
        print("You Win!")
    else:
        print("You lose!")
elif num1 == num2:
    print("Draw. Try Again!")
else:
    if (num2 - num1) == 1:
        print("You lose!")
    else:
        print("You Win")

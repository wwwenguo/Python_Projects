# first piece
num = input("Type a two digit number: ")
num1 = int(num[0])
num2 = int(num[1])
result = num1 + num2
print(result)

# second piece
age = input("What is your current age?\n")
years = 90 - int(age)
days = years * 365
weeks = years * 52
months = years * 12
print(f"You have {days} days, {weeks} weeks and {months} months left.")

# tip calculator
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?\n")
tip_percentage = input(
    "What percentage tip would you like to give? 10, 12 or 15?\n")
num_people = input("How many people to split the bill?\n")
result = round(float(total_bill) * (float(tip_percentage) /
                                    100 + 1) / float(num_people), 2)
print(f"Each person should pay: {result}.")

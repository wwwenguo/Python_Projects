# # for loop # can use the combination of sum() and len() function
# student_heights = input("Input a list of student heights:\n").split()
# count = 0
# for x in student_heights:
#     y = int(x)
#     count += y

# average_height = round(count / (len(student_heights)))

# print(f"The average student height is {average_height}.")

# # Add the even number
# total = 0
# for number in range(2, 101, 2):
#     # print(number)
#     total += number
# print(total/(len(range(2, 101, 2))))

# # FizzBuzz
# for number in range(1, 101):
#     if number % 3 == 0:
#         if number % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Passcode Generator
import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_upper = []
for x in letter:
    letter_upper.append(x.upper())

letter.extend(letter_upper)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = random.choices(letter, k=num_letters)
password1 = random.choices(numbers, k=num_numbers)
password2 = random.choices(symbols, k=num_symbols)
password.extend(password1)
password.extend(password2)
random.shuffle(password)

passcode = ''

for x in password:
    passcode += x

print(passcode)

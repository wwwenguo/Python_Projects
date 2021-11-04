# caeser cipher
import os
def clear(): return os.system('cls')
# from replit import clear - need to install the replit module


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # double inputs to avoid out of range when plus the shift (encode)

continue_game = True

while continue_game:
    clear()
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    # In case the inputs are large numbers
    shift = int(input("Type the shift number:\n")) % 26

    def caeser(text, shift, direction):
        caeser_text = []  # Can do plain string then add up char each time
        if direction == 'decode':
            shift *= -1
        for char in text:  # can use this if .. in .. statements to add more encrypted lists, such as Capis and symbols and numbers
            if char in alphabet:
                index = alphabet.index(char)
                # Python can do nagetive index!! So don't worry it will be out of range when devided!!!
                new_index = index + shift
                char = alphabet[new_index]
                caeser_text.append(char)
            else:
                caeser_text.append(char)
        new_text = "".join(caeser_text)
        print(f"Your {direction}d message is: '{new_text}'")

    caeser(text, shift, direction)

    whether_continue = input(
        "Input 'Y' to continue the process and 'N' to exit.")
    if whether_continue == 'N':
        continue_game = False

# Use while loops and booleans to control when the game ends

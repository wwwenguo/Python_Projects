# blackjack
import random
import os
def clear(): return os.system('cls')


cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q']
end_game = False

while not end_game:
    # pick two cards for the player
    player_cards = random.sample(cards, 2)
    print(f"Your cards are: {player_cards}")
    # pick two cards for the computer
    computer_cards = random.sample(cards, 2)
    print(f"The computer's first card is: {computer_cards[0]}")

    def sum_of_cards(card_list, values_of_A):
        """ returns the sum of a card list
            parameters: a card list and a list of the chosen values of A
            returns an int value of sum
        """
        s = 0
        for x in card_list:
            if x == "J" or x == 'K' or x == 'Q':
                s += 10
            elif x == 'A':
                s += values_of_A[0]
                values_of_A.pop(0)
            else:
                s += x
        return s

    def who_wins(result_dict):
        """ print who wins
            parameters: a dict contains the players and the sums
            no returns
        """
        a = list(result_dict.keys())
        if result_dict[a[0]] > 21 and result_dict[a[1]] > 21:
            print("Congrats! You Win!")
        elif result_dict[a[0]] > result_dict[a[1]]:
            if result_dict[a[0]] > 21:
                print(f"{a[1]} Win!")
            else:
                print(f"{a[0]} Win!")
        elif result_dict[a[0]] < result_dict[a[1]]:
            if result_dict[a[1]] > 21:
                print(f"{a[0]} Win!")
            else:
                print(f"{a[1]} Win!")
        elif result_dict[a[0]] == result_dict[a[1]]:
            print("Draw!")

    results = {
        'You': 0,
        'Computer': sum_of_cards(computer_cards, [random.choice([1, 11])]),
    }

    continue_game = True
    while continue_game:
        if_add_cards = input(
            "Input 'add' to get one more card or input 'skip' to continue:\n")
        if if_add_cards == 'skip':
            print(f"The computer's second card is: {computer_cards[1]}")

            counts_of_A = player_cards.count('A')
            A_list = []
            while counts_of_A > 0:
                g = int(
                    input("What value you want the 'A' to be? Type '1' or '11'\n"))
                while g not in [1, 11]:
                    g = int(
                        input("Invalid Input. Please input number '1' or '11'\n"))
                A_list.append(g)
                counts_of_A -= 1

            results['You'] = sum_of_cards(player_cards, A_list)
            who_wins(results)
            continue_game = False

        if if_add_cards == 'add':
            new_card = random.choice(cards)
            player_cards.append(new_card)
            print(
                f"Your new card is {new_card}, now your cards are {player_cards}")

    if_end_game = input(
        "Input any key to continue the game or input 'bye' to end the game\n")

    if if_end_game == 'bye':
        end_game = True
    clear()

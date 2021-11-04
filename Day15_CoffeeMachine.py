# Coffee Machine
espresso = {
    'Water': '50 mL',
    'Coffee': '18 g',
    'Milk': '0 mL',
    'Price': '$ 1.50',
}

latte = {
    'Water': '200 mL',
    'Coffee': '24 g',
    'Milk': '150 mL',
    'Price': '$ 2.50',
}

cappuccino = {
    'Water': '250 mL',
    'Coffee': '24 g',
    'Milk': '100 mL',
    'Price': '$ 3.00',
}

container = {
    'Water': '300 mL',
    'Coffee': '100 g',
    'Milk': '200 mL',
}


def separate_string(input_string):
    return int(input_string.split(' ')[0])


def separate_price(input_price):
    return float(input_price.split(' ')[1])


def print_dict(single_dict):
    for x, y in single_dict.items():
        print(f"{x}: {y}")


def flavor_fun(flavor, reservoir, flavor_name):
    if separate_string(reservoir['Water']) >= separate_string(flavor['Water']) \
            and separate_string(reservoir['Coffee']) >= separate_string(flavor['Coffee']):
        print_dict(flavor)
        print('Please insert coins.')
        money_get = 0
        quarter_count = 0
        dimes_count = 0
        nickel_count = 0
        pennies_count = 0
        while money_get < separate_price(flavor['Price']):
            print('Not enough money.')
            quarter_count += int(input('Add quarters: '))
            dimes_count += int(input('Add dimes: '))
            nickel_count += int(input('Add nickels: '))
            pennies_count += int(input('Add pennies: '))
            money_get = 0.25 * quarter_count + 0.1 * dimes_count + 0.05 * nickel_count + 0.01 * pennies_count
        print(f"Here is ${round(money_get - separate_price(flavor['Price']), 2)} in change.")
        print(f"Here is your {flavor_name}. Enjoy!")
        water_left = separate_string(reservoir["Water"]) - separate_string(flavor['Water'])
        coffee_left = separate_string(reservoir['Coffee']) - separate_string(flavor['Coffee'])
        milk_left = separate_string(reservoir['Milk']) - separate_string(flavor['Milk'])
        reservoir['Water'] = str(water_left) + ' mL'
        reservoir['Coffee'] = str(coffee_left) + ' g'
        reservoir['Milk'] = str(milk_left) + ' mL'
        return reservoir
    else:
        print("Not enough ingredients! Please check 'report' and add!")


def main():
    function_well = True
    while function_well:
        input1 = input('What would you like? (espresso/latte/cappuccino): ')
        print(input1)
        if input1 == 'report':
            print_dict(container)
        elif input1 == 'espresso':
            flavor_fun(espresso, container, input1)
        elif input1 == 'latte':
            flavor_fun(latte, container, input1)
        elif input1 == 'cappuccino':
            flavor_fun(cappuccino, container, input1)
        elif input1 == 'off':
            function_well = False
        else:
            print("Invalid input!")


if __name__ == '__main__':
    main()



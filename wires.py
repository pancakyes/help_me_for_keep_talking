import os
#import help_me_for_keep_talking

def wires_menu():
    # print options
    _ = os.system("clear")
    print('Which wires combination do you see?')
    print('Use B for Black wire, R for Red, W for white, Y for yellow, N - for navy Blue')
    combination = input('Please, enter the sequence of wires from top to bottom. For example, BYY or choose 0 for main menu: ')
    combination = combination.lower()

    if combination == '0':
        return

    for letter in combination:
        if letter not in 'brwyn':
            wires_menu()

    # choosing options
    number_of_wires = len(combination)
    if number_of_wires == 3:
        wire = three_wires(combination)
    elif number_of_wires == 4:
        wire = four_wires(combination)
    elif number_of_wires == 5:
        wire = five_wires(combination)
    elif number_of_wires == 6:
        wire = six_wires(combination)
    else:
        wires_menu()
    print ('Cut the {} wire'.format(wire))
    print()
    next_step = input('1 - for next wire collection\n2 - for main menu: ')

    if next_step == '1':
        wires_menu()
    else:
        return

def three_wires(combination):
    # If there are no red wires, cut the second wire.
    if not 'r' in combination:
        return 'second'

    # Otherwise, if the last wire is white, cut the last wire.
    elif combination[-1] == 'w':
        return 'last'

    # Otherwise, if there is more than one blue wire, cut the last blue wire
    elif combination.count('n') > 1:
        return 'last blue'

    # Otherwise, cut the last wire.
    else:
        return 'last'

def four_wires(combination):
    # If there is more than one red wire and the last digit of the serial number is odd, cut the last red wire.
    if combination.count('r') > 1 and last_number_of_serial_number():
        return 'last red'

    # Otherwise, if the last wire is yellow and there are no red wires, cut the first wire.
    elif not 'r' in combination and combination[-1] == 'y':
        return 'first'

    # Otherwise, if there is exactly one blue wire, cut the first wire.
    elif combination.count('n') == 1:
        return 'first'

    # Otherwise, if there is more than one yellow wire, cut the last wire.
    elif combination.count('y') > 1:
        return 'last'

    # Otherwise, cut the second wire.
    else:
        return 'second'

def five_wires(combination):
    # If the last wire is black and the last digit of the serial number is odd, cut the fourth wire.
    if combination[-1] == 'b' and last_number_of_serial_number():
        return 'fourth'

    # Otherwise, if there is exactly one red wire and there is more than one yellow wire, cut the first wire.
    elif combination.count('r') == 1 and combination.count('y') > 1:
        return 'first'

    # Otherwise, if there are no black wires, cut the second wire.
    elif 'b' not in combination:
        return 'second'

    # Otherwise, cut the first wire
    else:
        return 'first'

def six_wires(combination):
    # If there are no yellow wires and the last digit of the serial number is odd, cut the third wire
    if 'y' not in combination and last_number_of_serial_number():
        return 'third'

    # Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
    elif combination.count('y') == 1 and combination.count('w') > 1:
        return 'fourth'

    # Otherwise, if there are no red wires, cut the last wire.
    elif 'r' not in combination:
        return 'last'

    # Otherwise, cut the fourth wire
    else:
        return 'fourth'

def last_number_of_serial_number():
    while True:
        serial_number = input("Please, enter bomb's serial number: ")
        if serial_number[-1].isdigit():
            return int(serial_number[-1]) % 2 == 1


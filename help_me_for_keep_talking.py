import sys
import os
import wires

def menu_list():
    menu = {}
    menu['1'] = ' - Wires'
    menu['2'] = ' - Button'
    menu['0'] = ' - Exit'
    return menu

def main_menu(menu_options):
    while True:
        # clear the screen
        _ = os.system("clear")
        # print the menu 
        for key in menu_options:
            print (key, menu_options[key])
        print('')
        type_of_module = input("Please, choose a type of module or exit: ")

        # choosing options
        if type_of_module == '1':
            wires.wires_menu()
        elif type_of_module == '2':
            print ('Nothing here')
        elif type_of_module == '0':
            sys.exit()
        else:
            main_menu(menu_options) 

# main part
menu_options = menu_list()
main_menu(menu_options) 

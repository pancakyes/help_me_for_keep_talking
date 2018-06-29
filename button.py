def buttons():
    # clear the screen
     _ = os.system("clear")
    label = input('Enter the label from the button or 0 for main menu: ')

    if label == '0':
        return

    color = input('Enter the color of the button. B - for blue, W - for white, Y - for yellow, R - for red, X - for other colors')

    label = label.lower()
    color = color.lower()
    
    # If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button".
    if color == 'b' and label == 'abort':
        pass

    # If there is more than 1 battery on the bomb and the button says "Detonate", press and immediately release the button.
    elif 


def number_of_batteries():
    number = input('How many batteries do you see? ')
    return int(number)

def colored_strip():
    color = input('Which color does have strip on the right? (B)lue, (W)hite, (Y)ellow or (O)ther?')
    color = color.lower()
    if color == 'b':
        return 4
    elif color == 'w':
        return 1
    elif color == 'y':
        return 5
    else:
        return 1 

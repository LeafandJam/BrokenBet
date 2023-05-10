print('''██████╗ ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██████╗ ███████╗████████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██████╔╝█████╗     ██║   ███████╗
██╔══██╗██╔══██╗██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██╔══██╗██╔══╝     ██║   ╚════██║
██████╔╝██║  ██║╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██████╔╝███████╗   ██║   ███████║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝
                                                                                        

''')
calc = input("Welcome to Broken Bets! \nBegin calculations? [y/n] ")
if calc == 'y':
    game = True
else:
    print('Bruh')


while game == True:

    oddHi = float(input('What is the highest odd? '))
    oddLo = float(input('What is the lowest odd? '))
    bonusMoney = int(input('What is the amount of bonus money? '))

    investment = ((oddHi * bonusMoney) - bonusMoney) / oddLo

    profit1 = ((oddHi * bonusMoney) - bonusMoney) - investment
    profit2 = (oddLo * investment) - investment

    print('\n\nYou must put in $',investment,'.')
    print('\nThe profit is:\n $', profit1,'\n $',profit2)

    calc2 = input('\n\n Would you like to calculate another game? [y/n] ')
    if calc2 != 'y':
        print("Good luck!")
        game = False




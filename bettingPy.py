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
    bonusMoney = int(input('What is the amount of bonus money? $'))
elif calc == 'n':
    print('Bruh')




while game == True:

    oddHi = float(input('What is the highest odd? '))
    oddLo = float(input('What is the lowest odd? '))


    investment = ((oddHi * bonusMoney) - bonusMoney) / oddLo

    profit1 = ((oddHi * bonusMoney) - bonusMoney) - investment
    profit2 = (oddLo * investment) - investment

    print('\n\nYou must put in $',investment,'.')
    print('\nThe profit is:\n $', profit1,'\n $',profit2)

    calc2 = input("\n\n Would you like to calculate another game? ('c' will clear the bonus money) [y/n/c] ")
    if calc2 != 'y' and calc2 != 'c':
        print("Good luck!")
        game = False
    elif calc2 == 'c':
        bonusMoney = int(input('What is the new bonus money? $'))




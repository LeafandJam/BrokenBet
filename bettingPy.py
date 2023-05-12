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

    calc2 = input("\n\n Would you like to calculate another game? \n ('c' will clear the bonus money) ('b' will let you type the name of the team to remember it)\n [y/n/c/b] ")
    if calc2 != 'y' and calc2 != 'c' and calc2 != 'b':
        print("Good luck!")
        game = False

    elif calc2 == 'c':
        bonusMoney = int(input('What is the new bonus money? $'))
    
    elif calc2 == 'b':
        bookmark = input("What team is this? ")
        print("\n\n The team is: ",bookmark)
        print('You must put in $',investment,'.')
        print('The profit is:\n $', profit1,'\n $',profit2,'\n\n')




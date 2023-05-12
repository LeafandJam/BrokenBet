print('''
██████╗ ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██████╗ ███████╗████████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██████╔╝█████╗     ██║   ███████╗
██╔══██╗██╔══██╗██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██╔══██╗██╔══╝     ██║   ╚════██║
██████╔╝██║  ██║╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██████╔╝███████╗   ██║   ███████║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝
                                                                                        

''')

bookmarks = []
mode = 'mainMenu'

while mode == 'mainMenu':
    print('Welcome to Broken Bets!\n')
    print('''
Game calculations   [g]
Profit calculations [p]
Bookmarks           [b]
Exit                [e]
''')
          
    options = ['g','p','e','b']

    choice = input("\nWhat would you like to do? ")

    if choice == 'g':
        mode = 'game'
        bonusMoneyTrigger = 0
    
    elif choice == 'e':
        mode = 'exit'
    
    elif choice == 'p':
         mode = 'profit'
    
    elif choice == 'b':
         mode = 'bookmark'
        
    while choice not in options:
            print('Bruh pick one: ',options)
            choice = input("What would you like to do? ")



    while mode == 'bookmark':
        print(bookmarks)
        userChoice = input('Would you like to go back to the menu? [y/n]: ')
        if userChoice == 'y':
            mode = 'mainMenu'
            print('beans')


    while mode == 'game':
        if bonusMoneyTrigger == 0:
            bonusMoney = int(input('What is the amount of bonus money? $'))
            bonusMoneyTrigger += 1

            while bonusMoney <= 0:
                    print("can't have $0 bonus money you fool")
                    bonusMoney = int(input('What is the amount of bonus money? $'))
                    bonusMoneyTrigger += 1


        oddHi = float(input('What is the highest odd? '))
        oddLo = float(input('What is the lowest odd? '))

        # Maths
        investment = ((oddHi * bonusMoney) - bonusMoney) / oddLo
        profit1 = ((oddHi * bonusMoney) - bonusMoney) - investment
        profit2 = (oddLo * investment) - investment
        ##

        print('\n\nYou must put in $',investment,'.')
        print('\nThe profit is:\n $',profit1,'\n $',profit2,'.')

        calc2 = input("\n\n Would you like to calculate another game? \n('c' clear the bonus money) \n('b' create a bookmark)\n('m' main menu) \n [y/n/c/b/m] ")
        if calc2 != 'y' and calc2 != 'c' and calc2 != 'b' and calc2 != 'm':
            print("Good luck!")
            mode = exit

        elif calc2 == 'c':
            bonusMoney = int(input('What is the new bonus money? $'))
            while bonusMoney <= 0:
                print("can't have $0 bonus money you fool")
                bonusMoney = int(input('What is the amount of bonus money? $'))

        elif calc2 == 'b':
            bookmark = input("Write your bookmark: ")
            bookmarks.append(bookmark)
            print('\nAdded to bookmarks. Go to the main menu to view them\n')
            calc2 = input("Would you like to calculate another game? \n[y/n/] ")
            if calc2 == 'n':
                 mode = 'mainMenu'
                 
        elif calc2 == 'm':
            mode = 'mainMenu'
            
        elif calc2 == 'n':
            exit

    while mode == 'profit':

        print("\nCalculate how much money you need to pay your partner or vice versa.\n")
        gameOne = float(input('How much TOTAL did you make from Game #1? $'))
        gameTwo = float(input('How much TOTAL did you make from Game #2? $'))
        ownMoney = int(input('How much of your personal money did you put in? $'))
        
        if gameOne == 0 and gameTwo == 0:
            print('\nYou lost both. Continue to calculate how much your partner owes you.\n')
            gameOne = float(input('How much TOTAL did YOUR PARTNER make from Game #1? $'))
            gameTwo = float(input('How much TOTAL did YOUR PARTNER make from Game #2? $'))
            otherPersonsMoney = int(input('How much of YOUR PARTNER\'S personal money did they put in? $'))

            totalPay = (((gameOne + gameTwo) - (ownMoney + otherPersonsMoney)) /2) + otherPersonsMoney
            print('\nYour partner must send $',totalPay,' to you. You don\'t have to send anything (you lost both games).')
            profit = totalPay-otherPersonsMoney
            print('\nYou made $',profit,' PROFIT')



        elif gameOne == 0 and gameTwo > 0:
             totalPay = gameTwo - ownMoney
             print('\nYou must send $',totalPay,' to the other person. They must send you money as well (it may be a different amount).')

        elif gameOne > 0 and gameTwo == 0:
             totalPay = (gameOne - ownMoney) / 2
             print('\nYou must send $',totalPay,' to the other person. They must send you money as well (it may be a different amount).')
        
        elif gameOne > 0 and gameTwo > 0:
             otherPersonsMoney = int(input('How much of their own money did your betting partner put in? $'))

             totalPay = (((gameOne + gameTwo) - (ownMoney + otherPersonsMoney)) /2) + otherPersonsMoney
             print('\nYou must send $',totalPay,' to the other person. They will not send you any (you won both games).')
             profit = totalPay-otherPersonsMoney
             print('\nYou made $',profit,' PROFIT')


        mode = exit
        









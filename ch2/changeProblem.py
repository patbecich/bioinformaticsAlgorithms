
# Provide a method for determining the lowest number of coins
# (quarters,dimes,nickels,and pennies) needed for a cashier to make change.


# def makeChange():
#     price = input('Enter price:')
#     cash = input('Enter cash:')
#     print(price)
#     print(cash)


# makeChange()


def makeChange():
    price = 46.45
    cash = 50.00
    change = cash - price
    dollars = 0
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    while (change >= 0.01):
        change = round(change, 2)
        print('remaining change ' + str(change))
        if change >= 1.00:
            dollars += 1
            change -= 1.00
        elif change >= .25:
            quarters += 1
            change -= .25
        elif change >= .10:
            dimes += 1
            change -= .10
        elif change >= .05:
            nickles += 1
            change -= .05
        elif change >= .01:
            pennies += 1
            change -= .01
    print('Optimal change for $' + str(round((cash - price), 2)) + ': ')
    print('Dollars: ' + str(dollars))
    print('Quarters: ' + str(quarters))
    print('Dimes: ' + str(dimes))
    print('Nickles: ' + str(nickles))
    print('Pennies: ' + str(pennies))
      



#makeChange()
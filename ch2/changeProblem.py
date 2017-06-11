
# Provide a method for determining the lowest number of coins
# (quarters,dimes,nickels,and pennies) needed for a cashier to make change.


# def makeChange():
#     price = input('Enter price:')
#     cash = input('Enter cash:')
#     print(price)
#     print(cash)


# makeChange()

from itertools import combinations

def testCombo():
    for combo in combinations(usCurrency, 2):
        print(combo)

    
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
        if change >= 1.00:      # 
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

# makeChange()

# generalize this example to accomodate different denominations

# currency in cents


usCurrency = [25, 10, 5, 1]
euCurrency = [20, 10, 5, 2, 1]


def betterChange(price, cash, denomList):
    remainder = cash - price
    specificCounts = []
    for k in range(0, len(denomList)):
        specificCounts.append(0)
        specificCounts[k] += int(remainder/denomList[k])
        remainder -= specificCounts[k]*denomList[k]
    # clearly print the count of each denomination used
    for d in range(0, len(specificCounts)):
        print(str(denomList[d]) + "'s: " + str(specificCounts[d]))


# betterChange does not always guarantee the smallest number of coins
# we can address this with a brute force method that compares different solutions


def BruteForceChange(price, cash, denomList):
    remainder = cash - price
    smallestCoinCount = float('inf')
    limitList = []
    specificCounts = []
    for i in denomList:
        specificCounts.append(0)
        limitList.append(0)
        limitList[i] = int(remainder/denomList[i] + 1)
    print(limitList)
    for i in denomList:
        for j in range(0, int(remainder/denomList[i] + 1)):
            specificCounts[i] = j
            print(specificCounts)
 
def loopTest(digits):
    for i in range(0, digits):
        return(str(i))


# https://stackoverflow.com/questions/1208118/using-numpy-to-build-an-array-of-all-combinations-of-two-arrays
import numpy
a = numpy.array([1,2,3])
b = numpy.array([5,9])
c = numpy.array([10,11,12])
abc = [a,b,c]
# combos = numpy.stack(numpy.meshgrid(*abc))

# def cartesian(*arrays):
#     mesh = numpy.meshgrid(*arrays)  # standard numpy meshgrid
#     dim = len(mesh)  # number of dimensions
#     elements = mesh[0].size  # number of elements, any index will do
#     flat = numpy.concatenate(mesh).ravel()  # flatten the whole meshgrid
#     reshape = numpy.reshape(flat, (dim, elements)).T  # reshape and transpose
#     return reshape

# combos = cartesian(abc)

# https://stackoverflow.com/questions/29714771/combinatoric-cartesian-product-of-numpy-arrays-without-iterators-and-or-loops

from sklearn.utils.extmath import cartesian

combos = cartesian(abc)

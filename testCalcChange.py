import math

def testCalcChange():
    dollars = quarters = dimes = nickels = pennies = 0
    userInput = eval(input("Enter amount in dollars:  "))
    # multiply user input by 100 to get a whole number representing total amount of cents
    userInput *= 100
    # find out how many whole dollars we have then subtract that many dollarts from user input
    dollars = math.floor(userInput/100)
    userInput %= 100
    # find out how many quarters we have then subtract that many dollarts from user input
    quarters = math.floor(userInput/25)
    userInput %= 25
    # find out how many dimes we have then subtract that many dollarts from user input
    dimes = math.floor(userInput / 10)
    userInput %= 10
    # find out how many nickles we have then subtract that many dollarts from user input
    nickles = math.floor(userInput / 5)
    userInput %= 5
    # pennies are whatever is remaining
    pennies = math.floor(userInput)
    print(dollars)
    print(quarters)
    print(dimes)
    print(nickles)
    print(pennies)

def main():
    testCalcChange()

main()
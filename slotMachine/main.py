########## read the comments that have a single# in front of them first then go through the program then read the comments with the ##

#  so we're actually going to build a text based slot machine.
# Now, the way this will work is the user will deposit a certain amount of money. We're then going to allow them to bet on either one,
# two or three lines of the slot machine, just to keep it pretty simple. I know in real slot machines they have a lot more lines than that
# and then we are going to determine if they won. So if they got any lines, we're going to multiply their bet by the value of the line,
# add that to their balance, and then allow them to keep playing until they want to cash out or until they run out of money. So
# this is actually a fairly complex project because we need to do a lot of things.

# We need to collect the users deposit, we need to add that to their balance.
# We need to allow them to bet on a line or on multiple lines. We then need to see if they actually got any of those lines.
# We then need to spin the slot machine. We need to generate the different items that are going to be in the slot machine
# on the different reels, and then we need to add whatever they won back to their balance.


# the place where we will start is by collecting user input
# and for this we neeed to get the deposit the user is entering and the bet
# those are the 2 things that we need before we start using the slot machine

import random  # because we need to generate the slot machine values kind of randomly, right?


## Well, the first thing we need to figure out is how many items we want to have in each reel and how long we want the lines to be.
## Now, slot machines can get a bit complicated in terms of how the lines work. I'm going to keep this really simple,
## and we're going to imagine that we have a three by three slot machine and that you only get a line if you get three in a row.
## Okay, we had three in a row, then you win. This might not be the most balanced slot machine. It might not be one you want to play on, but for this project is fine.


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

## All right. Now, what we need to specify is how many symbols are in each of our reels.
## Now, it should be the same, at least from what I know. It should be the same number of symbols in every single reel.
## We're not doing anything really complicated. When I say real, I'm talking about kind of one column, right? So how many symbols are in that column?
## Because we're going to have to randomly select out of those symbols, and then we need values for our different symbols.
## So we need to pick kind of first of all, how many symbols do we want to have in total and what do we want those symbols to be now
## to keep this easy, we can do something just like, you know, ABCD. I think those are probably fine as the symbols.

symbolCount = {"A": 2, "B": 4, "C": 6, "D": 8}

## now we need something that will generate what the outcome of the slot machine is using the values of symbolCount and ROWS and COLS
## what we need to do is generate what symbols are going to be in each column
## based on the frequency of symbols that we have here. So we essentially need to randomly pick the number
## of rows inside of each column. So if we have three rows, need to pick three symbols
## that go inside of each of the columns that we have. And for each column we're doing kind of a new random pick, right? Or new random generation of the symbols.
def getSlotMachineSpin(rows, cols, symbols):
    # Now, the easiest way to randomly select
    # values here for each of our columns is going to be to create a list that contains all of the different values we possibly could select from.
    # And then to randomly choose three of those values and when we choose a value, will remove it from the list, and then we'll choose again.
    allSymbols = []

    # So what's going to happen here is I'm going to loop through this dictionary. Let's imagine I'm on the first key value pair.
    #  My symbol is going to be "A" and my symbol count is going to be two.
    # All right. So then I have another for loop inside of here where I'm looping through the symbol count.
    # So the symbol count is two, and what I'm doing is doing this two times. So I'm going to add this symbol twice into my all symbols list.
    for (
        symbol,
        symbolCount,
    ) in (
        symbol.items()
    ):  # .items will give us both the key and value associated with a dictionary
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    # not that we have the allSymbols list now we have to decide what values go inside each of COLS

    columns = [[], [], []]


# this function is gonna be responsible for collecting user input
# that gets the deposit from user
def deposit():
    #  we are continously gonna ask the user to provide a valid amount
    # so if they don't give a valid amount then we are gonna keep asking the user for avalid amount
    while True:
        amount = input("What would you like to deposit? $")
        # now we will need to check if the amount entered is a number
        # isdigit will help us get a valid number i.e. if they enter 1000 or 100 then
        #  isdigit will help with that if they provide a negative number then this if condition won't be true
        # we can use isdigit on a string to check if the amount is a valid number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


#  this is where we ask on how many lines they want to bet on
def getNumberOfLines():
    # here we will ask them to bet on lines from 1 to 3 because we have defined a global const which says MAX_LINES = 3
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines


#  this function will give us the amount to bet on each line
def getBetOnEachLine():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit:
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount


# if we want to rerun the program like if you want to pay again then we just run the main function
def main():
    balance = deposit()
    lines = getNumberOfLines()
    # we need to check if the amount that they are betting is less than or equal to their balance
    while True:
        getBet = getBetOnEachLine()
        totalBet = getBet * lines
        if totalBet > balance:
            print(
                f"you donot have enough to bet that amount, Your currenct balance is ${balance}."
            )
        else:
            break
    print(f"You are betting ${getBet} on {lines}. Total bet is equal to: ${totalBet} ")


main()

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

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
    getBet = getBetOnEachLine()
    totalBet = getBet * lines
    print(f"You are betting ${getBet} on {lines}. Total bet is equal to: ${totalBet} ")


main()

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
    num = input("Enter a number: ")  # here we take the input from the user
    if num == "done":
        break  # since we see that num is done so we break and exit the loop from here
    try:
        inputNum = int(num)  # here we convert the input from a string to an integer
        # print("the number is", inputNum)
    except:
        print("Invalid input")
        continue

    # here we assign the smallest and largest value to the incoming input straight away because we saw in the lectures
    # that can later check whether the smallest value that we assigned is truly the smallest and the largest value that we assigned is truly the largest
    if smallest is None and largest is None:
        smallest = inputNum
        largest = inputNum

    # here we check if the next incoming number from the user is lesser than the number already there in the smallest variable if yes then
    # we tell python hey we found a number that is smaller than the value that is present in smallest varaiable so take this new value and assign it to the smallest variable
    elif inputNum < smallest:
        smallest = inputNum

    # here we check if the next incoming number from the user is larger than the number already there in the largest variable if yes then
    # we tell python hey we found a number that is larger than the value that is present in largest varaiable so take this new value and assign it to the largest variable
    elif inputNum > largest:
        largest = inputNum

# here we just print out the largest and smallest variables
print("Maximum is", largest)
print("Minimum is", smallest)

##### smallest number of a list
# numList = [9, 41, 12, 3, 74, 15]
# smallestNumSoFar = numList[4]
# print("Before", smallestNumSoFar)
# for num in numList:
#     if smallestNumSoFar > num:
#         smallestNumSoFar = num
#     print(smallestNumSoFar, num)
# print("After", smallestNumSoFar)

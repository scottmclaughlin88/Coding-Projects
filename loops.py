"""loops.py: Displays and tests the different iteration concepts."""

#####################
##     Range       ##
#####################
def printNums(stop):
    for x in range(stop):
        print(x)

def printNumsMore(stop, start):
    for x in range(start,stop):
        print(x)

def printNumsEvenMore(stop,start,step):
    for x in range(start,stop,step):
        print(x)

def printNumsAll(stop,start=0,step=1):
    for x in range(start,stop,step):
        print(x)

# printNums(5)
# printNumsMore(10,5)#refer to line 10
# printNumsEvenMore(10,0,2) #start, stop, step
# printNumsAll(5)
# printNumsAll(10,5)
# printNumsAll(10,0,2)
# printNumsAll(19,step=-1,start=30)#step -1 decreases the amount.

#####################
##     List        ##
#####################
def printItems(items):
    for item in items:
        print(item)

def printItemsByIndex(items):
    for index in range(len(items)): #
        print(index,":",items[index])

items = ['chocolate','rice krispie','reeses cup']
# printItems(items)
# printItemsByIndex(items)

#####################
##    Break        ##
#####################
def printUntil(list,stopItem):
    for item in list:
        if item == stopItem:
            break #looking for something until you reach it, then stop.
        print(item)

def printWhileValid(list,allowedItems):
    for item in list:
        if item not in allowedItems:
            break
        print(item)

def whileTrue(startValue,stopValue):
    while True:
        if startValue > stopValue:
            break  #used in while loops as well
        startValue+=1
        print('Value is now', startValue)
        
items = ['chocolate','rice krispie','reeses cup']
allowedItems = ['chocolate','rice krispie']
stopItem = 'rice krispie'
# printUntil(items,stopItem)
# printWhileValid(items,allowedItems)
# whileTrue(5,10)

#####################
##   Continue      ##
#####################

#continue is used to skip to the next item in the list
def skipItems(allItems,badItems):
    for item in allItems:
        if item in badItems:
            continue
        print(item)

def skipIndices(allItems, badIndices):
    for x in range(len(allItems)):
        if x in badIndices:
            continue
        print(allItems[x])

def printLowerCase(items):
    for item in items:
        if item.islower():
            continue
        print(item)

items = ['chocolate','rice krispie','BaNaNa']
baditems = ['chocolate','rice krispie']
# skipItems(items,baditems)
# skipIndices(items,[0,2])
# printLowerCase(items)

#####################
##    While        ##
#####################
def askUserUntil(requiredInput):
    userInput = ''
    while userInput != requiredInput: #!= is not equal to.  opposite of ==
        userInput = input(f'Please enter {requiredInput}: ')
    print(f'Thank you for entering {requiredInput}')

def printUntilReaching(value):
    current = 0
    while current < value:
        print("Not there yet..")
        current+=1
    print("We made it!")

def printUntilReachingBad(items,stopIndex):
    currentIndex = 0
    while currentIndex < stopIndex and currentIndex < len(items):
        print(items[currentIndex])
        currentIndex+=1

# askUserUntil('bob')
# printUntilReaching(50)
# items = ['chocolate','rice krispie','BaNaNa']
# printUntilReachingBad(items,1) #only takes in the number of variables in the function.

#####################
##   Recursion     ##
##################### 
def printUntilZero(num):
    if num <= 0:
        pass #do nothing
    else:
        printUntilZero(num-1)
    print(num)

def fib(num):
    if num == 0 or num == 1:
        return 1
    return fib(num-1) + fib(num-2)

# # printUntilZero(5)
# print(fib(3),fib(4),fib(5))

####################
##     Tasks      ##
####################

# Task #1  
# Write a function that prints out all even numbers between a given start and stop point
# Write a function that prints out all odd numbers below a stop point
# Write a function that prints out all multiples of 5 below a stop point
# def numbers(start,stop):
#     for x in range(start,stop,2):
#         print(x)
# # numbers(2,20) #answer 1

# def oddNumbers(stop):
#     for x in range(1,stop+1,2):
#         print(x)
# # oddNumbers(9)#answers 2

# def multipleNubers(stop):
#     for x in range(5,stop+1,5):
#         print(x)
# multipleNubers(25)

# Task #2  
# Write a function that prints out each item in a list twice in its own line
# Write a function that prints out each item in a list with its index before and after it
def print_list(num_list):
    for num in num_list:
        print(num,num)
num_list = [10,20,30,40]
# print_list(num_list) #answer 1

def print_list(num_list):
    for num in range(len(num_list)):
        print(num,num_list[num],num)
num_list = [10,20,30,40]
# print_list(num_list)

# Task #3
# Write a function that will take in two lists of items and a string (allItems, goodItems, stopItem). It will print
# out each item from that list that is also in the gooditems list but will STOP when it reaches the stop item 
def multi_list(allItems,goodItems,stopItem):
    for item in allItems:
        # print(item,'is in',allItems)
        if item in goodItems:
            print(item,'is in',goodItems)
        else:
            print(item,'is not in',goodItems) #else is another way of saying something is not in it.
        # if item == stopItem:
        #     break

allItems = ['spinach','pizza','burger','broccoli','kitkat','cabbage']
goodItems = ['spinach','broccoli','cabbage']
stopItem = 'kitkat'

# multi_list(allItems,goodItems,stopItem) 

# Task #4
# Write a function that will ask the user to pick a number until they pick one that is a multiple of 3 
def input_num(num=3):
    userInput = 1
    while userInput % num != 0: #!= is not equal to.  opposite of ==
        userInput = int(input(f'Please enter a multiple of {num}: '))
    print(f'Thank you for entering a multiple of {num}!')

# input_num(7)
# Task #5
# Write a recursive function that will print out every letter in a string
def print_word(word):
    if len(word) <= 0:
        pass #do nothing
    else:
        print(word[0])
        word=word[1:] #ends after colon if nothing after it
        print_word(word)
# print_word('antarctica')

# times_printed = 0
# while times_printed < 5: #while something is true, keep running it, then stop.
#     print("False")
#     times_printed += 1
# print(".")


# for times_printed in range(5): #adds one iniately.  Simpler way to do while loop.
#     print("False")
# # print('0')

times_printed = 2
while times_printed < 5: #only used when you don't know where your stopping point is going to be.
    print(times_printed)
    times_printed += 2
print('.')

for times_printed in range(2,5,2):
    print(times_printed)
print('.')


# write a function that takes in a list and a number and will print out every item from that list before the number.

def sports(list,num):
    for x in range(min(num,len(list))): #min function takes the minimum of two values
        print(list[x])       
        

list = ['Basketball','Soccer','Rugby','Baseball','Hockey']
num = 3
sports(list,num)

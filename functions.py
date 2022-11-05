"""functions.py: Displays and tests the different common function concepts."""
import time

#####################
##     Void        ##
#####################
# These are functions that have no return type
def printHelloTwice():
    print('Hello')
    print('Hello')

def print0and5():
    x = 0
    print(x, x+5)

def doNothing():
    pass #end a function, end if statement, etc

# printHelloTwice()
# print0and5()
# doNothing()

#####################
##     Return      ##
#####################
# Functions that return some kind of value to be used elsewhere
def getHello():
    return 'Hello'

def getTenSquared():
    return 10**2

def getNothing():
    return None

# value = getHello()
# print(value)
# value = getTenSquared()
# print(value)
# value = getNothing()
# print(value)

#####################
##    Parameters   ##
#####################
# Information passed into the function
def printStringTwice(string):
    print(string, string) 

def addNumbers(num1, num2):
    return num1 + num2

def getItemAtIndex(list,index):
    return list[index]

# printStringTwice('blue')
# printStringTwice("banana")
# value = addNumbers(5,10)
# print(value)
# value = getItemAtIndex([5,6,10],2) 
# print(value)

#####################
##   Optional      ##
#####################
# Optional information that uses a default value if not passed in
def printMessage(string, times=1): #optional parameters allow for default values.
    for x in range(times):
        print(string)

def multiplyNumbers(num1, num2, num3=1):
    return num1 * num2 * num3

def addSpaces(string='default', spaces=1):  #optional parameter is something=something
    output = ""
    for letter in string:
        output += letter + (" " * spaces)
    return output

# printMessage("Racecar")
# printMessage("Vroom", 5)

# value = multiplyNumbers(2,3)
# print(value)
# print(multiplyNumbers(2,3,num3=2))
# print(multiplyNumbers(2,3,2))

# print(addSpaces())
# print(addSpaces("Spacey"))
# print(addSpaces("SuperSpacey",2))

#####################
##    Arbitrary     ##
#####################
def printFirstNameAndAge(**personData): #** could be any number of paramters.
    print(personData['firstName'],'is',personData['age'])

def doDifferentThings(**foodItems):
    for item in foodItems.values():
        print(item)
    if len(foodItems) > 2:
        print("Bit Chonky are we?")
    if len(foodItems) <= 1:
        print("Put some meat on them bones!")

# printFirstNameAndAge(age='15',lastName='Smith',firstName='Josh')
# doDifferentThings(arg1='grape',arg2='watermelon',arg3='steak',arg4='fries')
# doDifferentThings(arg1='salad')

#####################
##   Decorators    ##
##################### 
def addPoundSymbolRows(func): #allow you to call another function inside of them
    def inner(*args,**kwargs): #*arbitary number of arguments.
        print('###############')
        func(*args, **kwargs)
        print('###############')
    return inner

def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner

@addPoundSymbolRows #add these above functions
@calculate_time
def printList(list):
    for item in list:
        print(item)

@calculate_time
def loopTimes(times):
    for x in range(times):
        continue
    pass

# printList(['Pear','Apple','Orange'])
# loopTimes(1000000)
# loopTimes(10000000)

####################
##     Tasks      ##
####################

# Task #1
# Write a function that will combine two strings and return that combination.  
def merge(str1, str2):
    str_merge = str1 + ' ' + str2
    return str_merge
value = merge('the','helper')
# print(value)
# Task #2  
# Augment the previous function to work when provided 0 or 1 strings by supplying default values for the two strings.
def merge_new(str1='mic', str2='sound'): #useful for defaults in many scenarios
    str_merge = str1 + ' ' + str2
    return str_merge
value = merge_new()
# print(value)

# Task #3
# Write a function that takes in a list and a integer in addition to an optional integer.  It will then add
# the integer to that list the optional integer number of times.
# add_num([1,2,3],5,2) = [1,2,3,5,5]
def complexity(list,num,times=1):
    for x in range(times):
        list.append(num)
    return list
print(complexity([4,2,1],100))

# Task #4
# Write a decorator that will put 1 row of # symbols before the function, and two rows of $ signs after the
# function.
def test_Functionator(func): #allow you to call another function inside of them
    def inner(*args,**kwargs): #*arbitary number of arguments.
        print('###############')
        func(*args, **kwargs)
        print('$$$$$\n $$$$$')#\n can exist in a string
    return inner

@test_Functionator
def test_dec():
    print('hello')
test_dec()

# Task #5
# Write a function that takes in a string and a letter and will return the index of the second occurance
# of that letter.
def string_letter(string,letter):
    for index in range(len(string)):
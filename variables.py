"""variables.py: Displays and tests the different common variables."""

from concurrent.futures.process import _python_exit


test = ''
testOptions = ['string', 'int', 'float', 'bool', 'list', 'tuple', 'dict', 'none']

print("Currently Analyzing: ", test,'\n')

#####################
##     Strings     ##
#####################
if test == 'string':
    # Declaring
    x = 'banana'
    print(x, type(x)) #type can be used for, str, int, any kind 'type'

    # Adding 
    x2 = x + 'b'
    print(x2)

    # Other operations
    x2 = x[0]
    print(x2)

    x2 = x.replace('b','t')
    print(x2)

    x2 = x.find('n') #finds index of the first of the substring
    print(x2)


#####################
##     Ints        ##
#####################
if test == 'int':
    # Declaring
    x = 5
    print(x, type(x))

    # Adding
    x2 = x + 5
    print(x2)

    # Other operations
    x2 = x % 3 #odd/even elements (mod).
    print(x2)

    x2 = x**3 #exponent
    print(x2)


#####################
##     Float       ##
#####################
if test == 'float':
    # Declaring
    x = 5.0
    print(x, type(x))

    # Adding
    x2 = x + 5
    print(x2)

    # Other operations
    x2 = x % 3
    print(x2)

    x2 = x/3.1415
    print(x2)
    print(f'as a formatted string with 2 decimal places {x2:.2f}')
    print(f'as a formatted string of a percent {x2:.2%}')
    print(f'as a formatted string of as a currency ${x2:.2f}')


#####################
##     Bool        ##
#####################
if test == 'bool':
    # Declaring
    x = False
    print(x, type(x))

    # As ints
    print('True as int is: ', int(True)) #True = [1], False = [0], circuit is active [1]
    print('False as int is: ', int(False))
    print('1 as a bool is: ', bool(1))

    # Other operations
    print('x equal to True is', x == True)
    print('x equal to False is', x == False)
    print('x not equal to True is', x != True) #!= is not equals


#####################
##     Lists       ##
#####################
# if test == 'list':
#     # Declaring
#     x = ['apple', 'pear', 'kumquat']
#     print(x, type(x))

#     # Adding
#     x.append('banana')
#     print(x)

    # Other Operations
    # print('The item at the 0 position in list is', x[0])

    # print("All items in list on their own lines")
    # for item in x:
    #     print(item)

    # x.sort()
    # print(x)

    # x.sort(reverse=True)
    # print(x)

    # x = [45,32,81,2,45,1]
    # x.sort()
    # print(x)

    # x.remove(45)
    # print(x)

    # x.pop(1)
    # print(x)


#####################
##     Tuples      ##
#####################
if test == 'tuple':
    # Declaring
    x = ('apple', 'pear', 'kumquat') #Tuples are in ()
    print(x, type(x))

    # Adding
    x = x + ('banana',)
    print(x)

    # Other Operations
    print('The item at the 0 position in tuple is', x[0])

    print("All items in tuple on their own lines")
    for item in x:
        print(item)

    print(x.count('banana'))


#####################
##     Dicts       ##
#####################
if test == 'dict':
    # Declaring
    x = {'V':'9.2/10'}
    print(x, type(x))

    # Adding
    x['Matrix'] = '8/10' #use [] to add to list, = to the value 
    print(x)

    # Update existing value
    x.update({'Matrix':'9/10'})
    print(x)

    # Other Operations
    print('The whole dictionary is', x)
    print('The keys are', x.keys())
    print('The values are', x.values())
    print('The rating of "Matrix" is ', x['Matrix'])
    print(sorted(x.items()))
    
#####################
##     None       ##
#####################
if test == 'none':
    # Declaring
    x = None
    print(x, type(x))

    if x == None:
        print("It has no value")
    


####################
##     Tasks      ##
####################

# Task #1  
#   Combine the word banana with phone and print it out
#   Print out the 7th letter of this combined string
#   Finally replace all of the letters 'a' with '$'

# word = "banana"
# word2 = word + "phone"
# print(word2[6])
# word2 = word.replace('a','$')
# print(word2)

# Task #2  
#   Print out the sum of 15 and 34.2131 with 2 decimal places
#   Find what percent 20 is of 205 and print it out as a percent
#   Print out the remainder when dividing 10 by 3
x = 15 + 34.2131
print(f'{x:.2f}') #string and variable you give inside it
x = 20 / 205
print(x)
print(f'{x:.1%}') #f strings change rules a bit
x2 = 10 % 3 #mods divide then give you change.
print(x2)

# Task #3
#   Print out a statement that evaluates to true  
#   Print out a statement that evaluates to false  
#   Change 1 into False through type conversions (and subtraction) and print it out
print(5 == 5)
print(1234123 == 1234123)
print(1234123 == 120548701850123570)
x = 1
print('1 as a bool is: ', bool(x-1))


# Task #4
#   Print out a list of 5 elements, add an element then print it again
#   Print out the list with each element on its own line
#   Sort the list and print it out again
#   Print out the third item in the list
#   Remove the first item from the list and print out the list
list = ['green','blue','yellow','dark green','purple']
print(list)
list.append('violet')
print(list) #answer #1

for colors in list:
    print(colors) #answer #2

list.sort()
print(list) #answer #3

print(list[2]) #answer #4

list.pop(0) #pop removes at index
print(list) #answer #5

# Task #5
#   Create a dictionary storing client records where the keys are names and the values are amount spent
#   e.g {Bob Dylan: 15.43}
#   Add three entries to the dictionary and print it
#   Modify one of the entries and print it out again
#   Print out the amount spent for one of the entries
#   Print out all of the keys (names) stores in the dictionary

songs_dict = {'Bob Dylan': '50.10'}
songs_dict.update({'Skillet':'60.15','Santana':'40.1','Random Band':'29.30'})
print(songs_dict)#answer #1
songs_dict['Skillet'] = '40.10'
print(songs_dict) #answer #2
print("I spent " + songs_dict['Skillet']) #stuck here on answer #3
for key in songs_dict.keys(): #answer #4, had to do a stackoverflow search.
    print(key)

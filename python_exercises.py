# # #credit to https://pynative.com/python-dictionary-exercise-with-solutions/

#loops
#per http://lovelace.augustana.edu/q2a/index.php/4345/whats-the-difference-between-if-elif-and-else
#if is always first in loop to check if the statement is true.
#next it goes to elif or else if the statement is false.


# # #Convert two lists into a dictionary
# # #Below are the two lists.
# # #Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# # keys = ['Ten', 'Twenty', 'Thirty']
# # values = [10, 20, 30]

# # res_dict = dict(zip(keys, values))
# # print(res_dict)

# # # write a function that takes in a list and a number and will print out every item from that list before the number.

# # # def sports(list,num): 
# #     # index = 0
# #     # while index < num:
# #     #     print(list[index])
# #     #     index += 1

# # # def sports_for(list,num):
# # #     for x in range(num):  #range excludes the last element
# # #         print(list[x])
# # def sports_for(list,num):
# #     times_printed = 0
# #     for item in list:
# #         if times_printed >= num:
# #             break
# #         print(item)
# #         times_printed += 1

# # list = ['Basketball','Soccer','Rugby','Baseball','Hockey']
# # num = 2


# # sports_for(list,num) #stuck on lines 8-11

# #credit to https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# i = 1
# while i <= 10:
#     print(i)
#     i += 2



# #1 Change the function above to work with a while loop




# #2 Change the fucntion above to work with a for loop, without using the range method.

# """loops.py: Displays and tests the different iteration concepts."""

# #####################
# ##     Range       ##
# #####################
# # def printNums(stop):
# #     for x in range(stop):
# #         print(x)

# # def printNumsMore(stop, start):
# #     for x in range(start,stop):
# #         print(x)

# # def printNumsEvenMore(stop,start,step):
# #     for x in range(start,stop,step):
# #         print(x)

# # def printNumsAll(stop,start=0,step=1):
# #     for x in range(start,stop,step):
# #         print(x)

# # printNums(5)
# # printNumsMore(10,5)#refer to line 10
# # printNumsEvenMore(10,0,2) #start, stop, step
# # printNumsAll(5)
# # printNumsAll(10,5)
# # printNumsAll(10,0,2)
# # printNumsAll(19,step=-1,start=30)#step -1 decreases the amount.

# #####################
# ##     List        ##
# #####################
# def printItems(items):
#     for item in items:
#         print(item)

# def printItemsByIndex(items):
#     for index in range(len(items)): #
#         print(index,":",items[index])

# items = ['chocolate','rice krispie','reeses cup']
# # printItems(items)
# # printItemsByIndex(items)

# #####################
# ##    Break        ##
# #####################
# def printUntil(list,stopItem):
#     for item in list:
#         if item == stopItem:
#             break #looking for something until you reach it, then stop.
#         print(item)

# def printWhileValid(list,allowedItems):
#     for item in list:
#         if item not in allowedItems:
#             break
#         print(item)

# def whileTrue(startValue,stopValue):
#     while True:
#         if startValue > stopValue:
#             break  #used in while loops as well
#         startValue+=1
#         print('Value is now', startValue)
        
# items = ['chocolate','rice krispie','reeses cup']
# allowedItems = ['chocolate','rice krispie']
# stopItem = 'rice krispie'
# # printUntil(items,stopItem)
# # printWhileValid(items,allowedItems)
# # whileTrue(5,10)

# #####################
# ##   Continue      ##
# #####################

# #continue is used to skip to the next item in the list
# def skipItems(allItems,badItems):
#     for item in allItems:
#         if item in badItems:
#             continue
#         print(item)

# def skipIndices(allItems, badIndices):
#     for x in range(len(allItems)):
#         if x in badIndices:
#             continue
#         print(allItems[x])

# def printLowerCase(items):
#     for item in items:
#         if item.islower():
#             continue
#         print(item)

# items = ['chocolate','rice krispie','BaNaNa']
# baditems = ['chocolate','rice krispie']
# # skipItems(items,baditems)
# # skipIndices(items,[0,2])
# # printLowerCase(items)

# #####################
# ##    While        ##
# #####################
# # def askUserUntil(requiredInput):
# #     userInput = ''
# #     while userInput != requiredInput: #!= is not equal to.  opposite of ==
# #         userInput = input(f'Please enter {requiredInput}: ')
# #     print(f'Thank you for entering {requiredInput}')

# # def printUntilReaching(value):
# #     current = 0
# #     while current < value:
# #         print("Not there yet..")
# #         current+=1
# #     print("We made it!")

# # def printUntilReachingBad(items,stopIndex):
# #     currentIndex = 0
# #     while currentIndex < stopIndex and currentIndex < len(items):
# #         print(items[currentIndex])
# #         currentIndex+=1

# # askUserUntil('bob')
# # printUntilReaching(50)
# # items = ['chocolate','rice krispie','BaNaNa']
# # printUntilReachingBad(items,1) #only takes in the number of variables in the function.

# #####################
# ##   Recursion     ##
# ##################### 
# def printUntilZero(num):
#     if num <= 0:
#         pass #do nothing
#     else:
#         printUntilZero(num-1)
#     print(num)

# def fib(num):
#     if num == 0 or num == 1:
#         return 1
#     return fib(num-1) + fib(num-2)

# # # printUntilZero(5)
# # print(fib(3),fib(4),fib(5))

# ####################
# ##     Tasks      ##
# ####################

# # Task #1  
# # Write a function that prints out all even numbers between a given start and stop point
# # Write a function that prints out all odd numbers below a stop point
# # Write a function that prints out all multiples of 5 below a stop point
# # def numbers(start,stop):
# #     for x in range(start,stop,2):
# #         print(x)
# # # numbers(2,20) #answer 1

# # def oddNumbers(stop):
# #     for x in range(1,stop+1,2):
# #         print(x)
# # # oddNumbers(9)#answers 2

# # def multipleNubers(stop):
# #     for x in range(5,stop+1,5):
# #         print(x)
# # multipleNubers(25)

# # Task #2  
# # Write a function that prints out each item in a list twice in its own line
# # Write a function that prints out each item in a list with its index before and after it
# def print_list(num_list):
#     for num in num_list:
#         print(num,num)
# num_list = [10,20,30,40]
# # print_list(num_list) #answer 1

# def print_list(num_list):
#     for num in range(len(num_list)):
#         print(num,num_list[num],num)
# num_list = [10,20,30,40]
# # print_list(num_list)

# # Task #3
# # Write a function that will take in two lists of items and a string (allItems, goodItems, stopItem). It will print
# # out each item from that list that is also in the gooditems list but will STOP when it reaches the stop item 
# def multi_list(allItems,goodItems,stopItem):
#     for item in allItems:
#         # print(item,'is in',allItems)
#         if item in goodItems:
#             print(item,'is in',goodItems)
#         else:
#             print(item,'is not in',goodItems) #else is another way of saying something is not in it.
#         # if item == stopItem:
#         #     break

# allItems = ['spinach','pizza','burger','broccoli','kitkat','cabbage']
# goodItems = ['spinach','broccoli','cabbage']
# stopItem = 'kitkat'

# # multi_list(allItems,goodItems,stopItem) 

# # Task #4
# # Write a function that will ask the user to pick a number until they pick one that is a multiple of 3 
# def input_num(num=3):
#     userInput = 1
#     while userInput % num != 0: #!= is not equal to.  opposite of ==
#         userInput = int(input(f'Please enter a multiple of {num}: '))
#     print(f'Thank you for entering a multiple of {num}!')

# # input_num(7)
# # Task #5
# # Write a recursive function that will print out every letter in a string
# def print_word(word):
#     if len(word) <= 0:
#         pass #do nothing
#     else:
#         print(word[0])
#         word=word[1:] #ends after colon if nothing after it
#         print_word(word)
# # print_word('antarctica')

# # times_printed = 0
# # while times_printed < 5: #while something is true, keep running it, then stop.
# #     print("False")
# #     times_printed += 1
# # print(".")


# # for times_printed in range(5): #adds one iniately.  Simpler way to do while loop.
# #     print("False")
# # # print('0')

# times_printed = 2
# while times_printed < 5: #only used when you don't know where your stopping point is going to be.
#     print(times_printed)
#     times_printed += 2
# print('.')

# for times_printed in range(2,5,2):
#     print(times_printed)
# print('.')


# # write a function that takes in a list and a number and will print out every item from that list before the number.

# def sports(list,num):
#     for x in range(min(num,len(list))): #min function takes the minimum of two values
#         print(list[x])       
        

# list = ['Basketball','Soccer','Rugby','Baseball','Hockey']
# num = 3
# sports(list,num)

# #1write a function that prints out the list backwards.

# def reverse_list(list):
#     #length list -1 (first element), change index by -1 each time it executes
#     for index in range(len(list)-1,-1,-1):
#         print(list[index])

           



# # list = ['Apple','Banana','Orange']
# # reverse_list(list)



# #2 write a function that prints out every 3rd item in the list
# def skip_items_list(list):
#     #length list -1 (first element), change index by -1 each time it executes
#     for index in range(0,len(list),3):
#         print(list[index])

# #---------------------Practice list excercises
# #---------------------Courtesy https://pynative.com/python-list-exercise-with-solutions/#h-exercise-1-reverse-a-list-in-python
# #---------------------
# #---------------------

# # list1 = ['M', 'n', 'P', 'Pa']
# # list2 = ['Ten', 'tanthou', 'oop']
# # list3 = [i + j for i, j in zip(list1, list2)]
# # print(list3)

# # nums = [2, 4, 5, 10]
# # results = []
# # for i in nums:
# #         results.append(i * i)
# # print(results)

# # list = ['Apple','Banana','Orange',1,2,3,5,6]
# # # skip_items_list(list)

# #Concatenate two lists in the following order
# # list1 = ['Lets', 'try this!']
# # list2 = ['Yes', 'SIR!']
# # list3 = list1 + list2
# # print(list3)

# #Say you have two lists.  Iterate on both lists simultaneously.  Display items from
# #list1 in original order, while doing list2 in reverse order.

# # list1 = [10, 30, 40, 50, 60]
# # list2 = [1000, 2000, 3000, 4000, 5000]
# # for l1, l2 in zip(list1, list2[::-1]):
# #     print(l1, l2)

# #Remove empty strings from the list of strings.
# # list1 = ['Scott', '', 'Kelly', 'Roger', '']
# # result = list(filter(None, list1))
# # print(result)

# #Write a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000, 7001], 500], 30, 40]
# list1[2][2].append(7000)
# # print(list1)


# #3 write a fucntion that prints out the first and last item in the list.
# def first_last_item(list):
#     # print(list[0])
#     # print(list[len(list)-1])

# # list = ['Apple','Banana','Orange',1,2,3,5,6]
# # first_last_item(list)
# #4 write a function that only prints out items in the list that start with the letter b.
# # def specific_letters(list):
# #     #naturally the 3rd element in range is a 1
# #     for index in range(0,len(list)): 
# #         letters = str(list[index])
# #         f_letter = letters[0]
# #         if f_letter == 'b' or f_letter == 'B':
# #             print(letters)

# # specific_letters(list)

# # # make the pieces for a battleship.

# # #grab out the key from the dictionary, for efficiency
# # ships = {'cruiser': 3,'submarine': 2} 
# # #[] are used to access element(s) in a collection.
# # ships['battleship'] = 4

# # print(ships)
# # ships['battleship'] = 5
# # print(ships)
# # print('length of', 'cruiser', ships['cruiser'])

# # #doing for loops within a dictionary allows for the key,value pair, instead of one item
# # # for name,length in ships.items():
# #     # print(name,length)

# # ships_list = ['cruiser','submarine']
# # print(ships_list[1])
# # #values out of a dictionary, use the key from the value pair []
# # print(ships['battleship'])

# #write a function that will take in a list of ships, and a list of sizes, and will create a dictionary where the ships are the keys
# #and the sizes are the values
# ships_list = ['cruiser','submarine','sailboat','row boat','USS Fake Battleship']
# sizes_list = [4,3,2,1,100]
# def create_boat_dictionary(ships_list,sizes_list):
#     boat_dict = {}
# #the loop through every ship using x as in the index in the list
#     for x in range(len(ships_list)):
#         boat_dict[ships_list[x]] = sizes_list[x]
#     return boat_dict
# boats = create_boat_dictionary(ships_list,sizes_list)
# # print(boats['submarine'])

# #[] can be used to grab thigns from dicts, lists, strings - anything you need to grab a particular element from.
# # ship = 'USS Fake Battleship'
# # print(ship[4])

# # nums = [1,-4,100,50,70]
# # print(nums)
# # #reverse the list using sort method
# # nums.sort(reverse=True)
# # print(nums)
# def ships_sort(ship):
#     return len(ship)
# # print(ships_list)
# ships_list.sort()
# # print(ships_list)
# ships_list.sort(key = ships_sort)
# # print(ships_list)

# #Classes exercices
# """classes.py: Displays and tests the different class concepts."""

# #####################
# ##  What is Self?  ##
# #####################
# from turtle import window_width


# class Printer1():
#     def __init__(self) -> None: #fancy comment
#         self.message = "test"

# p = Printer1() #calls init function when () is used
# # print(p.message)

# #####################
# ## Init Parameters ##
# #####################
# # class Printer2():
# #     def __init__(self, message) -> None:
# #         self.message = message

# # p = Printer2("Break me of a piece of that Fancy Feast") #creating an instance of 'the class'
# # p2 = Printer2("This is a robotic message") #creating an instance of 'the class'
# # print(p.message)
# # print(p2.message)

# #####################
# ##   Functions     ##
# #####################
# # class Printer3():
# #     def __init__(self, message,times=1) -> None:
# #         self.message = message
# #         self.times = times
    
# #     def showMessage(self): #self is the instance
# #         for x in range(self.times):
# #             print(self.message)

# # p = Printer3("Knock Knock",3)
# # p.showMessage()

# #####################
# ##   Overriding    ##
# #####################
# # Commonly overloaded functions include:
# #   str,repr,lt,le,gt,ge,eq,ne and of course init

# # class Person():
# #     def __init__(self, name, color, age=10) -> None:
# #         self.name = name
# #         self.color = color
# #         self.age = age

# #     def __str__(self):
# #         return f"My name is: {self.name} and {self.color} is the best.  You should know that I am {self.age}."

# #     def __eq__(self,other):
# #         if self.name == other.name:
# #             if self.color == other.color:
# #                 return True
# #         return False

# #     def __ge__(self,other):
# #         return self.age >= other.age


# # p1 = Person("Bob", "Blue")
# # p2 = Person("Frank","Green",20)
# # p3 = Person("Bob", "Blue")

# # print(p1)
# # print(p2)
# # print(p1 == p3)
# # print(p2 >= p1)

# #####################
# ##  Inheritance    ##
# #####################
# # class Student(Person):
# #     def __init__(self,name,color,age=10,major="Comp Sci"):
# #         super().__init__(name,color,age) #super run the version of the function in the base class (universal Python info)
# #         self.major = major

# #     def __str__(self):
# #         return super().__str__() + " and I'm majoring in " + self.major

# # class Professor(Person):
# #     def __init__(self,name,color,age=10,courses=[]):
# #         super().__init__(name,color,age)
# #         self.courses = courses

# #     def __str__(self):
# #         return super().__str__() + " and I teach " + str(self.courses)

# # s1 = Student("Dylan", "red",19,"History")
# # # print(s1)
# # p1 = Professor("Professor Mittens","white", 4, ["Wet Food Analysis, Box Structures, Cat Nip Agriculture"])
# # # print(p1)

# #####################
# ##  Private Vars   ##
# ##################### 
# # class Car():
# #     def __init__(self,color) -> None:
# #         self.__color = color  #__ private variables - can only be modified inside the class itself.  Keep things safe.
# #         self.__gear = "third" 

# #     def changeGear(self,newGear):
# #         self.__gear = newGear

# #     def __str__(self):
# #         return f'The car is {self.__color} and is currently in {self.__gear} gear'

# # c1 = Car("Blue")
# # # print(c1)
# # # # c1.__gear = "second"
# # # c1.changeGear("second")
# # # print(c1)

# # ####################
# # ##   Class Attr   ##
# # ####################
# # # Also called static in many languages

# # class Animal():
# #     noise = "I dont make a noise"

# #     def __init__(self,name) -> None:
# #         self.__name = name

# #     def makeNoise(self):
# #         print(f'My name is {self.__name} and I like to go {type(self).noise}')

# #     def __str__(self):
# #         return f'My name is {self.__name}'

# # class Dog(Animal):
# #     noise = "Woof"
    
# #     def __init__(self,name,breed="Golden") -> None:
# #         super().__init__(name) #the super function gives access to methods and properties of a parent or child class.
# #         self.breed = breed

# #     def __str__(self):
# #         return super().__str__() + f' and I am a {self.breed} breed'

# # class Cat(Animal):
# #     noise = "Meow"
    
# #     def __init__(self,name,breed="Siamese") -> None:
# #         super().__init__(name)
# #         self.breed = breed

# #     def __str__(self):
# #         return super().__str__() + f' and I am a {self.breed} breed'

# # animals = [Dog("Rover","Daschund"),Cat("Sammy"),Dog("Spike","Pit"),Cat("Garfield","fat")]
# # for animal in animals:
# #     print(animal)
# # print('\n\n')
# # for animal in animals:
# #     animal.makeNoise() #white method means it doesn't recognize the method (could be editor, or doesn't exist)


# ####################
# ##     Tasks      ##
# ####################
# # Task #1  
# # Write a class that stores a number and create a method that prints that number
# # class Number():
# #     def __init__(self,math):
# #         self.math=math
    
# #     def __str__(self):
# #         return f'The number is {self.math}'

# # n = Number(1)
# # print(n) #answer


# # Task #2  
# # Write a class called triangle that stores two numbers, base and height and has a method
# # that returns the area of the triangle
# # class Triangle():
# #     def __init__(self,base,height):
# #         self.base = base
# #         self.height = height

# #     def getarea(self):
# #         return self.base * self.height * 0.5

# # x = Triangle(10,50)
# # print(x.getarea())

# # Task #3
# # Write a class called rectangle that stores two numbers, width and length, and has a method
# # that draws the rectangle using the given character
# # class Rectangle():
# #     def __init__(self,width,length):
# #         self.width = width
# #         self.length = length

# #     def draw(self,char):
# #         for x in range(self.length):
# #             print(char*self.width)
    


# # This code should draw it after writing your class
# # r = Rectangle(3,6)
# # r.draw('$')
# # It should output this
# #   @@@@
# #   @@@@
# #   


# # Task #4
# # Write a class called Video that stores three values: title, rating, lead actor
# # Write a class called Movie that inherits from Video and also has a release year and genre
# # Write a class called TV Show that inherits from Video and has a number of seasons and number of episodes
# # Write a function in each class using __str__ that prints out all of the information in each of the above classes
# # Create an instance of each class to demonstrate their functionality
# # class Video():
# #     def __init__(self,title='The West World',rating=7,lead_actor='Mark Vanburg'):
# #         self.title = title
# #         self.__rating = rating
# #         self.lead_actor = lead_actor
    
# #     def __str__(self):
# #         return(f'The title of this series was {self.title} and it got a rating of {self.__rating} from critics.  {self.lead_actor} is the lead actor.')

# #     def change_rating(self,new_rating):
# #         self.__rating = new_rating

# # p1 = Video('The West', 4, 'Harrison Ford')
# # # print(p1)

# # class Movie(Video):
# #     def __init__(self,title,rating,lead_actor,year=2012,genre='Historical'):
# #         super().__init__(title,rating,lead_actor)
# #         self.year = year
# #         self.genre = genre
        
# #     def __str__(self):
# #         return super().__str__() + f'This show was created in the year {self.year}.  It is in the {self.genre} genre.'

# # print(Movie('Lone Survivor',9.5,'Mark Wahlburg',2013,'Action'))

# # class TvShow(Video):
# #     def __init__(self,title,rating,lead_actor,season=100,episode=10):
# #         super().__init__(title,rating,lead_actor)
# #         self.season = season
# #         self.episode = episode
    
# #     def __str__(self):
# #         return super().__str__() + f'This is currently in season {self.season}, episode {self.episode}'

# # show1 = (TvShow('M.A.S.H', 10, 'Joe Shmoe', 10, 150))
# # print(show1)
# # show1.change_rating(100)
# # print(show1)

#     # def self.__change_rating = change_rating

# # Task #5
# # Add a method to the above classes that allows you to change the rating of any movie or tv show and make the rating variable private
# # so that it can only be changed with that method.


#

list1 = [5, 20, 15, 20, 25, 50, 20]

def remove_value(sample_list, value):
    return [i for i in sample_list if i != value]

resolution = remove_value(list1, 20)
print(resolution)
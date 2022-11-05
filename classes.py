"""classes.py: Displays and tests the different class concepts."""

#####################
##  What is Self?  ##
#####################
from turtle import window_width


class Printer1():
    def __init__(self) -> None: #fancy comment
        self.message = "test"

p = Printer1() #calls init function when () is used
# print(p.message)

#####################
## Init Parameters ##
#####################
class Printer2():
    def __init__(self, message) -> None:
        self.message = message

p = Printer2("Break me of a piece of that Fancy Feast") #creating an instance of 'the class'
p2 = Printer2("This is a robotic message") #creating an instance of 'the class'
# print(p.message)
# print(p2.message)

#####################
##   Functions     ##
#####################
class Printer3():
    def __init__(self, message,times=1) -> None:
        self.message = message
        self.times = times
    
    def showMessage(self): #self is the instance
        for x in range(self.times):
            print(self.message)

# p = Printer3("Knock Knock",3)
# p.showMessage()

#####################
##   Overriding    ##
#####################
# Commonly overloaded functions include:
#   str,repr,lt,le,gt,ge,eq,ne and of course init

class Person():
    def __init__(self, name, color, age=10) -> None:
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return f"My name is: {self.name} and {self.color} is the best.  You should know that I am {self.age}."

    def __eq__(self,other):
        if self.name == other.name:
            if self.color == other.color:
                return True
        return False

    def __ge__(self,other):
        return self.age >= other.age


p1 = Person("Bob", "Blue")
p2 = Person("Frank","Green",20)
p3 = Person("Bob", "Blue")

# print(p1)
# print(p2)
# print(p1 == p3)
# print(p2 >= p1)

#####################
##  Inheritance    ##
#####################
class Student(Person):
    def __init__(self,name,color,age=10,major="Comp Sci"):
        super().__init__(name,color,age) #super run the version of the function in the base class (universal Python info)
        self.major = major

    def __str__(self):
        return super().__str__() + " and I'm majoring in " + self.major

class Professor(Person):
    def __init__(self,name,color,age=10,courses=[]):
        super().__init__(name,color,age)
        self.courses = courses

    def __str__(self):
        return super().__str__() + " and I teach " + str(self.courses)

s1 = Student("Dylan", "red",19,"History")
# print(s1)
p1 = Professor("Professor Mittens","white", 4, ["Wet Food Analysis, Box Structures, Cat Nip Agriculture"])
# print(p1)

#####################
##  Private Vars   ##
##################### 
class Car():
    def __init__(self,color) -> None:
        self.__color = color  #__ private variables - can only be modified inside the class itself.  Keep things safe.
        self.__gear = "third" 

    def changeGear(self,newGear):
        self.__gear = newGear

    def __str__(self):
        return f'The car is {self.__color} and is currently in {self.__gear} gear'

c1 = Car("Blue")
# print(c1)
# # c1.__gear = "second"
# c1.changeGear("second")
# print(c1)

####################
##   Class Attr   ##
####################
# Also called static in many languages

class Animal():
    noise = "I dont make a noise"

    def __init__(self,name) -> None:
        self.__name = name

    def makeNoise(self):
        print(f'My name is {self.__name} and I like to go {type(self).noise}')

    def __str__(self):
        return f'My name is {self.__name}'

class Dog(Animal):
    noise = "Woof"
    
    def __init__(self,name,breed="Golden") -> None:
        super().__init__(name) #the super function gives access to methods and properties of a parent or child class.
        self.breed = breed

    def __str__(self):
        return super().__str__() + f' and I am a {self.breed} breed'

class Cat(Animal):
    noise = "Meow"
    
    def __init__(self,name,breed="Siamese") -> None:
        super().__init__(name)
        self.breed = breed

    def __str__(self):
        return super().__str__() + f' and I am a {self.breed} breed'

animals = [Dog("Rover","Daschund"),Cat("Sammy"),Dog("Spike","Pit"),Cat("Garfield","fat")]
# for animal in animals:
#     print(animal)
# print('\n\n')
# for animal in animals:
#     animal.makeNoise() #white method means it doesn't recognize the method (could be editor, or doesn't exist)


####################
##     Tasks      ##
####################
# Task #1  
# Write a class that stores a number and create a method that prints that number
class Number():
    def __init__(self,math):
        self.math=math
    
    def __str__(self):
        return f'The number is {self.math}'

n = Number(1)
print(n) #answer


# Task #2  
# Write a class called triangle that stores two numbers, base and height and has a method
# that returns the area of the triangle
class Triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def getarea(self):
        return self.base * self.height * 0.5

x = Triangle(10,50)
print(x.getarea())

# Task #3
# Write a class called rectangle that stores two numbers, width and length, and has a method
# that draws the rectangle using the given character
class Rectangle():
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def draw(self,char):
        for x in range(self.length):
            print(char*self.width)
    


# This code should draw it after writing your class
# r = Rectangle(3,6)
# r.draw('$')
# It should output this
#   @@@@
#   @@@@
#   


# Task #4
# Write a class called Video that stores three values: title, rating, lead actor
# Write a class called Movie that inherits from Video and also has a release year and genre
# Write a class called TV Show that inherits from Video and has a number of seasons and number of episodes
# Write a function in each class using __str__ that prints out all of the information in each of the above classes
# Create an instance of each class to demonstrate their functionality
class Video():
    def __init__(self,title='The West World',rating=7,lead_actor='Mark Vanburg'):
        self.title = title
        self.__rating = rating
        self.lead_actor = lead_actor
    
    def __str__(self):
        return(f'The title of this series was {self.title} and it got a rating of {self.__rating} from critics.  {self.lead_actor} is the lead actor.')

    def change_rating(self,new_rating):
        self.__rating = new_rating

p1 = Video('The West', 4, 'Harrison Ford')
# print(p1)

class Movie(Video):
    def __init__(self,title,rating,lead_actor,year=2012,genre='Historical'):
        super().__init__(title,rating,lead_actor)
        self.year = year
        self.genre = genre
        
    def __str__(self):
        return super().__str__() + f'This show was created in the year {self.year}.  It is in the {self.genre} genre.'

# print(Movie('Lone Survivor',9.5,'Mark Wahlburg',2013,'Action'))

class TvShow(Video):
    def __init__(self,title,rating,lead_actor,season=100,episode=10):
        super().__init__(title,rating,lead_actor)
        self.season = season
        self.episode = episode
    
    def __str__(self):
        return super().__str__() + f'This is currently in season {self.season}, episode {self.episode}'

show1 = (TvShow('M.A.S.H', 10, 'Joe Shmoe', 10, 150))
print(show1)
show1.change_rating(100)
print(show1)

    # def self.__change_rating = change_rating



# Task #5
# Add a method to the above classes that allows you to change the rating of any movie or tv show and make the rating variable private
# so that it can only be changed with that method.

#Write a function that will find the second largest in a list

#pass ignores the function
def basic_list(list1):
    pass
#1nd method
    # list1.sort()
    # return list1[-2]

#2nd method    
    # largest = max(list1)
    # list1.remove(largest)
    # return max(list1)
    
# list1 = [1,-3,100,1000,500]
# print(basic_list(list1))

#How long does it take this function to run?
#Sorting takes a lot of time.  Move lots of data around.  Overkill for a basic scenario.

#Given two strings, find if there is a sequence of at least 5 words in both strings
#Use case: checking for plagiarism.

#Create a fuction that takes in two variables
#define the string
#loop through the words until you find a match
#return the results

def matching_words(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
#Find all of the 5 word combinations in string1
    phrases = []
    string1 = string1.split()
    # for i in
    for i in range(len(string1)-1, 2, -1):
        for y in range(len(string1)-i -1):
            words = []
            for x in range(y, y + i):
                words.append(string1[x])
            phrases.append(words)

        for phrase in phrases:
            if ' '.join(phrase) in string2:
                print(phrase, 'Plagiarism', i)
                return

#Never define parameters in the function, defeats the purpose.  
# string1 = "The quick brown blue dark fox jumped over the lazy dog fence"
# string2 = "Whales are really big and the quick brown blue dark fox jumped past everything and it was marvelous!"
file1  = open('text1.txt', 'r')
string1 = file1.read()
file2  = open('text2.txt', 'r')
string2 = file2.read()

matching_words(string1, string2)

#Next, go through each combination and see if it exists in string2    

#Next, return True if found

#How could we change this to find the longest instance of repeated phrases of both strings.
#Create another nested loop?
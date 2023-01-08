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
#We're creating a list of words.
    phrases = []
    string1 = string1.split()
    # for i in
#range what variable starts.  -1 changes will decrease by 1.
    for i in range(len(string1)-1, 2, -1):
        for y in range(len(string1)-i -1):
            words = []
            for x in range(y, y + i):
                words.append(string1[x])
            phrases.append(words)

        for phrase in phrases:
#join whatever character is in it (words, etc)
            if ' '.join(phrase) in string2:     
                return phrase

#Never define parameters in the function, defeats the purpose.  
# string1 = "The quick brown blue dark fox jumped over the lazy dog fence"
# string2 = "Whales are really big and the quick brown blue dark fox jumped past everything and it was marvelous!"
def get_longest_matching_words(filename1,filename2):

    file1  = open(filename1, 'r')
    string1 = file1.read()
    file2  = open(filename2, 'r')
    string2 = file2.read()

    return matching_words(string1, string2)

#Next, go through each combination and see if it exists in string2    

#Next, return True if found

#How could we change this to find the longest instance of repeated phrases of both strings.
#Create another nested loop?


# Dynamic Programming implementation of LCS problem
 
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
 
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# end of function lcs
 
 
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
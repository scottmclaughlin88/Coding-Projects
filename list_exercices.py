#1write a function that prints out the list backwards.

def reverse_list(list):
    #length list -1 (first element), change index by -1 each time it executes
    for index in range(len(list)-1,-1,-1):
        print(list[index])

           



# list = ['Apple','Banana','Orange']
# reverse_list(list)



#2 write a function that prints out every 3rd item in the list
def skip_items_list(list):
    #length list -1 (first element), change index by -1 each time it executes
    for index in range(0,len(list),3):
        print(list[index])

#---------------------Practice list excercises
#---------------------Courtesy https://pynative.com/python-list-exercise-with-solutions/#h-exercise-1-reverse-a-list-in-python
#---------------------
#---------------------

# list1 = ['M', 'n', 'P', 'Pa']
# list2 = ['Ten', 'tanthou', 'oop']
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)

# nums = [2, 4, 5, 10]
# results = []
# for i in nums:
#         results.append(i * i)
# print(results)

# list = ['Apple','Banana','Orange',1,2,3,5,6]
# # skip_items_list(list)

#Concatenate two lists in the following order
# list1 = ['Lets', 'try this!']
# list2 = ['Yes', 'SIR!']
# list3 = list1 + list2
# print(list3)

#Say you have two lists.  Iterate on both lists simultaneously.  Display items from
#list1 in original order, while doing list2 in reverse order.

# list1 = [10, 30, 40, 50, 60]
# list2 = [1000, 2000, 3000, 4000, 5000]
# for l1, l2 in zip(list1, list2[::-1]):
#     print(l1, l2)

#Remove empty strings from the list of strings.
# list1 = ['Scott', '', 'Kelly', 'Roger', '']
# result = list(filter(None, list1))
# print(result)

#Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000, 7001], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


#3 write a fucntion that prints out the first and last item in the list.
def first_last_item(list):
    print(list[0])
    print(list[len(list)-1])

# list = ['Apple','Banana','Orange',1,2,3,5,6]
# first_last_item(list)
#4 write a function that only prints out items in the list that start with the letter b.
# def specific_letters(list):
#     #naturally the 3rd element in range is a 1
#     for index in range(0,len(list)): 
#         letters = str(list[index])
#         f_letter = letters[0]
#         if f_letter == 'b' or f_letter == 'B':
#             print(letters)

# specific_letters(list)

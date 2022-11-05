#1write a function that prints out the list backwards.

def reverse_list(list):
    #length list -1 (first element), change index by -1 each time it executes
    for index in range(len(list)-1,-1,-1):
        print(list[index])

           



list = ['Apple','Banana','Orange']
# reverse_list(list)



#2 write a function that prints out every 3rd item in the list
def skip_items_list(list):
    #length list -1 (first element), change index by -1 each time it executes
    for index in range(0,len(list),3):
        print(list[index])

           



list = ['Apple','Banana','Orange',1,2,3,5,6]
# skip_items_list(list)


#3 write a fucntion that prints out the first and last item in the list.
def first_last_item(list):
    print(list[0])
    print(list[len(list)-1])

list = ['Apple','Banana','Orange',1,2,3,5,6]
# first_last_item(list)
#4 write a function that only prints out items in the list that start with the letter b.
def specific_letters(list):
    #naturally the 3rd element in range is a 1
    for index in range(0,len(list)): 
        letters = str(list[index])
        f_letter = letters[0]
        if f_letter == 'b' or f_letter == 'B':
            print(letters)

specific_letters(list)

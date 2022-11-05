# write a function that takes in a list and a number and will print out every item from that list before the number.

# def sports(list,num): 
    # index = 0
    # while index < num:
    #     print(list[index])
    #     index += 1

# def sports_for(list,num):
#     for x in range(num):  #range excludes the last element
#         print(list[x])
def sports_for(list,num):
    times_printed = 0
    for item in list:
        if times_printed >= num:
            break
        print(item)
        times_printed += 1

list = ['Basketball','Soccer','Rugby','Baseball','Hockey']
num = 2


sports_for(list,num) #stuck on lines 8-11

#1 Change the function above to work with a while loop




#2 Change the fucntion above to work with a for loop, without using the range method.

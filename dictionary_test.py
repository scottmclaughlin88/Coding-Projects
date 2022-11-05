# # make the pieces for a battleship.

# #grab out the key from the dictionary, for efficiency
# ships = {'cruiser': 3,'submarine': 2} 
# #[] are used to access element(s) in a collection.
# ships['battleship'] = 4

# print(ships)
# ships['battleship'] = 5
# print(ships)
# print('length of', 'cruiser', ships['cruiser'])

# #doing for loops within a dictionary allows for the key,value pair, instead of one item
# # for name,length in ships.items():
#     # print(name,length)

# ships_list = ['cruiser','submarine']
# print(ships_list[1])
# #values out of a dictionary, use the key from the value pair []
# print(ships['battleship'])

#write a function that will take in a list of ships, and a list of sizes, and will create a dictionary where the ships are the keys
#and the sizes are the values
ships_list = ['cruiser','submarine','sailboat','row boat','USS Fake Battleship']
sizes_list = [4,3,2,1,100]
def create_boat_dictionary(ships_list,sizes_list):
    boat_dict = {}
#the loop through every ship using x as in the index in the list
    for x in range(len(ships_list)):
        boat_dict[ships_list[x]] = sizes_list[x]
    return boat_dict
boats = create_boat_dictionary(ships_list,sizes_list)
print(boats['submarine'])

#[] can be used to grab thigns from dicts, lists, strings - anything you need to grab a particular element from.
# ship = 'USS Fake Battleship'
# print(ship[4])

# nums = [1,-4,100,50,70]
# print(nums)
# #reverse the list using sort method
# nums.sort(reverse=True)
# print(nums)
def ships_sort(ship):
    return len(ship)
print(ships_list)
ships_list.sort()
print(ships_list)
ships_list.sort(key = ships_sort)
print(ships_list)



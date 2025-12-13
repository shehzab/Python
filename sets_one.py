# A set is an unordered collection of unique element  ulkike lists or tuples, sets do not allow duplicate elemetns and the order or elements is not guaranteed


my_Set = set({1,4,2,3,6,7})
my_new_set = {2,3,4}
print(my_Set)
print(my_new_set)



s = set(["banana", "apple", "cherry", "mango"])
print(s)


# Duplicates not allowed 

unique_player = { "chackochi", "chackochi", "eepachan", "eepachan","michael", "chenthamara"}

print(unique_player) #it prints just ones no duplicates 


# add  element to existing set

games ={ "subway surfers", "freefire","GTA Vice City" }

games.add("Call of Duty") # Adding one element


games.update(["takken 8", "prince of persia: the lost crown"]) # Adding multiple elements

print(games)

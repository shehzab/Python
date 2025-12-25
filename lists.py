
numbers = [1,2,3,4,5]

# print(len(numbers))

# mixed type of lists

mix = [1, "hello" , 3.12 ]
# print(mix[1])


# Accessing Items

my_list = [1,2,3,4,5]
# print(my_list[-2])



# using slices

my_list_slice = [0,1,2,3,4,5,6,7,8,9]
subset = my_list_slice[1:9:2]
subset1 = my_list_slice[4]
subset3 = my_list_slice[:6]
# print(subset3)
# print(subset)
# print(subset1)
 

#updating items

one = [1,2,3,4,5,6,7,8,9,0]

one[2] = 12

#print(one)

#removing using del

two = [1,2,3,4,5]

del two[1] 
#print(two)


#removing using remove()

five = [1,2,3,4]
five.remove(3)
# print(five)



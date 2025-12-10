single_quoted_string = 'Nee Po mone dinesha'

# print(single_quoted_string)


double_quoted = "sahara marubhoomilekk manal keti vidalllee"

# print(double_quoted)

multiline_string  = """
this is 
a multi line
string"""

# print(multiline_string)


# Concantenation

str1 = "Hello"

str2 = "world"

conc_string = str1  + " " + str2 

# print(conc_string)

# String Length

str = "python"

my_length = len(str)

# print(my_length)

# String indexing and Slicing

text = "python"
first_char = text[0]

substring = text[1:4]
# print(first_char)
# print(substring)



# String Formatting

name = "Balaraman"
 
hobby = " koode nadann kuthikal vettal"

formatted_string = f"I'm {name} , My hobby is {hobby}"
# print(formatted_string)

## str.capitalize() and str.title()
phrase= "Antha bhayam irukkanam"

cap_phrase = phrase.capitalize()
title_phrase = phrase.title()
# print(cap_phrase)
# print(title_phrase)

# str.replace(old , new)

sentence = " I love Fishcurry"
new = sentence.replace("Fishcurry", "Beef Mandhi")

# print(new )

# lists unpacking

number_god = [1,2,3,4]

one, two, three, four = number_god

print(number_god)

friends = ["ramanan","chaandi","sojan"]

ramanan, chaandi, sojan = friends
print(ramanan)

list_my = [1,2,3,4,5]

first, second, *rest = list_my
print(first)
print(second)
print(rest)
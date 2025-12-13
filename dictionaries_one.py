# DIctionary is a bultIn data type that represents a collection of key-value pairs. it is a highly flexible a nd efficient data structure used for mapping keys to values

#Empty dictionary

empty_dict = {}

# print(type(empty_dict))

# Dictionary with key-value pairs

student_info = {
  
  "name": "Ramanan",
  "age": 23,
  "grade":"B"
  
  }

# print(student_info)

# using the dict() constructor

person = dict(name="bobby",age="34")

# print(person)

# dict with different data types

mixed_dict = { "name":"chaathan", "age":21, "marks":[23,21,23,43], "is_student": True}

# print(mixed_dict)

# Nested Dict

nested_dict = {
  "person":{
    "name":"chithragupthan",
    "age":19234,
    "place":"narakam"
  },
  "pet":{
    "name":"pushkaran",
    "age":3,
    "species":"dog"
  }
}

# print(nested_dict["pet"]["name"])

# using a list of tuples


tuple_list = [("name","eva"), ("age",12),("city","london")]

from_tuple_list = dict(tuple_list)

# print(from_tuple_list)

# using get() method

my_dic =  {
  
  "name": "Ramanan",
  "age": 23,
  "grade":"B"
  
  }

# print(my_dic.get("name"))
# print(my_dic.get("history")) # output is none


# iterating through keys 
Vivarangal =  {
  
  "name": "Bharghavan Pillai",
  "age": 23,
  "grade":"B"
  
  }

#for key in Vivarangal:
 # print(f"{key}: {Vivarangal[key]}")


# iterating through items(key- value pairs)

history =  {
  
  "name": "raghavan mestri",
  "age": 43,
  "grade":"S"
  
  }

#for key, value in history.items():
 # print(f"{key}: {value}")

# Updating dictionaries

# adding new kwy-value pair

role =  {
  
  "name": "eepachan",
  "age": 43,
  "grade":0
  
  }
role["pallikoodam"] = "poyitilla"

#print(role)


#modifyinf Existing ones




role =  {
  
  "name": "eepachan",
  "age": 43,
  "grade":0
  
  }

role["age"] = 57
# print(role)

# Updating with another dict

cinema = {
  "name":"CID Moosa",
  "Character":"Moolam kuzhiyil sahadevan AKA CID MOOSA",
  "comedy":"Thorappan kochunni and team"
}
update_dict = {"year": 2003, "state": "kerala"}

cinema.update(update_dict)

#print(cinema)

# Updating with keyword arguments

his_dict = {
  "name": "xavier",
  "age":"37",
  "ishtam":"neelakoduveli"
}

his_dict.update(location="High range", vattaperu=" Saathan")
# print(his_dict)

# using setdefault()

his_dict = {
  "name": "xavier",
  "age":"37",
  "ishtam":"neelakoduveli"
}
his_dict.setdefault("villain","shaji paapan")

# print(his_dict)

# Deleteing elements from dict

# del

del_dic = {
  "name": "xavier",
  "age":"37",
  "ishtam":"neelakoduveli",
  "location":"High range",
  "vattaperu":" Saathan"
}

del del_dic["location"]
# print(del_dic)

# pop() method

del_dic = {
  "name": "xavier",
  "age":"37",
  "ishtam":"neelakoduveli",
  "location":"High range",
  "vattaperu":" Saathan"
}

del_dic.pop("age")

# print(del_dic)

# popitem() methid -- removes th last element
del_dic = {
  "name": "xavier",
  "age":"37",
  "ishtam":"neelakoduveli",
  "location":"High range",
  "vattaperu":" Saathan"
}

del_dic.popitem()

print(del_dic)
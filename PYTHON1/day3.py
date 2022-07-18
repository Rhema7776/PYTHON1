# # collection
# # Python Collections (Arrays)
# # There are four collection data types in the Python programming language:

# # List is a collection which is ordered and changeable. Allows duplicate members.
# # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# # Dictionary is a collection which is ordered** and changeable. No duplicate members.
# # LISTS[]
# fruits = ["apples", "strawberry",1, "oranges",4, "apples"]
# print(type(fruits))

# # To loop through a list

# for x in fruits:
#     print(x)

# for x in range(len(fruits)):
#     print(fruits[x])


# # TUPLES()
# tup1 = ("apples",1, "strawberry",True,1, "oranges")


# # print(type(tup1))

# # conv = list(tup1)
# # # trying a list method

# # conv.remove(1)
# # print(conv)

# # conv.insert(1, 'banana')
# # print(conv)

# # conv.append("melon")
# # print(conv)

# # conv.remove('oranges')
# # print(conv)

# # conv.pop(4)
# # print(conv)

# ## OR
# # del conv[4]
# # print(conv)

# # ## To completely delete a LIST,
# # # del conv
# # # print(conv)

# # ANOTHER TUPLE
# for x in range(0,10,1): #start, stop, step
#     print(x)
# # # DICTIONARIES{}
# Cars = {
#     "name": "mercedes",
#     "color": "grey",
#     "year" : "2000"
# }
# print(type(Cars))
# # SETS{}
# set1 = {"apples", "strawberry", "oranges"}
# print(type(set1))

# print(list(set1))

# # CHAIN CONDITIONALS
# # if condition = True:
# #     do something

# x = 3
# y = 4

# if y!=x:
#     print('understood')

# if y==x or y-x==1:
#     print("worked")

# if y>x and y+x==7:
#     print("w😊rking")

# if y>x and y+x==7 or y<=x:
#     print('ran')

# if not(y>x and y+x==7 or y<=x):
#     print('runing')

# if not(y<x) and y+x==7 :
#     print('w😊w!')

# else:
#     print('😊')

# # ELIF's
# std_score1 = 30
# std_score2 = 30
# std_score3 = 20

# if std_score1 > std_score2 and std_score2 > std_score3:
#     print(f"student score1 is higher by {std_score1-std_score2} marks")

#     if std_score1 == std_score3:
#         print("good to go")
# elif std_score1 == std_score2:
#     print("It's a tie")

# else:
#     print(f"student score2 is higher than student score1 by {std_score2-std_score1} marks")





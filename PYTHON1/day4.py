# # ITERATION BY ITEM

# fruits = ['apples', 'pears', 'oranges']

# # for fruit in fruits:
# #     print(fruit)
# ##OR

# # newVar = iter(fruits)
# # print(next(newVar))

# # N.B This is mostly used with tuples

# partners = ("Unilever", "KFC", "Skybank")

# newvar = iter(partners)
# print(next(newvar))
# print(next(newvar))
# print(next(newvar))

# # Alternatively
# for partner in partners:
#     print(partner)

# string1 = "Rhema"
# iterate = iter(string1)

# print(next(iterate))
# # print(string1[0])
# # print(len(string1))

# designers = ['gucci', 'LV', 'Dolce', 'balenciaga']
# # for designer in designers:
# #     print(designer)

# for i in range(0, 4):
#     if designers[i] == 'LV':
#         print(designers[i])

#     else:
#         print('not Luois Vuitton')

# # WHILE LOOPS

# # loop = True

# # while loop:
# #     name = input('What is your name: ')
# #     if name == 'Ayomide':
# #         print(f'Welcome, {name}!')
# #         loop = False
# #     else:
# #         print('failed, try again')

# students = [
#     {
#         "name": "peter",
#         "age": 20,
#         "hobbies": "football"
#     },
#     {
#         "name": "Shola",
#         "age": 17,
#         "hobbies": "G+"
#     }
# ]

# newAge = students[0]["age"] = 16
# newName = students[1]["name"] = "Egbon"
# print(newAge)
# print(newName)
# print(students)

# print(students[0])

# STRING METHODS - .strip(), .len(), .lower(), .upper(), .split()

# text = input('type something: ')

# print(len(text))
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.strip())
# # # print(text.split())
# print(text.split('.'))
# print(text.split('rhema'))

# # SLICE OPERATOR - [] [:] [::]
text = input('type something: ')

# [start]- start from somewhere to the end
print(text[0:])
print(text[1:])
print(text[2:])
# # [start:stop]- start from somewhere and stop b4 the end
print(text[0:24]) ##same as- print(text[0:24:1])
print(text[0:6])
print(text[0:1])
print(text[2: 16])
# # [start:stop:step]- - start from somewhere and stop b4 the end and take a step
# print(text[1:6]) #or print(text[1:6:1])
print(text[0:24:2])

# WHILE LOOPS
# loop = True
# name = 'Ayodele'
# password = 'TECH_studio1'

# while loop:
#     username = input('Input your username: ')
#     trypassword= input('Input your password: ')
#     if trypassword == password and username == name:
#         print(f'Welcome, {username}!')
#         loop = False     
#     else:
#         print('failed, try again')

# WHILE LOOPS

# loop = True

# while loop:
#     name = input('What is your name: ')
#     if name == 'Ayomide':
#         print(f'Welcome, {name}!')
#         loop = False
#     else:
#         print('failed, try again')



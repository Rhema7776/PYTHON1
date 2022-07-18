# name = "Funke"
# age = 34
# netWorth = "$89 thousand"

# print("Hi fam!", "my name is", name, "i am", age, "years old. My net-worth is", netWorth)

# # BASIC OPERATORS
# # +, -, /, *,

# # ** Exponentiation(raised to power)
# # // Floor division(ignores the remainder)
# # % Modulus(gives only the remainder)
num1 = 42
num2 = 19

num3 = num1-num2
print("ANSWER IS", num3)
# print(4+7)
# print(4-2)
# print(4*2)
# print(num1/2)
# print(4.0 - 2.2)
# print(4//2)
# print(4%2)

num4 = '40'
num5 = '60'

print(int(num4) + int(num5))

# print(3 == 3)
# print(2 > 4)
# print(True >= False)
# print(False == False)
# print('Hello' == "hello")


# print('Hello!, What is your name')
# name = input()

# print("Hi", name)
# OR
# Name = input('Hello, What is your name: ')
# print("Hi", Name)

# Dob = input('What is your birth year?: ')
# Current_year = input("What is the current year?: ")

# Age = int(Current_year) - int(Dob) 
# print(Name, "you are", Age, "years old")
# # # OR
# print(f"{Name} you are {Age} years old")

# HOW TO READ A TEXT FILE
file = open('rhema.txt', 'r')

f = file.readlines()
# to eliminate \n
newList = []
for line in f:
    newList.append(line.strip())

print(newList)
file.close()

# # HOW TO WRITE TO A TEXT FILE
file = open('rhema.txt', 'w')

# write = file.write('')
write= file.write('Hello\ni\nlove\ntech\nheee')
# # OR
# # file.write('i\n')
# # file.write('love\n')
# # file.write('tech\n')
# # file.write('DO you?')

print(write)
file.close()

# # DECISIONS (IF/ELSE/ELIF)
# Lakers = 102
# Rockets = 89

# if Lakers > Rockets: 
#     print('Lakers won  Rockets')

# else:
#     print('Lakers were defeated by the Rockets')

# name = 'rhema'

# if name:
#     print('My name is Rhema')
# else:
#     print('wrong name')

# # ex2

# model_height = input('Input your height: ')

# if float(model_height) == 6.0:
#     print('You are qualified')

# elif float(model_height) > 6.0:
#     print('You tall sha')
# else:
#     print('You are too short')

# # EX3
# age = input('Input your age: ')

# if int(age) == 18:
#     print('You are eligible to vote')
    
# elif int(age) > 18:
#     print('You are good to go')

# else:
#     print('You are younger than 18')

# CHAIN CONDITIONALS( AND / OR)/NESTED IFs

# a = 2
# b = 3

# if a == b and b+a == 5:
#     print('worked')
    
# else:
#     print('G😁😒D MORNING')
# a = 2
# b = 3

# if a == b and b+a == 5:
#     print('worked')

# if a == b or b+a ==5:

#     print('Worked') 
#     if a == 2 and a+b == 5:
#         print('a is 2 and a+b is 5')
#     if a == 2 and a-b == 5:
#         print('a is 2 and a-b is 5')
#         if b == 3 or a == 2:
#             print('pardon me')
#     if not (a == b or b+a ==5):
#         print('W😂RKS')    
# else:
#     print('G😁😒D MORNING')

# # Ex2
# if a == 2:
#     print('correct!')
#     if b == 3:
#         print('a=2, b=3')  
#     else:
#         print('a=2, b!=3')
# else:
#     print(a != 2)


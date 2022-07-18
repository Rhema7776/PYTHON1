number = 2;
print(number)

string = "Hello"
print(string)

Height = 6.8
print(Height)

x = '4'
# print(x)
print(type(x))
print(type(string))
print(type(Height))
# Data Types

# int 1, 2, 4,30
# str "3", 'welcome', 'Rhema'
# float 0.99, 4.2, -2.8
# bool True or False

# complex 1+5j, 1j, -5j

name = 'Lillian'
age = '18'
networth = '$70 Billion'

print("Hey i'm", name, "and i am", age, "years old")
#OR
print(f"Hey i'm {name} and i am {age} years old")

x = 2+3j
print(type(x))

y = 5j
print(type(y))
print(y)

# BASIC OPERATORS
# + addition
# - subtraction
# / Division 
# * multiplication

# ** Exponential(raised to power)
# % Modulus(gives remainder)
# // Floor division(ignores remainder)

print(2 + 3)
# or
a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
# or
c = a*b
print(c)
print(c/a)
print(a//b)
print(b%a)
print(b**a)
# print(a%b)

num1 = '2'
num2 = '5'

print(float(num1) + float(num2))

print(2 == 3)
print('Hello' == 'hello')
print(2+3 == 3+2)
print(2+3 == 3+2 and 4 == 2-5)
print(2+3 == 3+2 and 'LILLIAN' == 'LILLIAN')
print(int(num1) ** int(num2))
print(True == True)
print(False == False)
print(False == True)


print('What is your name? :')
name = input()

print('Hi', name)

# OR
# name = input('What is your name?')
# print('Hi', name)
Date_year = input('What is the current year?')
Date_birth = input('When were you born?')

Age = int(Date_year) - int(Date_birth)

print("Hi", name, "you are", Age, "years old")
print(f"Hi {name} you are {Age} years old")


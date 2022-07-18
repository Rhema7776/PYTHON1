# FUNCTIONS: definitiion functionName(parameter):
def addThree(x):

    return (x+3)

newNumber = addThree(4)
print(newNumber)

def subtractThree(x):

    return (x-3)

newnumber = subtractThree(4)
print(newnumber)

print(addThree(4) - newnumber)
#OR
print(newNumber - newnumber)

# sometimes you don't need to have a parameter
def saySomething():
    
    print('hi') 

saySomething()
#OR
def saySomething():
    
    return('hi') 

print(saySomething())

#if we were using a string,

def printString(str):
    return(str)

printRhema = printString('Rhema')
print(printRhema)

#without a return statement,

def printHello(str):
    print(str)

printHello('hello')

#IN PHYSICS
#using multiple parameters
# def area(length, width):
#     return(length * width)

# Result = area(2, 3)
# print(Result)

#  optional parameters

def func(x, text='1'):
    print(text)
    if text == '1':
        print('Text is 1')
    else: 
        print('Text is not 1')
func('rhema', )
# func('rhema', '23')

y = 'meet'

print(y.replace('m', ''))
print(y.replace('e', 'a'))

# MODULAR PROGRAMMING
import math

print(math.pi)
print(math.degrees(20))
print(math.radians(20))

import myModule

print(myModule.addFive(4))

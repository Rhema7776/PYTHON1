car = 'Volvo'
name = 'Rhema'
scores = 102
fuel_price = 20.4 
newvar = 3 == 4
empty = ''
print(type(empty))
print(type(fuel_price))
print(type(newvar))
print(car)
print(name)
print(scores)

Lakers = 102
Rockets = 39

if Lakers > Rockets:
    print('You get ten thousand box')

else:
    print('You loose ')

# age = input('Input your age: ')
# print('You put in', age)

# if int(age) == 15 :
#     print('You are eligible for the youth team')

# if int(age) > 15:
#     print('Bro youre older than 15')
    
# if int(age) > 18:
#     print('Baba you are not 15')

# else:
#     print("You are  either younger than 15 or 15")

# AdmissionFee = input('Have you recieved your admission fee reciept')
# Ielts = input('What is your IELTS score? ')
# Bsc = input('Do you have a B.sc cert')
# Visa = input('Student or travelers visa')

# if AdmissionFee == 'yes' or 'Yes':
#     print('You are good to go.. Continue with the process')
#     if int(Ielts)  >= 8 :
#         print("Very good score, you can proceed")
#         if Bsc == 'yes' or 'Yes':
#             print('Good to go')
#             if Visa == 'Student':
#                 print('Congratulations youve been admitted')
#             else:
#                 print('oops needs to be a student visa' )
#         else:
#             print('You need a Bsc ') 
#     else:
#         print("Your score isn't good enough")
# else:
#     print("We're so sorry you cannot continue this process")

FullName = input('Fill in your fullname')
print('welcome!')
Ielts = input("What's your IELTS score? : ")
Bsc = input("Do you have a Bsc certificate?: ")
A_fee = input("Have you recieved a payment reciept")

if A_fee == 'Yes':
    print("You can continue processing your admission")
    if Bsc == 'Yes':
        print("Good, you can continue processing your admission")
        if int(Ielts) >= 8:
            print("Congratulations, you will recieve a email on further processes")
        else:
            print("Sorry you did not make the cut off mark")
    if Bsc == 'No':
        print("you cannot apply for the masters degree but you can try our Bachelor's degree program")
else:
    print("We're so sorry you can't be admitted")
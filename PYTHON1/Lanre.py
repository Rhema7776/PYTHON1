name = 'Lanre'

if name == 'Lanre':
    print('CORRECT')

else:
    print('wrong')

# Conditions for studying abroad
# IELTS = 8
# BSC = "if No you cannot apply for the masters degree but you can try our Bachelor's degree program"
# Admition fee

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


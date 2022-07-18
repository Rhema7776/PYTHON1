# # # WHILE LOOPS
# # loop = True
# # name = 'Ayodele'
# # password = 'TECH_studio1'

# # while loop:
# #     username = input('Input your username: ')
# #     trypassword= input('Input your password: ')
# #     if trypassword == password and username == name:
# #         print(f'Welcome, {username}!')
# #         loop = False     
# #     else:
# #         print('failed, try again')

# ROCK PAPER SCISSORS GAME
from random import randint

options = ["Rock", "Paper", "Scissors"]
computer = options[randint(0,2)]
print(computer)
player = False
while player == False:
    player = input("Rock, Paper, Scissors: ")
    print(f'You picked {player}')
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You loose! {computer} covers {player}")
            
        else:
            print(f"You win! {player} smashes {computer}")
            break
            
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You loose! {computer} cuts {player}")
            
        else:
            print(f"You win! {player} covers {computer}")
            break
            
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You loose {computer} smashes {player} ")
            
        else:
            print(f"You win {player} cut {computer}")
            break

    else:
        print("Thats not a valid play, Check your spelling!")

    player = False    


# GUESSING GAME 2
# from random import randint

# number = randint(1,10)

# player_name = input("Hello, What is your name?: ")

# print(f'okay! {player_name} I am guessing a number between 1 and 10')

# number_of_guesses = 0

# while number_of_guesses < 5:
#     guess = int(input("guess the number: "))
#     print(guess)
#     number_of_guesses = number_of_guesses +1

#     if guess == number:
#         print(f"You guessed correctly in {number_of_guesses} tries")
#         break
#     elif guess <number:
#         print('Your guess is too low')
#     elif guess >number:
#         print('Your guess is too high')

#     else:
#         print(f"You did'nt guess correctly in {number_of_guesses} tries")
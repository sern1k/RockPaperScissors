from math import comb
import random

def Play():
    print("Let's play a game! What's your move?\n")
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print("Computer's choice:" ,computer)

    if user == computer:
        print('You lost!')
        print(Play())


    if Iswin(user, computer):
        return 'You won!'

    print('You lost!')
    print(Play())

def Iswin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(Play())
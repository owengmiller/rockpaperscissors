import random

print('~Rock Paper Scissors~')

def getPlayerMove():
    # Gets the player's move.
    pMove = ''
    while not (pMove == 'R' or pMove == 'P' or pMove == 'S'):
        print('Choose...\n Rock (R)\n Paper (P)\n Scissors (S)')
        print('')
        pMove = input().upper()
        if len(pMove) != 1:
            print('Please select move using (R), (P), or (S)!')     # Maybe come back to this!~
        elif pMove not in 'RPS':
            print('Please choose a valid move!')
        else:
            return pMove

def getComputerMove():
    # Gets the computer's move and displays it to the player.
    moveList = ['R', 'P', 'S']
    cMove = random.choice(moveList)
    if cMove in 'R':
        print('Your opponent chooses Rock.')
    elif cMove in 'P':
        print('Your opponent chooses Paper.')
    elif cMove in 'S':
        print ('Your opponent chooses Scissors.')
    return cMove

def getResults():
    # Tells the player whether they won or lost.
    if playerMove == computerMove:
        print("It is a tie.")
    elif playerMove == 'R' and computerMove == 'P':
        print("Paper beats rock! You lose!")
    elif playerMove == 'R' and computerMove == 'S':
        print("Rock beats scissors! You win!")
    elif playerMove == 'P' and computerMove == 'S':
        print("Scissors beats Paper! You lose!")
    elif playerMove == 'P' and computerMove == 'R':
        print("Paper beats Rock! You win!")
    elif playerMove == 'S' and computerMove == 'R':
        print("Rock beats Scissors! You lose!")
    elif playerMove == 'S' and computerMove == 'P':
        print("Scissors beats Paper! You win!")


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    playerMove = getPlayerMove()
    computerMove = getComputerMove()
    getResults()

    print('Play again? (y/n)')
    playAgain = input().lower()

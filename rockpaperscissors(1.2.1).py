import random

print('~Rock Paper Scissors~')
print('')

def getPlayerMove():
    # Gets the player's move, allowing for variation in length of word.
    print('Choose...\n Rock (R)\n Paper (P)\n Scissors (S)')
    print('')
    pDrop = input().lower()
    if pDrop == 'r' \
            or pDrop == 'ro' \
            or pDrop == 'roc' \
            or pDrop == 'rock':
        pMove = 'rock'
    elif pDrop == 'p' \
            or pDrop == 'pa' \
            or pDrop == 'pap' \
            or pDrop == 'pape' \
            or pDrop == 'paper':
        pMove = 'paper'
    elif pDrop == 's' \
            or pDrop == 'sc' \
            or pDrop == 'sci' \
            or pDrop == 'scis' \
            or pDrop == 'sciss' \
            or pDrop == 'scisso' \
            or pDrop == 'scissor' \
            or pDrop == 'scissors':
        pMove = 'scissors'
    else:
        print('Please enter a valid move!')
        pMove = ''
    return pMove

def getComputerMove():
    # Gets the computer's move and displays it to the player.
    moveList = ['rock', 'paper', 'scissors']
    cMove = random.choice(moveList)
    print('Your opponent chooses ' + cMove + '.')
    return cMove

def getResults():
    # Tells the player whether they won or lost.
    if playerMove == computerMove:
        print('It is a tie.')
    elif playerMove == 'rock' and computerMove == 'paper' \
            or playerMove == 'paper' and computerMove == 'scissors' \
            or playerMove == 'scissors' and computerMove == 'rock':
        print(computerMove.capitalize() + ' beats ' + playerMove + '! You lose!')
    elif playerMove == 'rock' and computerMove == 'scissors' \
            or playerMove == 'scissors' and computerMove == 'paper' \
            or playerMove == 'paper' and computerMove == 'rock':
        print(playerMove.capitalize() + ' beats ' + computerMove + '! You win!')


gameInProgress = 'yes'

while gameInProgress == 'yes' or gameInProgress == 'y':
    playerMove = getPlayerMove()
    if playerMove == 'rock' or playerMove == 'paper' or playerMove == 'scissors':
        computerMove = getComputerMove()
        getResults()

        print('Play again? (y/n)')
        gameInProgress = input().lower()
#  convert quiz data from list of dictionaries

from random import randint

playerNames = []
playerScores = []

quiz = [
        {
            'question': 'what is 4x4?',
            'answer': '16'
        },
        {
            'question': 'what is 3+3?',
            'answer': '6'
        },
        {
            'question': 'what is 4+6?',
            'answer': '10'
        },
        {
            'question': 'what is 1+1?',
            'answer': '2'
        },
        {
            'question': 'what is 6-3?',
            'answer': '3'
        }
    ]

# set up players
numberOfPlayers = int(input('How many players do you have? '))

# run quiz
currentPlayer = 0

while currentPlayer < numberOfPlayers:
    print('\nReady - Player', currentPlayer+1)
    input('Hit enter to play')
    score = 0
    questionNum = 1

    while questionNum <= len(quiz):
        print('Question:', questionNum)
        print(quiz[questionNum - 1]['question'])

        playerAnswer = input('?')
        if playerAnswer == quiz[questionNum - 1]['answer']:
            print('correct!')
            score += 1
        else:
            print('Incorrect, better luck next time')
        questionNum += 1

    print('You scored', score)
    currentPlayer += 1

print('End of quiz')
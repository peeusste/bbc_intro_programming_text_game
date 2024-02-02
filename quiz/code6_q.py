from random import sample

playerNames = []
playerScores = []

quiz = [
        {
            'topic': 'Maths',
            'question': 'what is the square root of 4',
            'answers': ['2', '4', '8', '1'],
            'correct': 1
        },
        {
            'topic': 'Maths',
            'question': 'what is the opposite of divide',
            'answers': ['sum', 'division', 'multiply', 'percent'],
            'correct': 3
        },
        {
            'topic': 'Maths',
            'question': 'what is 10 + 10',
            'answers': ['10', '20', '30', '40'],
            'correct': 2
        },
    ]

# set up players
numberOfPlayers = int(input('How many players do you have? '))

i = 0
while i < numberOfPlayers:
    print('Player', i + 1)
    name = input('Enter name of player - ')
    playerNames.append(name)
    playerScores.append(0)
    i += 1

# run quiz
currentPlayer = 0

while currentPlayer < numberOfPlayers:
    print('\nReady -', playerNames[currentPlayer])
    input('Hit enter to play')
    questionNum = 1

    while questionNum <= numberOfQuestions:
        print('Question:', questionNum, 'Topic:', questionSet[questionNum - 1]['topic'])
        print(questionSet[questionNum - 1]['question'])
        display_choices(questionNum - 1)
        playerAnswer = input('?')
        if ord(playerAnswer.upper())-64 == questionSet[questionNum - 1]['correct']:
            print('correct!')
            playerScores[currentPlayer] += 1
        else:
            print('Incorrect, better luck next time')
        questionNum += 1

    print('\nAt the end of that round', playerNames[currentPlayer], 'you have scored a total of',
          playerScores[currentPlayer])

    currentPlayer += 1

i = 0
winner = 0
while i < numberOfPlayers:
    if playerScores[i] > playerScores[winner]:
        winner = i
    i += 1

print('The winner with', playerScores[winner], 'points is', playerNames[winner])

# introduce lists, indexes, increments, checking, more complex conditionals,

questions = ['4x2', '10x5', '3x3']
answers = ['8', '50', '9']
question_index = 0
score = 0

while question_index < len(questions):
    print('\n'
          'Questions', question_index + 1, '-', questions[question_index])

    userAnswer = input('Your answer >')

    if userAnswer == answers[question_index]:
        print('Correct')
        score += 1
    else:
        print('Sorry, incorrect')

    question_index += 1

print('End of quiz')
print('You scored', score, 'out of', len(questions))

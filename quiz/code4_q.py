# dictionaries, modules and random

from random import randint

round1 = {
    'question': 'what is 4x4?',
    'answer': '16'
}
round2 = {
    'question': 'what is 3+3?',
    'answer': '6'
}
round3 = {
    'question': 'what is 4+6?',
    'answer': '10'
}
round4 = {
    'question': 'what is 1+1?',
    'answer': '2'
}
round5 = {
    'question': 'what is 6-3?',
    'answer': '3'
}
question_index = 0
number_of_rounds = randint(3, 5)
score = 0

while question_index < number_of_rounds:
    if question_index == 0:
        question = round1['question']
        answer = round1['answer']
    elif question_index == 1:
        question = round2['question']
        answer = round2['answer']
    elif question_index == 2:
        question = round3['question']
        answer = round3['answer']
    elif question_index == 3:
        question = round4['question']
        answer = round4['answer']
    else:
        question = round5['question']
        answer = round5['answer']

    print('\n'
          'Questions', question_index + 1, '-', question)

    userAnswer = input('Your answer >')

    if userAnswer == answer:
        print('Correct')
        score += 1
    else:
        print('Sorry, incorrect')

    question_index += 1

print('End of quiz')
print('You scored', score, 'out of', number_of_rounds)

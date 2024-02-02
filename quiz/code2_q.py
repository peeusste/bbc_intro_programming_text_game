# sequential order of instructions, input & output, loops and conditionals

while True:
    answer = input('What is 10 + 10: ')

    if answer == '20':
        print('correct')
    elif answer == '19':
        print('close but too low')
    elif answer == 'order pizza':
        print('close but you\'ve gone over')
    else:
        print('Incorrect - the answer is 20')
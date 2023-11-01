# sequential order of instructions, input & output, loops and conditionals

while True:
    myFirstVariable = input('What do you want to do >')

    if myFirstVariable == 'help':
        print('let me try to help you')
    elif myFirstVariable == 'sing':
        print('la la de da')
    elif myFirstVariable == 'order pizza':
        print("spicy american is on it's way")
    else:
        print('You typed - ', myFirstVariable, " - I don't know what to do about that")

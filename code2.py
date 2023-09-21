# introduce lists, indexes, increments, checking, more complex conditionals,

rooms = ['a bedroom', 'a kitchen', 'a sitting room']

room_index = 0

print('you are in', rooms[room_index])

while True:
    user_input = input('What do you want to do >').split(' ')

    if user_input[0] == 'go' or user_input[0] == 'move':
        print ('moving you', user_input[1] )
        room_index = room_index + 1
        if room_index == len(rooms): room_index = 0

        print('you are in', rooms[room_index])



    else: print ('sorry, I don\'t know how to help you')
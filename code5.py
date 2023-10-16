# dictionaries, try except, modules and random

from random import randint

me = {
    "name": "Simon",
    "born": "UK",
    "age": 34
}

rooms = ['a bedroom', 'a kitchen', 'a sitting room']

room_index = 0

print('your name is', me['name'], 'you were born in', me['born'], 'and your age is', me['age'])

print('you are in', rooms[room_index])
if randint(1, 3) == 1:
    print('a cold wind blows from somewhere...')

while True:
    user_input = input('What do you want to do >').split(' ')

    try:
        if user_input[0] == 'go' or user_input[0] == 'move':
            print('moving you', user_input[1])
            room_index = room_index + 1
            if room_index == len(rooms):
                room_index = 0

            print('you are in', rooms[room_index])

        else:
            print('sorry, I don\'t know how to help you')
    except:
        print('sorry, I don\'t know how to help you')

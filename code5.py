# dictionaries, modules and random

from random import randint

me = {
    "name": "Simon",
    "born": "UK",
    "age": 34
}

rooms = ['a bedroom', 'a kitchen', 'a sitting room']

room_index = 0

print('your name is', me['name'], 'you were born in', me['born'], 'and your age is', me['age'],'\n')

print('you are in', rooms[room_index])
if randint(1, 3) == 1:
    print('a cold wind blows from somewhere...')

while True:
    user_input = input('What do you want to do >')

    if user_input == 'go' or user_input == 'move':
        print('moving you to another room')
        room_index = room_index + 1
        if room_index == len(rooms):
            room_index = 0

        print('you are in', rooms[room_index])

    else:
        print('sorry, I don\'t know how to help you')

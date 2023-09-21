# first refactor with functions, lowercase, more complex data.py structures, 'in'

from random import randint

me = {
    "name": "Simon",
    "born": "UK",
    "age": 34
}

rooms = {

    'bedroom': {
        'description': 'a bedroom with exits north',
        'north': 'kitchen'},

    'kitchen': {
        'description': 'a dirty kitchen with exits north and south',
        'south': 'bedroom',
        'north': 'sitting room'},

    'sitting room': {
        'description': 'a large sitting room with duck wallpaper with a door to the south',
        'south': 'kitchen'}

}
current_room = 'bedroom'

def look_around(r):
    print('you are in', rooms[r]['description'])

    if randint(1, 5) == 1:
        x = randint(1, 3)
        if x == 1:
            print('a cold wind blows from somewhere...')
        elif x == 2:
            print('you notice a strange smell...')
        elif x == 3:
            print('a fly buzzes around annoyingly...')
    print()

def move_room(r, direction):
    new_room = r

    if dir in rooms[r]:
        new_room = rooms[r][direction]
        print('moving you', direction)
    else:
        print('you can\t go in that direction')

    look_around(new_room)

    return new_room


print('your name is', me['name'], 'you were born in', me['born'], 'and your age is', me['age'])
look_around(current_room)


while True:
    user_input = input('What do you want to do >').lower().split(' ')

    if user_input[0] == 'go' or user_input[0] == 'move':
        current_room = move_room(current_room, user_input[1])

    elif user_input[0] == 'north' or user_input[0] == 'east' or user_input[0] == 'south' or user_input[0] == 'west':
        current_room = move_room(current_room, user_input[0])

    elif user_input[0] == 'look':
        look_around(current_room)

    else:
        print('sorry, I don\'t know how to help you')

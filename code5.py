# iterate through a dictionary, boolean values, complex conditionals

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

objects = {
    'kettle': 'kitchen',
    'tv remote': 'sitting room'
}

def look_around(r):
    print('you are in', rooms[r]['description'])

    # show any objects in room
    for k, v in objects.items():
        if v == r:
            print('There is a', k, 'here')

    # random atmosphere
    if randint(1, 5) == 1:
        x = randint(1, 3)
        if x == 1:
            print('a cold wind blows from somewhere...')
        elif x == 2:
            print('you notice a strange smell...')
        elif x == 3:
            print('a fly buzzes around annoyingly...')
    print()

def move_room(r, dir):
    new_room = r

    if dir in rooms[r]:
        new_room = rooms[r][dir]
        print('moving you', dir)
    else:
        print('you can\t go in that direction')

    look_around(new_room)

    return new_room

def check_bag():
    empty = True
    for k, v in objects.items():
        if v == 'bag':
            print('You have a', k, 'in your bag')
            empty = False

    if empty:
        print('Your bag is empty')

    print()

def pickup(object):
    # object not in room
    if object not in objects or objects[object] != current_room:
        print ('You can\'t see a', object, 'here')

    else:
        print('You pick up a', object, 'and put it in your bag')
        objects[object] = 'bag'

    print()

def drop(object):
    # object not in bag
    if object not in objects or objects[object] != 'bag':
        print ('You dont\'t have a', object)

    else:
        print('You drop a', object)
        objects[object] = current_room

    print()


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

    elif user_input[0] == 'bag' or ( user_input[0] == 'check' and user_input[1] == 'bag'):
        check_bag()

    elif user_input[0] == 'get':
        pickup(user_input[1])

    elif user_input[0] == 'drop':
        drop(user_input[1])

    else:
        print('sorry, I don\'t know how to help you')

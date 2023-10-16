#  convert room data from list to dictionary, split command and use of len

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

print('your name is', me['name'], 'you were born in', me['born'], 'and your age is', me['age'])

if randint(1, 3) == 1:
    print('a cold wind blows from somewhere...')

print('you are in', rooms[current_room]['description'])
print()

while True:
    user_input = input('What do you want to do >').lower().split(' ')
    # user_input[0] = 'move' or 'go'; user_input[1] = 'north', 'east' etc.

    if (user_input[0] == 'go' or user_input[0] == 'move') and len(user_input) == 2:
        # we need to make sure there is a second argument before we check it
        if user_input[1] in rooms[current_room]:
            current_room = rooms[current_room][user_input[1]]
            print('moving you', user_input[1])
        else:
            print('you can\t go in that direction')

    else:
        print('sorry, I don\'t know how to help you')

    print('you are in', rooms[current_room]['description'])
    print()
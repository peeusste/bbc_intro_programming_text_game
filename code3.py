# introduce lists, indexes, increments, checking, more complex conditionals,

rooms = ['a bedroom', 'a kitchen', 'a sitting room']

room_index = 0

print('you are in', rooms[room_index])

while True:
    user_input = input('What do you want to do >')

    if user_input == 'go' or user_input == 'move':
        print('moving you to another room')
        room_index = room_index + 1
        if room_index == len(rooms):
            room_index = 0

        print('you are in', rooms[room_index])

        # This cycles you through room after room and brings you back to the start

    else:
        print("sorry, I don't know how to help you")



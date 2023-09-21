
personal = {
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

objects = {
    'kettle': 'kitchen',
    'tv remote': 'sitting room'
}
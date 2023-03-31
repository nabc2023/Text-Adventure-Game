rooms = {
    'start': {'description': 'You are standing in a dark room. There is a door to the north and a door to the east.', 'north': 'room1', 'east': 'room2'},
    'room1': {'description': 'You are in a bright room. There is a table in the center of the room.', 'south': 'start'},
    'room2': {'description': 'You are in a dusty room. There is a window on the west wall.', 'west': 'start'}
}

current_room = 'start'

while True:
    print(rooms[current_room]['description'])
    direction = input("Which direction do you want to go? ")
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("You can't go that way.")

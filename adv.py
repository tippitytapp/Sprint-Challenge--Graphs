from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
maze = dict()
anti_trav_path = []
visited_rooms = set()
anti_trav_dict = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# pull the room exits from the room method
def get_room_exits(room):
    # create a dictionary for the room using its id
    maze[room.id] = dict()
    # pull the exits rom the rooms get exits method
    exits = room.get_exits()
    # loop through the exits to create the dictionary with all "?"s
    for exit in exits:
        maze[room.id][exit] = '?'

# DFS through the map
def get_lost(room, directions):
    # the room you're coming from is the prev_room
    prev_room = player.current_room.id
    # your new direction will come for the list of directions that room has available
    new_dir = directions.pop(0)
    # moves the player into the new direction
    player.travel(new_dir)
    # new room id becomes players new current room id
    new_room_id = player.current_room.id
    new_room = player.current_room
    # add the direction you just traveled to the traversal path list
    traversal_path.append(new_dir)
    # get the way back from the dictionary i createdd
    pathback = anti_trav_dict.get(new_dir)
    # add that pathback to the anti travelled path
    anti_trav_path.append(pathback)
    # check to see if the new room is in the maze
    if new_room_id not in maze:
        # get it exits
        get_room_exits(new_room)
        # update the previous rooms insert for the maze
        maze[prev_room][new_dir] = new_room_id
        # update the new rooms insert for the maze
        maze[new_room_id][pathback] = prev_room
    else:
        # update the maze listing
        maze[prev_room][new_dir] = new_room_id

# BFS back to a room with a '?'
def go_back(room):
    # loop through the paths in the anti-trav-paths
    for move in anti_trav_path[::-1]:
        # move the player one of the rooms
        player.travel(move)
        # add that room to the traversal path
        traversal_path.append(move)
        # remove that room from the anti_trav_path
        anti_trav_path.pop(-1)
        # if there is a '?' its the room you're looking for
        if '?' in maze[player.current_room.id].values():
            return

# This runs the sim
# while the length of the maze is smaller than the number of rooms
while len(maze) < len(room_graph):
    # start the player off from his default current room
    new_room = player.current_room
    # check to see if that room is in the maze already
    if new_room.id not in maze:
        # if not then pull its exits from the rooms get_exits method
        get_room_exits(new_room)
    # keep track of paths unknown
    unknown_paths = []
    # for the directions and rooms in the new room
    for direction, room in maze[new_room.id].items():
        # if the room is a '?' add it to the unknown rooms list
        if room == '?':
            unknown_paths.append(direction)
    # dfs through the maze and get lost using the unknown paths and starting in the new room
    if len(unknown_paths) > 0:
        get_lost(new_room, unknown_paths)
    else:
        # do a bfs through the way back to find rooms with '?'s to go through
        if len(anti_trav_path) > 0:
            go_back(new_room)
        else:
            # get the exits of the room
            exits = new_room.get_exits()
            # choose a random door to go through
            door = random.choice(exits)
            # make the player go through the door
            player.travel(door)



# TRAVERSAL TEST

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
'''
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
        '''
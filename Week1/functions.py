# Escape game Functions

# functions.py

# define rooms and items

couch = {
    "name": "couch",
    "type": "furniture",

}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom2 = {
    "name": "bedroom 2",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

door_b = {
    "name": "door b",
    "type": "door",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",

}

dinning_table = {
    "name" : "double bed",
    "type" : "furniture",

}

dresser = {
    "name": "dresser",
    "type": "furniture",

}

dinning_table = {
    "name": "dinning table",
    "type": "furniture",

}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

door_c = {
    "name": "door c",
    "type": "door",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

outside = {
  "name": "outside"
}

all_rooms = [game_room, bedroom1, bedroom2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "bedroom 1": [queen_bed, door_b,door_c],
    "queen bed": [key_b],
    "bedroom 2": [door_b, double_bed, dresser],
    "double bed": [key_c],
    "dresser": [key_d],
    "living room": [dinning_table, door_d],
    "door a": [game_room, bedroom1],
    "door b": [bedroom1, bedroom2],
    "door c": [bedroom1, living_room],
    "door d": [outside],
    "dinning table": [living_room]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

game_state = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    esc_art = """

███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗    ██████╗  ██████╗  ██████╗ ███╗   ███╗     ██████╗  █████╗ ███╗   ███╗███████╗    
██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    
█████╗  ███████╗██║     ███████║██████╔╝█████╗      ██████╔╝██║   ██║██║   ██║██╔████╔██║    ██║  ███╗███████║██╔████╔██║█████╗      
██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝      ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      
███████╗███████║╚██████╗██║  ██║██║     ███████╗    ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    
                                                                                                                                     

"""
    
    print(esc_art)
    print("\n\033[1mWelcome to the Escape Game!!!\033[0m")
    print("\nYou wake up on a couch and find yourself in a strange house with no windows which you have never been to.")
    print("\nYou don't remember why you are here and what had happened before.")
    print("\nYou feel some unknown danger is approaching and you must get out of the house, \033[1mRIGHT NOW!\033[0m")
    print("\n\033[1m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \033[0m")
    print("\n\033[1mARE YOU READY? LOS GEHTS!!!\033[0m")
    play_room(game_state["current_room"])
    
def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    
    you_win_art = """

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝

                                                             
    
"""
    
    
    
    
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("\nCONGRATS!!! YOU ESCAPED ")
        print(you_win_art)
    else:
        print("\n\nYou are now in the " + room["name"] + ".")
        intended_action = input("\n    --> What would you like to do? Type 'explore' or 'examine'? ").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("\n    --> What would you like to examine? ").strip())
        else:
            print("\n    --> Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()  
        
def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("\nYou are exploring the " + room["name"] + ". Here you find: " + ", ".join(items))        
        
def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    locked_art = """


██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗         ██╗
██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╗██╔╝
██║     ██║   ██║██║     █████╔╝ █████╗  ██║  ██║    ╚═╝██║ 
██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██╗██║ 
███████╗╚██████╔╝╚██████╗██║  ██╗███████╗██████╔╝    ╚═╝╚██╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝         ╚═╝
                                                            

"""
   
    
    unlocked_art = """

██╗   ██╗███╗   ██╗██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗        ███╗
██║   ██║████╗  ██║██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╗╚██║
██║   ██║██╔██╗ ██║██║     ██║   ██║██║     █████╔╝ █████╗  ██║  ██║    ╚═╝ ██║
██║   ██║██║╚██╗██║██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██╗ ██║
╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╗██║  ██╗███████╗██████╔╝    ╚═╝███║
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝        ╚══╝
                                                                               


"""

    key_art = """                                                                                   
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                      ██████████                                                            
                  ████░░░░░░░░░░██████                                                   
                ██░░░░░░░░░░░░░░░░░░░░██                                                    
              ██░░░░░░░░░░░░░░░░░░░░░░░░██    ████                                          
            ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██                                          
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░████████████████████████████████            
          ██░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
          ██░░░░██      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
          ██░░░░██      ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
          ██░░░░██      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▓▓░░░░░░░░██            
          ██░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░██████░░██  ██░░░░██  ████████              
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██    ██      ████                          
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██                                          
              ██░░░░░░░░░░░░░░░░░░░░░░░░██    ████                                          
                ██░░░░░░░░░░░░░░░░░░░░██                                                    
                  ████░░░░░░░░░░██████                                                      
                  ░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░                                                      
                                                                                            
                                                                                            
                                                                                         
                 """
    
    
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "\nYou examine the " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "\n\n>>> You unlock it with a key you have. Well done!!! <<<"
                    print(unlocked__art)
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "\nIt is locked but you don't have the key. Keep trying."
                    print(locked_art)
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "\n\n>>> You found " + item_found["name"] + ". <<<"
                    print(key_art)
                else:
                    output += "\nThere isn't anything interesting about it. Look somewhere else!"
            print(output)
            break

    if(output is None):
        print("\nThe item you requested is not found in the current room.")
    
    if(next_room and input("\n    --> Do you want to go to the next room? Enter 'yes' or 'no' ").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)
       

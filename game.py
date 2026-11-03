locations = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

def new_game(name):
    player = {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }
    return player


def move_player(player, destination):
    if player["game_over"]:
        return "The game is already over"

    current_location = player["location"]

    if destination not in locations[current_location]:
        return "Invalid destination"
        
    elif destination == "Old Bridge" and "rope" not in player["inventory"]:
        return "You cannot cross the bridge without a rope"
    else:
        player["location"] = destination
        player["energy"] -= 1

        if player["energy"] == 0:
            player["game_over"] = True
            return "Game Over, You ran out of energy"
        return "Movement was successful"

def explore(player):
    if player["game_over"]:
        return "The game is already over"
    
    location = player["location"]
    inventory = player["inventory"]

    if location == "Jungle":
        if "rope" not in inventory:
            inventory.append("rope")
            return "You collected a rope"
        else:
            return "You already collected the rope"

    elif location == "Cave":
        if "lantern" not in inventory:
            inventory.append("lantern")
            return "You collected a lantern"
        else:
            return "You already collected the lantern"

    elif location == "Lighthouse":
        if "lantern" in inventory and player["energy"] > 0:
            player["won"] = True
            player["game_over"] = True

            return "Congratulations, You restored the lighthouse beacon"

        else:
            return "You need a lantern to light the beacon"

    else:
        return "Nothing useful to explore here"
        
    
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
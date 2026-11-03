from game import locations, new_game, move_player

print("=== MYSTERY ISLAND ===")
print("The Lost Lighthouse\n")

name = input("Enter your name: ")
player = new_game(name)


print(f"\nWelcome to Mystery Island, {name}")
print("You wake up on a beach after a terrible storm")
print("Your mission is to restore the lighthouse beacon\n")

print(f"Current Location: {player['location']}")
print(f"Energy: {player['energy']}")
print(f"Inventory: {player['inventory']}\n")

while True:
    print("\n1. Move")
    print("2. Explore")
    print("3. Check Inventory")
    print("4. Quit\n")

    choices = input("Select an option: ").strip()

    if choices == "1":
        location = player["location"]

        print(f"Available locations: {locations[location]}")

        destination = input("Where do you want to go? ").strip().title()
        message = move_player(player, destination)

        print(message)
        print(f"Remaining energy: {player['energy']}")

        if player["game_over"]:
            break

    elif choices == "2":
        location = player["location"]
        inventory = player["inventory"]

        if location == "Jungle":
            print("You found a rope")

            if "rope" not in inventory:
                inventory.append("rope")
                print("You collected a rope")

            else:
                print("You already collected the rope")

        elif location == "Cave":
            print("You found a lantern")

            if "lantern" not in inventory:
                inventory.append("lantern")
                print("You collected a lantern")

            else:
                print("You already collected the lantern")

        elif location == "Lighthouse":
            if "lantern" in inventory and player["energy"] > 0:
                player["won"] = True
                player["game_over"] = True

                print("Congratulations! You restored the lighthouse beacon!")
                break

            else:
                print("You need a lantern to light the beacon.")

        else:
            print("Nothing useful to explore here.")

    elif choices == "3":
        print(f"Inventory: {player['inventory']}")

    elif choices == "4":
        player["game_over"] = True
        print("Goodbye, Thanks for playing")
        break

    else:
        print("Invalid choice. Please try again")
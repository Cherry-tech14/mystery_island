from game import locations, new_game, move_player, explore

print("=== MYSTERY ISLAND ===")
print("The Lost Lighthouse\n")

name = input("Enter your name: ")

while True:
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
            message = explore(player)
            print(message)

            if player["game_over"]:
                break

        elif choices == "3":
            print(f"Inventory: {player['inventory']}")

        elif choices == "4":
            player["game_over"] = True
            print("Goodbye, Thanks for playing")
            break

        else:
            print("Invalid choice. Please try again")

    replay = input("\nWould you like to play again? (yes/no): ").strip().lower()

    if replay != "yes":
        print("Thanks for playing Mystery Island")
        break
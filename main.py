from game import locations

print("=== MYSTERY ISLAND ===")
print("The Lost Lighthouse\n")

name = input("Enter your name: ")
print(f"\nWelcome to Mystery Island, {name}")
print("You wake up on a beach after a terrible storm")
print("Your mission is to restore the lighthouse beacon\n")

location = "Beach"
print(f"Current Location: {location}")

energy = 5
print(f"Energy: {energy}")

inventory = []
print(f"Inventory: {inventory}\n")

while True:
    print("1. Move")
    print("2. Explore")
    print("3. Check Inventory")
    print("4. Quit\n")

    choices = input("Select an option: ").strip()

    if choices == "1":
        print(f"Available locations: {locations[location]}")
        destination = input("Where do you want to go? ").strip().title()

        if destination not in locations[location]:
            print("Invalid destination")

        elif destination == "Old Bridge" and "rope" not in inventory:
            print("You cannot cross the bridge without a rope")

        else:
            location = destination
            energy -= 1
            print(f"You moved to {location}")
            print(f"Remaining energy: {energy}")

        if energy == 0:
            print("Game Over! You ran out of energy.")
            break

        

    
    elif choices == "2":
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
            if "lantern" in inventory and energy > 0:
                print("Congratulations! You restored the lighthouse beacon!")
                break
            else:
                print("You need a lantern to light the beacon.")


    elif choices == "3":
        print(f"Inventory: {inventory}")

    elif choices == "4":
        print("Goodbye, Thanks for playing")
        break

    else:
        print("Invalid choice. Please try again")
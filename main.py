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

        if destination in locations[location]:
            location = destination
            print(f"You moved to {location}")

        else:
            print("Invalid destination, You cannot move there")

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


    elif choices == "3":
        print(f"Inventory: {inventory}")

    elif choices == "4":
        print("Goodbye, Thanks for playing")
        break

    else:
        print("Invalid choice. Please try again")
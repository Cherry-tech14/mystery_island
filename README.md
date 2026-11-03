# Mystery Island — The Lost Lighthouse

## Project Description

Mystery Island is an interactive command-line adventure game built using Python.

The player wakes up on a mysterious island after a terrible storm. The mission is to explore different locations, collect useful items, overcome obstacles, and restore the lighthouse beacon.

The player must complete the mission before running out of energy.

## Features

- Interactive command-line interface (CLI).
- Five locations to explore.
- Player movement between connected locations.
- Energy management system.
- Inventory system for collecting items.
- Rope requirement for crossing the Old Bridge.
- Lantern requirement for restoring the lighthouse beacon.
- Winning and losing conditions.
- Replay option after the game ends.
- Automated unit tests.

## Game Locations

The game contains five locations:

1. **Beach:** The player's starting location.
2. **Jungle:** The player can collect a rope.
3. **Cave:** The player can collect a lantern.
4. **Old Bridge:** The player needs a rope to enter.
5. **Lighthouse:** The player must use the lantern to restore the beacon and win.

## How to Play

1. Start the game and enter your name.
2. The player begins at the Beach with 5 energy points.
3. Choose an option from the main menu.
4. Move between connected locations.
5. Explore the Jungle to collect a rope.
6. Explore the Cave to collect a lantern.
7. Use the rope to access the Old Bridge.
8. Reach the Lighthouse with the lantern and at least 1 energy point.
9. Explore the Lighthouse to restore the beacon and win.

Each successful movement reduces the player's energy by 1 point.

If the player's energy reaches 0, the game ends.

### Replay

After winning, losing, or quitting, the player can choose to start a new game.

A new game resets the player's location, energy, inventory, and game status.


### File Descriptions

**main.py**

Handles the command-line interface, player input, menu options, and replay functionality.

**game.py**

Contains the main game logic, including player creation, movement, energy management, exploration, item collection, and winning conditions.

**test_game.py**

Contains automated unit tests for checking the game's functionality.

**README.md**

Provides documentation and instructions for running the project.

## How to Run the Game

Open a terminal in the project directory.

Run:

```bash
python3 main.py
```

Follow the instructions displayed in the terminal.

### Run the tests using:

```bash
python3 -m unittest test_game.py -v
```

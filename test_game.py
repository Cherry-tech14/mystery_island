import unittest
from game import new_game, move_player, explore

class TestGame(unittest.TestCase):

    def test_starting_location(self):
        player = new_game("Alex")
        self.assertEqual(player["location"], "Beach")

    def test_starting_energy(self):
        player = new_game("Alex")
        self.assertEqual(player["energy"], 5)

    def test_starting_inventory(self):
        player = new_game("Alex")
        self.assertEqual(player["inventory"], [])

    def test_initial_game_status(self):
        player = new_game("Alex")
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])

    def test_valid_movement(self):
        player = new_game("Alex")

        move_player(player, "Jungle")

        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)

    def test_invalid_movement(self):
        player = new_game("Alex")

        message = move_player(player, "Lighthouse")

        self.assertEqual(message, "Invalid destination")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_bridge_without_rope(self):
        player = new_game("Alex")
        player["location"] = "Cave"

        message = move_player(player, "Old Bridge")

        self.assertEqual(
            message,
            "You cannot cross the bridge without a rope"
        )
        self.assertEqual(player["location"], "Cave")

    def test_collect_rope(self):
        player = new_game("Alex")
        player["location"] = "Jungle"

        explore(player)

        self.assertIn("rope", player["inventory"])

    def test_collect_lantern(self):
        player = new_game("Alex")
        player["location"] = "Cave"

        explore(player)

        self.assertIn("lantern", player["inventory"])

    def test_duplicate_rope(self):
        player = new_game("Alex")
        player["location"] = "Jungle"

        explore(player)
        explore(player)

        self.assertEqual(player["inventory"].count("rope"), 1)

    def test_energy_depletion(self):
        player = new_game("Alex")
        player["location"] = "Jungle"
        player["energy"] = 1

        move_player(player, "Beach")

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])

    def test_winning_condition(self):
        player = new_game("Alex")
        player["location"] = "Lighthouse"
        player["inventory"].append("lantern")

        message = explore(player)

        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])
        self.assertEqual(
            message,
            "Congratulations, You restored the lighthouse beacon"
        )


if __name__ == "__main__":
    unittest.main()
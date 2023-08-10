import unittest
import service.game_service as game_service
from domain.game import Game

class Game_service_test(unittest.TestCase):

    def test_create_filled_game(self): 
        game = game_service.create_filled_game(2, 3, {"Dono da Bola", "Mocinha"}, {"Dono da Bola": -2, "Mocinha": -1}, [])
        self.assertEqual(game.name, "game_2")
        self.assertEqual(game.total_kills, 3)
        self.assertEqual(game.players, {"Dono da Bola", "Mocinha"})
        self.assertEqual(game.kills, {"Dono da Bola": -2, "Mocinha": -1})
        self.assertEqual(game.alert_messages, [])
    
    def test_find_game(self): 
        games = [Game(1), Game(2), Game(3), Game(4)]
        game = game_service.find_game(games, 3)
        self.assertEqual(game.name, "game_3")

    def test_create_json(self): 
        game = Game(1)
        game_json = game_service.create_json(game)
        expected_json = "{\"game_1\": {\"total_kills\": 0, \"players\": [], \"kills\": {}}}"
        self.assertEqual(game_json, expected_json)

if __name__ == "__main__":
     unittest.main()
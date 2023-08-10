import unittest
from domain.game import Game
from service.game_service import create_filled_game

class Add_player_test(unittest.TestCase):

    def test_add_first_player(self): 
        game = Game(1)
        game.add_player("Test")
        self.assertEqual(game.players, {"Test"})
        self.assertEqual(game.kills, {"Test": 0})
    
    def test_add_new_player(self): 
        game = create_filled_game(3, 3, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 2, "Mocinha": 1})
        game.add_player("Test")
        self.assertEqual(game.players, {"Mocinha", "Dono da Bola", "Test"})
        self.assertEqual(game.kills, {"Dono da Bola": 2, "Mocinha": 1, "Test": 0})

    def test_add_existing_player(self): 
        game = create_filled_game(3, 3, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 2, "Mocinha": 1})
        game.add_player("Mocinha")
        self.assertEqual(game.players, {"Mocinha", "Dono da Bola"})
        self.assertEqual(game.kills, {"Dono da Bola": 2, "Mocinha": 1})

if __name__ == "__main__":
     unittest.main()
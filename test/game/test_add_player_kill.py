import unittest
from domain.game import Game
from service.game_service import create_filled_game

class Add_player_test(unittest.TestCase):

    def test_add_first_kill(self): 
        game = Game(1)
        game.add_player("Test")
        game.add_player("Mocinha")
        game.add_player_kill("Test")
        self.assertEqual(game.players, {"Test", "Mocinha"})
        self.assertEqual(game.kills, {"Test": 1, "Mocinha": 0})
    
    def test_add_new_kill(self): 
        game = create_filled_game(3, 3, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 2, "Mocinha": 1}, [])
        game.add_player_kill("Mocinha")
        self.assertEqual(game.players, {"Mocinha", "Dono da Bola"})
        self.assertEqual(game.kills, {"Dono da Bola": 2, "Mocinha": 2})

    def test_add_existing_player(self): 
        game = create_filled_game(3, 3, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 2, "Mocinha": 1}, [])
        game.add_player_kill("Test")
        self.assertEqual(game.players, {"Mocinha", "Dono da Bola"})
        self.assertEqual(game.kills, {"Dono da Bola": 2, "Mocinha": 1})

if __name__ == "__main__":
     unittest.main()
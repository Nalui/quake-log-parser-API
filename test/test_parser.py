import unittest
from service.parser_service import file_reader
from service.game_service import create_filled_game
from domain.game import Game
from domain.game_matcher import Game_matcher

RESULT = file_reader("test.log")

class Parser_test(unittest.TestCase):

    def test_case_1(self): 
        game_case_1 = create_filled_game(1, 0, {"Isgalamido"}, {"Isgalamido": 0})
        game_result = RESULT[0]
        self.assertEqual(Game_matcher(game_case_1), game_result)
    
    def test_case_2(self): 
        game_case_2 = create_filled_game(2, 3, {"Dono da Bola", "Mocinha"}, {"Dono da Bola": -2, "Mocinha": -1})
        game_result = RESULT[1]
        self.assertEqual(Game_matcher(game_case_2), game_result)

    def test_case_3(self): 
        game_case_3 = create_filled_game(3, 3, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 2, "Mocinha": 1})
        game_result = RESULT[2]
        self.assertEqual(Game_matcher(game_case_3), game_result)

    def test_case_4(self): 
        game_case_4 = create_filled_game(4, 10, {"Maluquinho", "Dono da Bola", "Fasano Again", "Oootsimo", "Isgalamido", "UnnamedPlayer", "Zeh"}, \
                                    {"Fasano Again": 0, "Oootsimo": 1, "Isgalamido": 3, "Zeh": 0, "Dono da Bola": 1, "UnnamedPlayer": 0, "Maluquinho": 1})
        game_result = RESULT[3]
        self.assertEqual(Game_matcher(game_case_4), game_result)

    def test_case_5(self): 
        game_case_5 = create_filled_game(5, 1, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": 0}, \
                                  ["The game did not shut down properly."])
        game_result = RESULT[4]
        self.assertEqual(Game_matcher(game_case_5), game_result)

    def test_case_6(self): 
        game_case_6 = create_filled_game(6, 2, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": -1}, \
                                  ["Player Zeh is not in players set and therefore cannot be killed."])
        game_result = RESULT[5]
        self.assertEqual(Game_matcher(game_case_6), game_result)

    def test_case_7(self): 
        game_case_7 = create_filled_game(7, 1, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": 0}, \
                                  ["Player Zeh is not in players set and therefore cannot kill."])
        game_result = RESULT[6]
        self.assertEqual(Game_matcher(game_case_7), game_result)

if __name__ == "__main__":
     unittest.main()
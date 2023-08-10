import unittest
from service.parser_service import file_reader
from service.game_service import create_filled_game
from domain.game_matcher import Game_matcher

RESULT = file_reader("test.log")

class Parser_test(unittest.TestCase):
    '''Case 1: game with one player and zero kills'''
    def test_case_1(self): 
        game_case_1 = create_filled_game(1, 0, {"Isgalamido"}, {"Isgalamido": 0}, [])
        game_result = RESULT[0]
        self.assertEqual(Game_matcher(game_case_1), game_result)
    
    '''Case 2: game with only <world> kills'''
    def test_case_2(self): 
        game_case_2 = create_filled_game(2, 3, {"Dono da Bola", "Mocinha"}, {"Dono da Bola": -2, "Mocinha": -1}, [])
        game_result = RESULT[1]
        self.assertEqual(Game_matcher(game_case_2), game_result)

    '''Case 3: game with only player kills'''
    def test_case_3(self): 
        game_case_3 = create_filled_game(3, 3, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 2, "Mocinha": 1}, [])
        game_result = RESULT[2]
        self.assertEqual(Game_matcher(game_case_3), game_result)
    
    '''Case 4: game with <world> and player kills with new plyers in the middle of the game'''
    def test_case_4(self): 
        game_case_4 = create_filled_game(4, 10, {"Maluquinho", "Dono da Bola", "Fasano Again", "Oootsimo", "Isgalamido", "UnnamedPlayer", "Zeh"}, \
                                    {"Fasano Again": 0, "Oootsimo": 1, "Isgalamido": 3, "Zeh": 0, "Dono da Bola": 1, "UnnamedPlayer": 0, "Maluquinho": 1}, [])
        game_result = RESULT[3]
        self.assertEqual(Game_matcher(game_case_4), game_result)

    '''Case 5: game with no ShutdownGame''' 
    def test_case_5(self):
        game_case_5 = create_filled_game(5, 1, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": 0}, \
                                  ["Line 103: The game did not shut down properly."])
        game_result = RESULT[4]
        self.assertEqual(Game_matcher(game_case_5), game_result)
    
    '''Case 6: game with invalid <world> kill - killed exists but is not in the game'''
    def test_case_6(self):   
        game_case_6 = create_filled_game(6, 2, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": -1}, \
                                  ["Line 114: Player Zeh is not in players set and therefore cannot be killed."])
        game_result = RESULT[5]
        self.assertEqual(Game_matcher(game_case_6), game_result)

    '''Case 7: game with invalid killer - killer exists but is not in the game'''
    def test_case_7(self): 
        game_case_7 = create_filled_game(7, 1, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": 0}, \
                                  ["Line 127: Player Dono is not in players set and therefore cannot kill."])
        game_result = RESULT[6]
        self.assertEqual(Game_matcher(game_case_7), game_result)

    '''Case 8: game with invalid killer - can't get killer'''
    def test_case_8(self): 
        game_case_8 = create_filled_game(8, 2, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": -1}, \
                                  ["Line 141: Unable to find killed"])
        game_result = RESULT[7]
        self.assertEqual(Game_matcher(game_case_8), game_result)

    '''Case 9: game with invalid<world> kill - can't get killed'''
    def test_case_9(self): 
        game_case_9 = create_filled_game(9, 1, {"Mocinha", "Dono da Bola"}, {"Dono da Bola": 1, "Mocinha": 0}, \
                                  ["Line 154: Unable to find killer"])
        game_result = RESULT[8]
        self.assertEqual(Game_matcher(game_case_9), game_result)

if __name__ == "__main__":
     unittest.main()
import unittest
from unittest.mock import patch
from werkzeug import exceptions
from controller.game_controller import get_game

class Get_game_testl(unittest.TestCase):

    def test_list_all_successful(self): 
        result = get_game("test.log", 1)
        expected_result = "{\"game_1\": {\"total_kills\": 0, \"players\": [\"Isgalamido\"], \"kills\": {\"Isgalamido\": 0}}}"
        self.assertCountEqual(result, expected_result)

    def test_list_all_unsuccessful(self):
        with self.assertRaisesRegex(exceptions.NotFound, "404 Not Found: File invalid.log not found. Try to use 'games.log' or 'test.log'"):
            get_game("invalid.log", 1)
        
        with self.assertRaisesRegex(exceptions.NotFound, "404 Not Found: Game number 11 not found"):
            get_game("test.log", 11)        
    
if __name__ == "__main__":
     unittest.main()
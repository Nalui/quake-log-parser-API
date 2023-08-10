import unittest
from unittest.mock import patch
from werkzeug import exceptions
from controller.game_controller import list_all

class List_all_testl(unittest.TestCase):

    def test_list_all_successful(self): 
        result = list_all("test.log")
        expected_result = [
                            "{\"game_1\": {\"total_kills\": 0, \"players\": [\"Isgalamido\"], \"kills\": {\"Isgalamido\": 0}}}",
                            "{\"game_2\": {\"total_kills\": 3, \"players\": [\"Dono da Bola\", \"Mocinha\"], \"kills\": {\"Dono da Bola\": -2, \"Mocinha\": -1}}}",
                            "{\"game_3\": {\"total_kills\": 3, \"players\": [\"Dono da Bola\", \"Mocinha\"], \"kills\": {\"Dono da Bola\": 2, \"Mocinha\": 1}}}",
                            "{\"game_4\": {\"total_kills\": 10, \"players\": [\"Zeh\", \"Dono da Bola\", \"Isgalamido\", \"UnnamedPlayer\", \"Maluquinho\", \"Oootsimo\", \"Fasano Again\"], \"kills\": {\"Fasano Again\": 0, \"Oootsimo\": 1, \"Isgalamido\": 3, \"Zeh\": 0, \"Dono da Bola\": 1, \"UnnamedPlayer\": 0, \"Maluquinho\": 1}}}",
                            "{\"game_5\": {\"total_kills\": 1, \"players\": [\"Dono da Bola\", \"Mocinha\"], \"kills\": {\"Dono da Bola\": 1, \"Mocinha\": 0}, \"alert_messages\": [\"The game did not shut down properly.\"]}}",
                            "{\"game_6\": {\"total_kills\": 2, \"players\": [\"Dono da Bola\", \"Mocinha\"], \"kills\": {\"Dono da Bola\": 1, \"Mocinha\": -1}, \"alert_messages\": [\"Player Zeh is not in players set and therefore cannot be killed.\"]}}",
                            "{\"game_7\": {\"total_kills\": 1, \"players\": [\"Dono da Bola\", \"Mocinha\"], \"kills\": {\"Dono da Bola\": 1, \"Mocinha\": 0}, \"alert_messages\": [\"Player Dono is not in players set and therefore cannot kill.\"]}}"
                            ]
        for i in range(len(result)):
            self.assertCountEqual(result[i], expected_result[i])

    def test_list_all_unsuccessful(self):
        with self.assertRaisesRegexp(exceptions.NotFound, "404 Not Found: File invalid.log not found. Try to use 'games.log' or 'test.log'"):
            list_all("invalid.log")
    
if __name__ == "__main__":
     unittest.main()
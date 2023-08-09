from service.parser import file_reader
import service.game as game_service

def list_all():
    return file_reader("test.log")

def get_game(game_number):
    return game_service.find_game(file_reader("test.log"), game_number)        
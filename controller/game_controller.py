from service.parser_service import file_reader
import service.game_service as game_service

def list_all():
    games = file_reader("test.log")
    return game_service.create_json_list(games)

def get_game(game_number):
    game = game_service.find_game(file_reader("test.log"), game_number)
    return game_service.create_json(game)        
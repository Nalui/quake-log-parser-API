from service.parser_service import file_reader
import service.game_service as game_service

def list_all(file_name):
    games = file_reader(file_name)
    return game_service.create_json_list(games)

def get_game(file_name, game_number):
    game = game_service.find_game(file_reader(file_name), game_number)
    return game_service.create_json(game)        
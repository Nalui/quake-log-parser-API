from flask import abort
import json
from domain.game import Game

def find_game(games, game_number):
    try:
        return games[game_number - 1]
    except IndexError or AttributeError:
        abort(
            404, f"Game number {game_number} not found"
        )

def create_json_list (games):
    json_list = []
    for game in games:
        json_list.append(create_json(game))
    return json_list

def create_json (game):
    data = {}
    data["total_kills"] = game.total_kills
    data["players"] = list(game.players)
    data["kills"] = game.kills
    if game.alert_messages: 
        data["alert_messages"] = game.alert_messages
    return json.dumps({game.name : data})

def create_filled_game(game_number, total_kills, players, kills, alert_messages = []):
    game = Game(game_number)
    game.set_total_kills(total_kills)
    game.set_players(players)
    game.set_kills(kills)
    game.set_alert_messages(alert_messages)
    return game
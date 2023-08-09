from flask import abort
import json

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
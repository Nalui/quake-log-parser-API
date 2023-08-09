from flask import abort

def find_game(games, game_number):
    try:
        return games[game_number - 1]
    except IndexError or AttributeError:
        abort(
            404, f"Game number {game_number} not found"
        )
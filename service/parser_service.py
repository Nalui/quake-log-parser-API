import re
from flask import abort
from domain.game import Game
from enumeration.regex import Regex

def file_reader(file):
    try:
        log_file = open(file, "r+")
        return parser(log_file)
    except FileNotFoundError:
        abort(
            404, f"File {file} not found. Try to use 'games.log' or 'test.log'"
        )

def parser(log_file):
    game_number = 0
    in_game = False
    games = []
    game = Game(0)

    for row in log_file:
        if re.match(Regex.INIT_GAME.value, row):
            if in_game:
                game.alert_messages.append("The game did not shut down properly.")
                games.append(game)
            game_number += 1
            game = Game(game_number)
            in_game = True
        elif in_game:
            if re.match(Regex.NEW_PLAYER.value, row):
                player = re.split("\\\\", row)
                game.add_player(player[1]) 
            elif re.match(Regex.NEW_KILL.value, row):
                killer_re = re.search(Regex.KILLER.value, row)
                if(killer_re): 
                    killer = killer_re.group(1)
                    if re.fullmatch(killer, Regex.WORLD.value):
                        killed_re = re.search(Regex.KILLED.value, row)
                        if(killed_re):
                            killed = killed_re.group(1)
                            game.add_world_kill(killed)
                        else:
                          game.alert_messages.append("Unable to find killed.")  
                    else: 
                        game.add_player_kill(killer)
                else:
                    game.alert_messages.append("Unable to find killer.")
            elif re.match(Regex.END_GAME.value, row):
                games.append(game)
                in_game = False

    return games

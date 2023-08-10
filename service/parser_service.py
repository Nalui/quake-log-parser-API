import re
from domain.game import Game
from enumeration.regex import Regex

def file_reader(file):
    log_file = open(file, "r+")
    return parser(log_file)

def parser(log_file):
    game_number = 0
    in_game = False
    games = []

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
                killer = re.search(Regex.KILLER.value, row).group(1)
                if re.fullmatch(killer, Regex.WORLD.value):
                    killed = re.search(Regex.KILLED.value, row).group(1)
                    try:
                        game.add_world_kill(killed)
                    except KeyError:
                        game.alert_messages.append(f"Player {killed} is not in players set and therefore cannot be killed.")
                else: 
                    try:
                        game.add_player_kill(killer)
                    except KeyError:
                        game.alert_messages.append(f"Player {killed} is not in players set and therefore cannot kill.")

            elif re.match(Regex.END_GAME.value, row):
                games.append(game)
                in_game = False

    return games
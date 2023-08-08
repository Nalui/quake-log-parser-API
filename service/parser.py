import re
from domain.game import Game
import json

def file_reader(file):
    log_file = open(file, "r+")

    init_game_regex = "\\s*\\d{1,2}:\\d{2}\\s*(InitGame)\\w*"
    new_player_regex = "\\s*\\d{1,2}:\\d{2}\\s*(ClientUserinfoChanged)\\w*"
    new_kill_regex = "\\s*\\d{1,2}:\\d{2}\\s*(Kill)\\w*"
    end_game_regex = "\\s*\\d{1,2}:\\d{2}\\s*(ShutdownGame)\\w*"
    killer_regex = "Kill:\\s*\\d*\\s*\\d*\\s*\\d*:\\s*(.*) killed"
    killed_regex = 'killed\\s*(.*) by'
    world_regex = "<world>"

    game_number = 0
    games = []

    for row in log_file:
        if re.match(init_game_regex, row):
            game_number += 1
            game = Game(game_number)
            in_game = True
        elif re.match(new_player_regex, row):
            player = re.split("\\\\", row)
            game.set_player(player[1]) 
        elif re.match(new_kill_regex, row):
            killer = re.search(killer_regex, row).group(1)
            if re.fullmatch(killer, world_regex):
                killed = re.search(killed_regex, row).group(1)
                game.add_world_kill(killed)
            else: 
                game.add_player_kill(killer)
        elif re.match(end_game_regex, row):
            games.append(json.dumps(game.__dict__, default=list))
    return games

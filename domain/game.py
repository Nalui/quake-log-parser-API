class Game (): 
    def __init__(self, number):
        self.name = f"game_{number}"
        self.total_kills = 0  
        self.players = set() 
        self.kills = {}
        self.alert_messages = [] 
    
    def __repr__(self):
        return f"""User(name={repr(self.name)}, total_kills={repr(self.total_kills)}), players={repr(self.players)}), kills={repr(self.kills)}, alert_messages={repr(self.alert_messages)}"""
    
    def set_total_kills(self, total_kills):
        self.total_kills = total_kills

    def set_players(self, players):
        self.players = players
        
    def set_kills(self, kills):
        self.kills = kills

    def set_alert_messages(self, alert_messages):
        self.alert_messages = alert_messages        
    
    def add_player(self, player):
        self.players.add(player)
        self.kills.setdefault(player, 0)

    def add_player_kill(self, player, line = None):
        try:
            self.kills[player] +=1
            self.total_kills += 1
        except KeyError:
            self.alert_messages.append(f"Line {line}: Player {player} is not in players set and therefore cannot kill.")

    
    def add_world_kill(self, player, line = None):
        try:
            self.kills[player] -=1
            self.total_kills += 1
        except KeyError:
            self.alert_messages.append(f"Line {line}: Player {player} is not in players set and therefore cannot be killed.")

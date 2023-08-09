class Game (): 
    def __init__(self, number):
        self.name = f"game_{number}"
        self.total_kills = 0  
        self.players = set() 
        self.kills = {}
        self.alert_messages = [] 
        
    def set_player(self, player):
        self.players.add(player)
        self.kills.setdefault(player, 0)

    def add_player_kill(self, player):
        self.kills[player] +=1
        self.total_kills += 1
    
    def add_world_kill(self, player):
        self.kills[player] -=1
        self.total_kills += 1
    
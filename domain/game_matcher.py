from .game import Game

class Game_matcher:
    expected: Game

    def __init__(self, expected):
        self.expected = expected

    def __repr__(self):
        return repr(self.expected)

    def __eq__(self, other):
        return self.expected.name == other.name and \
               self.expected.total_kills == other.total_kills and \
               self.expected.players == other.players and \
               self.expected.kills == other.kills and \
               self.expected.alert_messages == other.alert_messages
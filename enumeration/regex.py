from enum import Enum

class Regex(Enum):
    INIT_GAME = "\\s*\\d{1,2}:\\d{2}\\s*(InitGame)\\w*"
    NEW_PLAYER = "\\s*\\d{1,2}:\\d{2}\\s*(ClientUserinfoChanged)\\w*"
    NEW_KILL = "\\s*\\d{1,2}:\\d{2}\\s*(Kill)\\w*"
    END_GAME = "\\s*\\d{1,2}:\\d{2}\\s*(ShutdownGame)\\w*"
    KILLER = "Kill:\\s*\\d*\\s*\\d*\\s*\\d*:\\s*(.*) killed"
    KILLED = "killed\\s*(.*) by"
    WORLD = "<world>"
from service.parser import file_reader

def list_all():
    games = file_reader("test.log")
    return games
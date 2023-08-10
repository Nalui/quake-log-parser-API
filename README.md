# quake-log-parser-API

## Description
A RESTful API to parse and consult quake 3 arena log files.

## Dependencies
- Python (developed with 3.9.6)
- Flask
- connexion

## Running the API
After installing dependencies, run the app by entering its folder and typing:
```
py -m app
```
in windows or
```
python -m app
```
in linux

**Calling routes**

List all endpoint:
- http://localhost:5000/api/games?file_name=games.log
  
Where file_name is the name of the .log file to be read (needs to save the .log file in the project)


Get game endpoint:
- http://localhost:5000/api/game?file_name=games.log&game_number=1
  
Where file_name is the name of the .log file to be read (needs to save new files in the project)
And game_number is the number of the game in occurence order

**Swagger:** http://localhost:5000/api/ui/#/Games

## Running the tests
```
py -m unittest
```
in windows or
```
python -m unittest
```
in linux

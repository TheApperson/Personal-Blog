import random
from flask_app.controllers import users

games = 0

#adds a global counter for number of games played
def add_game():
    global games
    games += 1
    return games

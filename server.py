from flask import Flask
from random import random
import json
import os, random

def get_random_line():
    total_bytes = os.stat("data.txt").st_size
    random_point = random.randint(0, total_bytes)
    file = open("data.txt")
    file.seek(random_point)
    file.readline() # skip this line to clear the partial line
    return file.readline()

number_of_players = 0
app = Flask(__name__)
ans = get_random_line()


def __addPlayer():
    global number_of_players
    if number_of_players < 2:
        number_of_players += 1
        return ans
    else:
        return "game is already started"

@app.route("/start")
def add_player():
    ret = __addPlayer()
    return ret


def __playTurn():
    pass


@app.route("/play/<string:player_num>")
def play_turn(player_num):
    ans = __playTurn(player_num)
    return


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def getMember(name):
    return name


if __name__ == "__main__":
    app.run()
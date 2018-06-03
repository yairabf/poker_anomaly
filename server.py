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

app = Flask(__name__)
number_of_players = 0
pot = 0
is_raised = False
raised = 0
current_player = 0

def __playTurn(player_num,task,bet):
    global current_player
    global put
    global raised
    if(current_player == player_num):
        if(task==1):
            if(raised == 0):
                current_player = (current_player + 1) %2
        elif(task==2):
            put =+ raised
            raised = bet
    pass

def __addPlayer():
    global number_of_players
    if number_of_players < 2:
        number_of_players += 1
        return get_random_line()
    else:
        return "game is already started"


@app.route("/start")
def add_player():
    ret = __addPlayer()
    return ret


@app.route("/play/<string:player_num><int:task>")
def play_turn(player_num,task):
    ans = __playTurn(player_num,task)
    return


@app.route("/show")
def members():
    global pot
    return str(pot)


@app.route("/members/<string:name>/")
def getMember(name):
    return name


if __name__ == "__main__":
    app.run()
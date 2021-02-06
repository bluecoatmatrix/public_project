import flask
from flask import jsonify
from flask import request
from hanoi import Hanoi

app = flask.Flask(__name__)
app.config["DEBUG"] = True

games = [None]

@app.route('/hanoi/create', methods=['GET'])
def create_game():
    try:
        game = Hanoi()
        games[0] = game
        return jsonify(Message='Game created'), 200
    except Exception as e:
        return jsonify(Message='Fail to create game, {}'.format(e)), 201


@app.route('/hanoi/state', methods=['GET'])
def get_state():
    try:
        return games[0].getState(), 200
    except Exception as e:
        return jsonify(Message="Fail to get state or game needs to be created first, {}".format(e)), 201

@app.route('/hanoi/win', methods=['GET'])
def is_win():
    try:
        if(games[0].isWin()):
            return jsonify(Message="You are winner!!"), 200
        else:
            return jsonify(Message="You are not won yet!!"), 200
    except Exception as e:
        return jsonify(Message="Fail to check winning or game needs to be created first!"), 201

@app.route('/hanoi/move', methods=['PUT'])
def game_move():
    if(request.args.get('source') == None or request.args.get('source') == ''):
        return jsonify(Message='Please provide source rob index!'), 201
    if(request.args.get('target') == None or request.args.get('target')== ''):
        return jsonify(Message='Please provide target rob index!'), 201
    source = int(request.args.get('source'))
    target = int(request.args.get('target'))
    try:
        games[0].move(source, target)
        return jsonify(Message="Successfully moved"), 200
    except Exception as e:
        return jsonify(Message="Fail to move, {}".format(e)), 201

if __name__ == '__main__':
    app.run()
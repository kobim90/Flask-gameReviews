import ast
import flask
from flask import Blueprint, request
import json
from DBmodules import *
from flask_cors import CORS, cross_origin

login = Blueprint('login', __name__)
originPathGames = "/login"


def convert_data_dict(data):
    dict_str = data.decode("UTF-8")
    return ast.literal_eval(dict_str)


@login.route(f'{originPathGames}', methods=['POST'])
@cross_origin(supports_credentials=True)
def post_login():
    username = request.data
    my_data = convert_data_dict(username)
    user = Users.objects(username=my_data['username'])
    res_data = {
        'userID': str(user[0].id),
        'username': user[0].username,
        'img': user[0].img,
        'admin': user[0].isAdmin,
        'gameID': [str(gameId.id) for gameId in user[0].favorite_games]
    }
    if len(user):
        res = flask.make_response({'data': res_data})
        res.set_cookie('user', json.dumps(res_data, separators=(',', ':')))
        return res, 200
    else:
        return flask.jsonify({'error': 'username or password incorrect'})


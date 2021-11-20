import flask
from flask import Blueprint, request
import json
from DBmodules import *
from flask_cors import CORS, cross_origin
from routes.games import card_game
from routes.login import convert_data_dict

users = Blueprint('users', __name__)
originPathGames = "/users"


def auth_user(func):
    def wrapper(*args, **kwargs):
        cookie = json.loads(request.cookies.get('user'))
        user = Users.objects(id=cookie['userID'])
        if len(user):
            return func(*args, **kwargs)
        else:
            return {'msg': "NOT Authenticated"}

    return wrapper


def cookie_data():
    cookie = request.cookies.get('user')
    user_client_data = json.loads(cookie)
    return user_client_data


@auth_user
@users.route(f'{originPathGames}/games')
@cross_origin(supports_credentials=True)
def get_user_games():
    user_client_data = cookie_data()
    user_games = Users.objects(id=user_client_data['userID'])
    result = []
    for game in user_games[0].favorite_games:
        result.append(card_game(game))

    return flask.jsonify(result)


@auth_user
@users.route(f'{originPathGames}/scores')
@cross_origin(supports_credentials=True)
def get_user_scores():
    cookie = cookie_data()
    reviews = Reviews.objects(userId=cookie['userID'])
    result = {'lables': [review.gameId.gameName for review in reviews],
              'userScores': [review.score for review in reviews],
              'avgScores': [Reviews.objects(gameId=game.gameId).average('score') for game in reviews]}
    # reviews = Reviews.objects(gameId__in=user_games)
    return flask.jsonify(result)


@auth_user
@users.route(f'{originPathGames}/profile')
@cross_origin(supports_credentials=True)
def get_user_profile():
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID'])
    result = {
        'user': [],
        'genres': [],
        'reviews': [],
        'games': []
    }
    result['user'].append({
        'userID': str(user[0].id),
        'username': user[0].username,
        'email': user[0].email,
        'img': user[0].img
    })
    result['genres'] = [{'genreID': str(genre.id), 'genreName': genre.genreName} for genre in user[0].favorite_genres]
    result['reviews'] = [{'gameID': str(review.gameId.id), 'reviewID': str(review.id)} for review in
                         Reviews.objects(userId=user[0])]
    result['games'] = [card_game(game) for game in user[0].favorite_games]

    return flask.jsonify(result)


@auth_user
@users.route(f'{originPathGames}/favorite')
@cross_origin(supports_credentials=True)
def user_favorite_games():
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID'])
    result = [str(game.id) for game in user[0].favorite_games]
    return flask.jsonify(result)


@auth_user
@users.route(f'{originPathGames}/username')
@cross_origin(supports_credentials=True)
def get_user_by_username():
    username = request.args.get('username')
    user = Users.objects(username=username)
    result = []
    if len(user):
        result.append({'userID': str(user[0].id)})
    return flask.jsonify(result)


@auth_user
@users.route(f'{originPathGames}/search')
@cross_origin(supports_credentials=True)
def get_user_searched_games():
    param = request.args.get('searchParam')
    searchBy = request.args.get('searchBy')
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID'])
    gameList = user[0].favorite_games
    result = []
    if searchBy == 'releaseDate':
        for game in gameList:
            if str(game.releaseDate.year) == param:
                result.append(card_game(game))
    else:
        for game in gameList:
            if param.lower() in game.gameName.lower():
                result.append(card_game(game))
    return flask.jsonify(result)


@auth_user
@users.route(f'{originPathGames}/addGame/<game_id>', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_game_favorite(game_id):
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID']).first()
    games = user.favorite_games
    user.favorite_games.append(Games.objects(id=game_id).first())
    user.update(set__favorite_games=games)
    return flask.jsonify([{'userID': str(user.id)}])


@auth_user
@users.route(f'{originPathGames}/addGame/<game_id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_game_favorite(game_id):
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID']).first()
    games = user.favorite_games
    index = 0
    for i in range(len(games)):
        if str(games[i].id) == game_id:
            index = i
            break
    del games[index]
    user.update(set__favorite_games=games)
    return flask.jsonify([{'userID': str(user.id)}])


@auth_user
@users.route(f'{originPathGames}/gamesToReview')
@cross_origin(supports_credentials=True)
def get_games_to_review():
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID']).first()
    games_to_review = Games.objects(id__nin=[str(game.gameId.id) for game in Reviews.objects(userId=str(user.id))])
    result = [{"gameID": str(game.id), "gameName": game.gameName} for game in games_to_review]
    return flask.jsonify(result)


@auth_user
@users.route(f'{originPathGames}/addReview', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_review():
    data = request.data
    review_data = convert_data_dict(data)
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID']).first()
    Reviews(
        userId=str(user.id),
        gameId=review_data['data']['gameID'],
        visability=lambda x: 1 if review_data['data']['visability'] == 1 else 0,
        title=review_data['data']['title'],
        body=review_data['data']['body'],
        conclusion=review_data['data']['conclusion'],
        score=review_data['data']['score'],
        tags=review_data['data']['tagID'],
    ).save()

    if review_data['data']['gameID'] not in [str(game.id) for game in user.favorite_games]:
        add_game_favorite(review_data['data']['gameID'])

    return flask.jsonify({'msg': "review added!"})


@auth_user
@users.route(f'{originPathGames}/review/<review_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_review(review_id):
    review = Reviews.objects(id=review_id).first()
    review = json.loads(review.to_json())
    review['userID'] = review['userId']['$oid']
    del review['userId']
    review['reviewID'] = review['_id']['$oid']
    del review['_id']
    review['gameID'] = review['gameId']['$oid']
    del review['gameId']
    review['tags'] = [tag['$oid'] for tag in review['tags']]
    return flask.jsonify(review)


@auth_user
@users.route(f'{originPathGames}/review/<review_id>', methods=['PUT'])
@cross_origin(supports_credentials=True)
def put_review(review_id):
    data = request.data
    review_data = convert_data_dict(data)['data']
    print(review_data)
    update_review = Reviews.objects(id=review_id).first()
    update_review.update(set__title=review_data['title'])
    update_review.update(set__body=review_data['body'])
    update_review.update(set__conclusion=review_data['conclusion'])
    update_review.update(score=review_data['score'])
    if review_data['visability'] == 1:
        update_review.update(set__visability=True)
    else:
        update_review.update(set__visability=False)
    update_review.update(set__tags=[Tags.objects(id=tag).first() for tag in review_data['tagID']])
    return flask.jsonify({'response': True})
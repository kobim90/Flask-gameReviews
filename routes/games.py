import flask
from flask import Blueprint, request
import json
from DBmodules import *
from flask_cors import CORS, cross_origin

games = Blueprint('games', __name__)
originPathGames = "/games"


def card_game(game):
    gameFinal = {
        'gameID': str(game.id),
        'gameName': game.gameName,
        'coverImg': game.coverImg,
        'publisher': game.publisher,
        'releaseDate': str(game.releaseDate.day) + "/" + str(game.releaseDate.month) + "/" + str(game.releaseDate.year),
        'platform': [{'id': str(platform.id), 'name': platform.platformName} for platform in game.platforms],
        'genre': [{'id': str(genre.id), 'name': genre.genreName} for genre in game.genres],
    }
    for key, val in game.screenshots.items():
        gameFinal[key] = val
    score = Reviews.objects(gameId=game).average('score')
    if score:
        gameFinal['score'] = score
    else:
        gameFinal['score'] = 'No Reviews'
    return gameFinal


@games.route(f'{originPathGames}')
@cross_origin(supports_credentials=True)
def get_games():
    result = []
    for game in Games.objects:
        gameFinal = card_game(game)
        result.append(gameFinal)

    return flask.jsonify(result)


@games.route(f'{originPathGames}/search')
@cross_origin(supports_credentials=True)
def get_search_results():
    param = request.args.get('searchParam')
    searchBy = request.args.get('searchBy')
    gameList = Games.objects()
    result = []
    if searchBy == 'releaseDate':
        for game in gameList:
            if str(game.releaseDate.year) == param:
                result.append(card_game(game))
    else:
        gameList = Games.objects(gameName__icontains=param)
        for game in gameList:
            result.append(card_game(game))
    return flask.jsonify(result)


@games.route(f'{originPathGames}/filteredGames')
@cross_origin(supports_credentials=True)
def get_filtered_games():
    filterGenres = request.args.getlist('genreID')
    filterPlatforms = request.args.getlist('platformID')
    gameListGenres = []
    gameListPlatforms = []
    result = []
    if filterGenres and not filterPlatforms:
        genres = Genres.objects(id__in=filterGenres)
        gameListGenres = Games.objects(genres__in=genres)
        for game in gameListGenres:
            result.append(card_game(game))
    elif filterPlatforms and not filterGenres:
        platforms = Platforms.objects(id__in=filterPlatforms)
        gameListPlatforms = Games.objects(platforms__in=platforms)
        for game in gameListPlatforms:
            result.append(card_game(game))
    elif filterGenres and filterPlatforms:
        genres = Genres.objects(id__in=filterGenres)
        gameListGenres = Games.objects(genres__in=genres)
        platforms = Platforms.objects(id__in=filterPlatforms)
        gameListPlatforms = Games.objects(platforms__in=platforms)
        test = Games.objects(platforms__in=platforms, genres__in=genres)
        for game in test:
            result.append(card_game(game))
            print(card_game(game))
    else:
        return get_games()

    return flask.jsonify(result)


@games.route(f'{originPathGames}/sortedGamesScoreDate')
@cross_origin(supports_credentials=True)
def get_game_sorted():
    sortBy = request.args.get('sort')
    direction = request.args.get('direction')
    gameList = []
    sortedGames = []

    def func(game):
        return game['score']

    if sortBy == 'releaseDate':
        if direction == "asc":
            sortedGames = Games.objects.order_by('releaseDate')[:7]
        else:
            sortedGames = Games.objects.order_by('-releaseDate')[:7]
    else:
        for game in Games.objects():
            score = Reviews.objects(gameId=game).average('score')
            if score:
                sortedGames.append({'game': game, 'score': score})
        if direction == "asc":
            sortedGames.sort(key=func)
            sortedGames = sortedGames[:7]
        else:
            sortedGames.sort(reverse=True, key=func)
            sortedGames = sortedGames[:7]
    for game in sortedGames:
        if sortBy == 'releaseDate':
            gameList.append(card_game(game))
        else:
            gameList.append(card_game(game['game']))

    return flask.jsonify(gameList)


@games.route(f'{originPathGames}/<game_id>')
@cross_origin(supports_credentials=True)
def get_all_game_details(game_id):
    game = Games.objects(id=game_id)
    result = card_game(game[0])
    result = {
        **result,
        'description': game[0].description,
        'system': game[0].systemRequirements.system,
        'processor': game[0].systemRequirements.processor,
        'memory': game[0].systemRequirements.memory,
        'graphics': game[0].systemRequirements.graphics,
        'directx': game[0].systemRequirements.directx,
        'storage': game[0].systemRequirements.storage
    }
    return flask.jsonify(result)


@games.route(f'{originPathGames}/reviews/<game_id>')
@cross_origin(supports_credentials=True)
def get_game_reviews(game_id):
    reviews = Reviews.objects(gameId=game_id, visability=True)
    reviews = json.loads(reviews.to_json())
    for i in range(len(reviews)):
        user = Users.objects(id=str(reviews[i]['userId']['$oid']))
        user_reviews = len(Reviews.objects(userId=str(user[0].id)))
        reviews[i]['username'] = user[0].username
        reviews[i]['games'] = len(user[0].favorite_games)
        reviews[i]['reviews'] = user_reviews
        reviews[i]['img'] = user[0].img
        reviews[i]['tags'] = [Tags.objects(id=tag['$oid'])[0].tagName for tag in reviews[i]['tags']]
    return flask.jsonify(reviews)

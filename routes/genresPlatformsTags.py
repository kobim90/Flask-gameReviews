import flask
from flask import Blueprint
import json
from DBmodules import *
from flask_cors import cross_origin


genresPlatformsTags = Blueprint('genresPlatformsTags', __name__)
originPathGenres = "genres"


@genresPlatformsTags.route(f'/{originPathGenres}')
@cross_origin(supports_credentials=True)
def get_genres():
    result = []
    for genre in Genres.objects:
        genreFinal = {'id': str(genre.id), 'Name': genre.genreName}
        result.append(genreFinal)
    return flask.jsonify(result)


@genresPlatformsTags.route(f'/{originPathGenres}/platforms')
@cross_origin(supports_credentials=True)
def get_platforms():
    result = []
    for platform in Platforms.objects:
        platformFinal = {'id': str(platform.id), 'Name': platform.platformName}
        result.append(platformFinal)
    return flask.jsonify(result)


@genresPlatformsTags.route(f'/{originPathGenres}/tags')
@cross_origin(supports_credentials=True)
def get_tags():
    result = []
    for tag in Tags.objects:
        tagFinal = {'tagID': str(tag.id), 'tagName': tag.tagName}
        result.append(tagFinal)
    return flask.jsonify(result)



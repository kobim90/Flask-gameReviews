import flask
from flask import Blueprint, request
from DBmodules import *
from flask_cors import cross_origin
from routes.users import auth_user, cookie_data
from werkzeug.utils import secure_filename
import os
import uuid

register = Blueprint('register', __name__)
originPathGames = "/register"
UPLOAD_FOLDER = 'Public/Images/users'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_img(file):
    if file and allowed_file(file.filename):
        unique_filename = str(uuid.uuid4()) + file.filename
        filename = secure_filename(unique_filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename


@auth_user
@register.route(f'{originPathGames}', methods=['POST'])
@cross_origin(supports_credentials=True)
def register_user():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    genres = request.form['genres'].split(",")
    if 'img' in request.files:
        filename = upload_img(request.files['img'])
    else:
        filename = 'avatar.png'

    Users(
        username=username,
        password=password,
        email=email,
        img=f'http://localhost:3200/{UPLOAD_FOLDER}/{filename}',
        favorite_games=[],
        favorite_genres=[Genres.objects(id=genre).first() for genre in genres],
        isAdmin=False
    ).save()

    return flask.jsonify({'data': True})


@register.route(f'{originPathGames}', methods=['PUT'])
@cross_origin(supports_credentials=True)
def update_user():
    cookie = cookie_data()
    user = Users.objects(id=cookie['userID'])
    email = request.form['email']
    genres = request.form['genres'].split(",")
    if 'img' in request.files:
        filename = upload_img(request.files['img'])
        user.update(img=f'http://localhost:3200/{UPLOAD_FOLDER}/{filename}')

    user.update(email=email)
    user.update(favorite_genres=[Genres.objects(id=genre).first() for genre in genres])

    return flask.jsonify({'data': True})


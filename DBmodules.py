from mongoengine import *
import json


class Platforms(Document):
    platformName = StringField(required=True, max_length=200)


class Genres(Document):
    genreName = StringField(required=True, max_length=200)


class Tags(Document):
    tagName = StringField(required=True, max_length=200)


class SystemRequirements(EmbeddedDocument):
    system = StringField(required=True, max_length=200)
    processor = StringField(required=True, max_length=200)
    memory = StringField(required=True, max_length=100)
    graphics = StringField(required=True, max_length=200)
    directx = StringField(required=True, max_length=100)
    storage = StringField(required=True, max_length=100)


class Games(Document):
    gameName = StringField(required=True, max_length=200)
    publisher = StringField(required=True, max_length=200)
    releaseDate = DateField(required=True)
    description = StringField(required=True)
    coverImg = StringField(required=True)
    systemRequirements = EmbeddedDocumentField(SystemRequirements)
    genres = ListField(ReferenceField('Genres'), DBRef=True)
    screenshots = DictField(required=True)
    platforms = ListField(ReferenceField('Platforms'), DBRef=True)



class Users(Document):
    username = StringField(required=True, max_length=20)
    password = StringField(required=True, max_length=20)
    email = StringField(required=True, max_length=40)
    img = StringField(required=True)
    favorite_genres = ListField(ReferenceField('Genres'), DBRef=True)
    favorite_games = ListField(ReferenceField('Games'), DBRef=True)
    isAdmin = BooleanField(required=True, default=False)

    # @classmethod
    # def add_to_favorite_games(cls, game_id):
    #     user = Users.objects(id=cls.id)
    #     print(games)
    #     # games.append(game_id)
    #     # cls.favorite_games.update(cls, games)


class Reviews(Document):
    userId = ReferenceField('Users', DBRef=True)
    gameId = ReferenceField('Games', DBRef=True)
    visability = BooleanField(required=True, default=1)
    title = StringField(required=True, max_length=200)
    body = StringField(required=True)
    conclusion = StringField(required=True, max_length=600)
    score = IntField(required=True, max_value=10, min_value=0)
    tags = ListField(ReferenceField('Tags'), DBRef=True)

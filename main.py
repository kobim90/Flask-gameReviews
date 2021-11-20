from flask import Flask, jsonify, send_file, request, url_for, Blueprint
from DBmodules import *
from flask_cors import CORS
from routes.genresPlatformsTags import genresPlatformsTags
from routes.games import games
from routes.login import login
from routes.users import users
from routes.register import register

app = Flask(__name__, static_folder="Public")
CORS(app, supports_credentials=True, resources={
            r"/api/*": {"origins": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'
# auth = HTTPBasicAuth()
connect(host="mongodb+srv://kobim:karok12K@kobiscluster.rvdyv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# routes
app.register_blueprint(genresPlatformsTags)
app.register_blueprint(games)
app.register_blueprint(login)
app.register_blueprint(users)
app.register_blueprint(register)

if __name__ == '__main__':
    app.run(debug=True, port=3200)

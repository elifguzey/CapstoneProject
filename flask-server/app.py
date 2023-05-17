from flask import Flask, make_response, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
# from models import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a1863ba24c8ea81bb758df02'
app.json.compact = False

app = Flask(__name__)

migrate = Migrate(app, db)
cors = CORS(app)
db.init_app(app)
api = Api(app)




@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
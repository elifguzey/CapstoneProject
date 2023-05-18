from flask import Flask, make_response, request, session
from flask_migrate import Migrate
from config import app, api
from flask_restful import Api, Resource
from models import db, User, SavedRecipe, Recipe

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False
# app.config['SECRET_KEY'] = 'a1863ba24c8ea81bb758df02'

# db.init_app(app)
# migrate = Migrate(app, db)
# cors = CORS(app)

# api = Api(app)

@app.route('/')
def home():
    return "Hello, World!"

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5555, debug=True)

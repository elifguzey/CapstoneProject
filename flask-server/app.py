from flask import Flask, make_response, request, session
from flask_migrate import Migrate
from config import app, api
from flask_restful import Api, Resource
from models import db, User, SavedRecipe, Recipe

@app.route('/')
def home():
    return "Hello, World!"

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5555, debug=True)

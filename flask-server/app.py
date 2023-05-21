from flask import Flask, make_response, request, session, jsonify, flash
from flask_migrate import Migrate
from config import app, api
from flask_restful import Api, Resource
from models import db, User, Recipe
from config import db, app, api

@app.route('/')
def index():
    return "HomeBase API is running!"

with app.app_context():
    db.create_all()

class Home(Resource):
    def get(self):
        return "Welcome to TastyBites"

api.add_resource(Home, '/home')

class Users(Resource):
    def get(self):
        user_list = []
        for u in User.query.all():
            u_dict = {
                'id': u.id,
                'username': u.username,
                'email': u.email,
                'password': u._password_hash
            }
            user_list.append(u_dict)
        return make_response(user_list, 200)

    # def post (self):
    #     data = request.get_json()
    #     try:
    #         newUser = User(
    #             username = data['username'],
    #             email = data['email'],
    #             password = data["password"],
    #         )

    #         db.session.add(newUser)
    #         db.session.commit()
    #         return make_response (newUser.to_dict(), 200)
    #     except Exception as e:
    #         # db.session.rollback()
    #         return make_response({'error': f'{repr(e)}'}, 422)

api.add_resource(Users, '/users')

class Recipes(Resource):
    def get(self):
        recipe_list = []
        for r in Recipe.query.all():
            r_dict = {
                'id': r.id,
                'title': r.title,
                'image_url': r.image_url,
                'instructions': r.instructions
            }
            recipe_list.append(r_dict)
        return make_response(recipe_list, 200)

api.add_resource(Recipes, '/recipes')

class RecipesById(Resource):
    def get(self, id):
        r_inst = Recipe.query.filter(Recipe.id == id).first()
        if r_inst == None:
            return make_response('Recipe not found', 404)
        else:
           recipe_instance_dict = {
                'id': r_inst.id,
                'title': r_inst.title,
                'image_url': r_inst.image_url,
                'instructions': r_inst.instructions
            }
        return make_response(recipe_instance_dict, 200)
        
api.add_resource(RecipesById, '/recipes/<int:id>')


# class SavedRecipes(Resource):
#     def get(self):
#         recipe_list = []
#         for r in Recipe.query.all():
#             r_dict = {
#                 'id': r.id
#             }
#             recipe_list.append(r_dict)
#         return make_response(recipe_list, 200)

# api.add_resource(SavedRecipes, '/saved_recipes')

# class Signup(Resource):
#     def post(self):
#         email = request.json['email']
#         username = request.json['username']
#         password = request.json['password']

#         if email in [u.email for u in User.query.all()]:
#             flash('Username already taken!')
#             return jsonify({"error": "There is already a user with this name"}), 409

#         hashed_password = bcrypt.generate_password_hash(password)

#         new_user = User(
#             email = email,
#             _password_hash = hashed_password,
#             username = username
#         )

#         db.session.add(new_user)
#         db.session.commit()

#         return new_user.to_dict()

# class Login(Resource):
#     def post(self):
#         email = request.json['email']
#         password = request.json['password']

#         user = User.query.filter_by(email = email).first()

#         if not user.authenticate(password):
#             session['user_id'] = user.id
#             session.permanent = True
#             return user.to_dict()
#         elif user is None:
#             return {'error': 'Invalid email or password'}, 404
#         else:
#             return {'error': 'Invalid email or password'}, 404


# class Logout(Resource):
#     def delete(self):
#         session.get('user_id') == None
#         return make_response({}, 204)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

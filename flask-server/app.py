from flask import Flask, make_response, request, session, jsonify, flash
from flask_migrate import Migrate
from config import app, api
from flask_restful import Api, Resource
from models import db, User, Recipe, SavedRecipe
from config import db, app, api

@app.route('/')
def homepage():
    return "homepage"

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

    def post (self):
        data = request.get_json()
        try:
            newUser = User(
                username = data['username'],
                password = data["password"],
            )

            db.session.add(newUser)
            db.session.commit()
            return make_response (newUser.to_dict(), 200)
        except Exception as e:
            return make_response({'error': f'{repr(e)}'}, 422)

api.add_resource(Users, '/users')

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(user.to_dict(), 200)
        else:
            return make_response({'error': 'User not found'}, 404)
        
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(user.to_dict(), 200)
        else:
            return make_response({'error': 'User not found'}, 404)
        
    def patch(self, id):
        data = request.get_json()
        user = User.query.filter_by(id=id).first()
        if user:
            if 'username' in data:
                user.username = data['username']
            if 'email' in data:
                user.email = data['email']
            if 'password' in data:
                user.password = data['password']
            db.session.commit()
            return make_response(user.to_dict(), 200)
        else:
            return make_response({'error': 'User not found'}, 404)

api.add_resource(UserById, '/users/<int:id>')

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


class SavedRecipes(Resource):
    def get(self):
        recipe_list = []
        for r in Recipe.query.all():
            r_dict = {
                'id': r.id
            }
            recipe_list.append(r_dict)
        return make_response(recipe_list, 200)

api.add_resource(SavedRecipes, '/saved_recipes')

class SavedRecipesById(Resource):
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

# class Login(Resource):
#     def post(self):
#         data = request.get_json()
#         email = data['email']
#         password = data['password']
#         user = User.query.filter_by(email=email).first()
#         if user:
#             if (user.password == password):
#                 session['user_id'] = user.id
                
#                 return make_response(user.to_dict(), 200)
#         return make_response({'error': '401 Unauthorized'}, 401)
# api.add_resource(Login, '/login')
class Login(Resource):
    def post(self):
        request_json = request.get_json()

        username = request_json.get("username")
        password = request_json.get("password")

        user = User.query.filter_by(username = username).first()
            

        if user:
            if user.authenticate(password):
                print(user.id)
                session['user_id'] = user.id
                return user.to_dict(), 200
        else:
                return {'error': 'Invalid Credentials'}, 401
        
api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {'message': '204: No Content'}, 204
api.add_resource(Logout, '/logout')


class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401


api.add_resource(CheckSession, '/check_session')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

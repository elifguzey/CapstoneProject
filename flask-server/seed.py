# from faker import Faker
# import csv
# from config import db
# from app import app
# from models import db, User, Recipe, SavedRecipe

# fake = Faker()

# def create_users():
#     for _ in range(10):  # Generate 10 users
#         user = User(
#             email=fake.email(),
#             username=fake.user_name(),
#             password_hash=fake.password(),
#         )
#         db.session.add(user)
#     db.session.commit()


# def create_recipes():
#     users = User.query.all()
#     for _ in range(20):  # Generate 20 recipes
#         recipe = Recipe(
#             title=fake.sentence(),
#             instructions=fake.paragraph(),
#             cooking_time=fake.random_int(min=1, max=60),
#             user_id=fake.random_element(users).id
#         )
#         db.session.add(recipe)
#     db.session.commit()


# def create_saved_recipes():
#     users = User.query.all()
#     recipes = Recipe.query.all()
#     for _ in range(30):  # Generate 30 saved recipes
#         saved_recipe = SavedRecipe(
#             user_id=fake.random_element(users).id,
#             recipe_id=fake.random_element(recipes).id
#         )
#         db.session.add(saved_recipe)
#     db.session.commit()


# if __name__ == '__main__':
#     with app.app_context():
#         create_users()
#         create_recipes()
#         create_saved_recipes()


# print("Seeding complete!")

# scotss
# from flask import Flask
# from config import db
# from app import app
# from models import db, User, Recipe, SavedRecipe
# from app import app


# if __name__ == '__main__':
#     with app.app_context():
#         print("Starting seed...")
#         # Delete existing records
#         Recipe.query.delete()
#         # Create coaches
#         recipe1 = Recipe(fname="Joey", lname="Beef", email="joey@beef.com", phone="123-456-7890", password="test")
#         recipe2 = Recipe(fname="Robert", lname="Tringali", email="robert@tringali.com", phone="123-123-1234", password="test")
#         db.session.add(recipe1)
#         db.session.add(recipe2)
#         db.session.commit()
#         print("Seeding complete!")

from app import app
from models import User, Recipe, SavedRecipe
from config import db

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")

        User.query.delete()
        Recipe.query.delete()
        SavedRecipe.query.delete()

#################### PIECES #######################

        u1 = User(email= 'john.doe@gmail.com', username='johndoe', password_hash='12345678')
        u2 = User(email= 'jane.doe@hotmail.com', username='janedoe', password_hash='12345678')
        u3 = User(email= 'alexander.johnson@aol.com', username='alexanderjohnson', password_hash='12345678')
        u4 = User(email= 'emily.wilson@gmail.com', username='emilywilson', password_hash='12345678')
        u5 = User(email= 'david.miller@gmail.com', username='davidmiller', password_hash='12345678')

        users = [u1, u2, u3, u4, u5]

        db.session.add_all(users)
        db.session.commit()


        r1 = Recipe(title= 'Spaghetti', instructions= 'Make spaghetti', cooking_time= 30, user_id= 1)   
        r2 = Recipe(title= 'Pizza', instructions= 'Make pizza', cooking_time= 30, user_id= 1)
        r3 = Recipe(title= 'Burger', instructions= 'Make burger', cooking_time= 30, user_id= 1)
        r4 = Recipe(title= 'Chicken', instructions= 'Make chicken', cooking_time= 30, user_id= 1)
        r5 = Recipe(title= 'Fish', instructions= 'Make fish', cooking_time= 30, user_id= 1)

        recipes = [r1, r2, r3, r4, r5]
        db.session.add_all(recipes) 
        db.session.commit()

        sr1 = SavedRecipe(user_id= 1, recipe_id= 1)
        sr2 = SavedRecipe(user_id= 1, recipe_id= 2)
        sr3 = SavedRecipe(user_id= 1, recipe_id= 3)
        sr4 = SavedRecipe(user_id= 1, recipe_id= 4)
        sr5 = SavedRecipe(user_id= 1, recipe_id= 5)

        saved_recipes = [sr1, sr2, sr3, sr4, sr5]
        db.session.add_all(saved_recipes)
        db.session.commit()
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


from flask import Flask
from config import db
from app import app
from models import db, User, Recipe, SavedRecipe
from app import app


if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Delete existing records
        Recipe.query.delete()
        # Create coaches
        recipe1 = Recipe(fname="Joey", lname="Beef", email="joey@beef.com", phone="123-456-7890", password="test")
        recipe2 = Recipe(fname="Robert", lname="Tringali", email="robert@tringali.com", phone="123-123-1234", password="test")
        db.session.add(recipe1)
        db.session.add(recipe2)
        db.session.commit()
        print("Seeding complete!")
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


        r1 = Recipe(title= 'Manti', instructions= 'To make Turkish Manti, begin by preparing the dough. In a mixing bowl, combine all-purpose flour, salt, and water, kneading until a smooth and elastic dough is formed. Let it rest for about 30 minutes. Meanwhile, create the filling by mixing ground beef or lamb, finely chopped onion, minced garlic, salt, and pepper in a separate bowl. Roll out the dough on a floured surface, then cut it into small squares or circles. Take each piece of dough, place a small amount of the meat filling in the center, and fold the edges to form dumplings. Boil the manti in salted water until they float to the surface. In a serving dish, combine plain yogurt, minced garlic, and salt to prepare the yogurt sauce. In a separate saucepan, melt butter and add paprika and dried mint to create the spiced butter sauce. Serve the cooked manti in individual bowls, spooning yogurt sauce over them, and drizzling the spiced butter sauce on top. Optionally, garnish with dried mint or sumac. Enjoy the delightful combination of tender dumplings, creamy yogurt sauce, and fragrant spiced butter in this Turkish Manti dish.', cooking_time= '45 mins', image_url= 'https://www.panningtheglobe.com/wp-content/uploads/2013/11/turkish-manti-web-final.jpg', user_id= 1)   
        r2 = Recipe(title= 'Margherita pizza', instructions= 'To make a Margherita pizza at home, preheat your oven to the highest temperature and place a pizza stone or baking sheet inside to heat up. Roll out your pizza dough into a thin round shape and transfer it to a piece of parchment paper. Spread a thin layer of tomato sauce or crushed tomatoes on the dough, leaving a border around the edges. Tear or slice fresh mozzarella cheese and distribute it evenly over the sauce. Season with salt and pepper, and drizzle a bit of olive oil over the pizza. Carefully transfer the pizza on the parchment paper to the preheated oven. Bake for around 10-12 minutes until the crust turns golden brown and the cheese is bubbly and slightly browned. Once out of the oven, sprinkle torn fresh basil leaves over the hot pizza. Allow it to cool for a moment before slicing and serving', cooking_time= '35 mins', image_url= 'https://cookieandkate.com/images/2021/07/margherita-pizza-recipe-1-2.jpg', user_id= 1)
        r3 = Recipe(title= 'CheeseBurger', instructions= 'A cheeseburger is a classic and mouthwatering sandwich that can be easily made at home. Start by shaping ground beef into patties, being careful not to overwork the meat. Season the patties with salt and pepper, then cook them on a preheated pan for about 4-5 minutes per side, or until they reach your desired level of doneness. During the last minute of cooking, add a slice of cheese on top of each patty to let it melt. While the patties rest, lightly toast the hamburger buns. To assemble the cheeseburgers, place a patty on the bottom half of a toasted bun and top it with your favorite toppings like lettuce, tomato, onion, and pickles. Spread condiments such as ketchup, mustard, or mayonnaise on the top half of the bun and place it on top of the assembled ingredients. Serve the cheeseburgers immediately and savor the flavorful combination of juicy beef, melted cheese, and delightful toppings', cooking_time= '25 mins', image_url= 'https://s23209.pcdn.co/wp-content/uploads/2022/07/220602_DD_The-Best-Ever-Cheeseburger_267.jpg', user_id= 1)
        r4 = Recipe(title= 'Chicken Parmigiana', instructions= 'Chicken Parmigiana is a classic Italian dish that features breaded and fried chicken cutlets topped with marinara sauce and melted cheese. To make Chicken Parmigiana, start by flattening chicken breasts to an even thickness. Dip the chicken into beaten eggs, then coat it in a mixture of breadcrumbs, grated Parmesan cheese, and Italian herbs. Fry the breaded chicken in a skillet until golden and cooked through. Next, spread marinara sauce over the chicken cutlets and top them with slices of mozzarella cheese. Place the chicken under the broiler until the cheese is melted and bubbly. Sprinkle with fresh basil leaves and serve the Chicken Parmigiana over spaghetti or with a side of garlic bread. The result is a flavorful and comforting dish thats sure to satisfy your Italian food cravings', cooking_time= '30 mins', image_url = 'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2019/7/11/0/FNK_the-best-chicken-parmesan_H_s4x3.jpg.rend.hgtvcom.616.462.suffix/1562853897238.jpeg', user_id= 1)
        r5 = Recipe(title= 'Lemon Butter Fish', instructions= 'Lemon Butter Fish is a delicious and easy-to-make dish that combines the tangy freshness of lemon with the richness of butter. To prepare it, season fish fillets with salt and pepper, then sauté them in a skillet with melted butter and minced garlic until they are cooked through and flaky. Squeeze fresh lemon juice over the fish while cooking to infuse it with a zesty flavor. Once done, transfer the fish to a plate and pour the flavorful lemon butter sauce from the skillet on top. You can garnish with fresh parsley for added freshness. Serve this delightful dish with your choice of sides like steamed vegetables, rice, or a side salad, and enjoy a quick and tasty meal', cooking_time= '20 mins', image_url= 'https://www.chewoutloud.com/wp-content/uploads/2017/06/easy-lemon-butter-fish-0.jpg', user_id= 1)

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
from config import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from datetime import date, datetime, timedelta


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serializer_rules = ('-created_at', '-updated_at', '-saved_recipes')

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique= True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    saved_recipes = db.relationship('SavedRecipe', backref = 'user', cascade= 'all, delete, delete-orphan')
    recipes = association_proxy('saved_recipes', 'recipe')

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode( 'utf-8')
        )
    
    @validates('_password_hash')
    def validate_password(self, key, value):
        if len(value) < 8:
            raise ValueError('Password Must be at least 8 Characters')
        return value
   
    @validates('username')
    def validate_nullables(self, key, value):
        if value is None:
            raise ValueError(f'{key} is required')
        return value

    @validates('email')
    def validate_email(self, key, value):
        email = User.query.all()
        if value in  email:
            raise ValueError('email already exists')
        if not value:
            raise ValueError('email is required')
        return value

class Recipe(db.Model, SerializerMixin):
    __tablename__ ='recipes'

    serializer_rules = ('-created_at', '-updated_at', '-saved_recipes')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    cooking_time = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # this from chatgpt ^
    
    saved_recipes = db.relationship('SavedRecipe', backref = 'recipe')
    users = association_proxy('saved_recipes', 'user')


class SavedRecipe(db.Model, SerializerMixin):
    __tablename__ ='saved_recipes'

    serializer_rules = ('-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)

    # @validates('recipe_id')
    # def validate_recipe_id(self, key, recipe_id):
    #     recipe = Recipe.query.filter_by(id=recipe_id).first()
    #     if recipe is None:
    #         raise ValueError('Recipe does not exist')
    #     return recipe_id
    
    # @validates('user_id')
    # def validate_user_id(self, key, user_id):
    #     user = User.query.filter_by(id=user_id).first()
    #     if user is None:
    #         raise ValueError('User does not exist')
    #     return user_id


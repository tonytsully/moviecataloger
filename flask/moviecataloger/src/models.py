from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


class Genres(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    movies_id =  db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    profiles_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)

    def __init__(self, title: str):
        self.title = title
    

    def serialize(self):
            return {
                'id': self.id,
                'title': self.title,
                'movies_id': self.movies_id,
                'profiles_id': self.profiles_id     
            }    

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    profiles_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)

    def __init__(self, title: str, year: int, length: int, profiles_id: int):
        self.title = title
        self.year = year
        self.length = length
        self.profiles_id = profiles_id
    

    def serialize(self):
            return {
                'id': self.id,
                'title': self.title,
                'year': self.year,
                'length': self.length     
            }                


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    
    def __init__(self, name: str):
        self.name = name

    def serialize(self):
            return {
                'id': self.id,
                'name': self.name,     
            }             


class UserAccount(db.Model):
    __tablename__ = 'user_account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    profiles_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)

    def __init__(self, username: str, password: str, profiles_id: int):
        self.username = username
        self.password = password
        self.profiles_id = profiles_id

    def serialize(self):
            return {
                'id': self.id,
                'username': self.username     
            }    
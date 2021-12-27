"""
Populate twitter database with fake data using the SQLAlchemy ORM.
"""

import random
import string
import hashlib
import secrets
from faker import Faker
from moviecataloger.src.models import UserAccount, Genres, Movies, db, Profiles
from moviecataloger.src import create_app

USER_COUNT = 50
MOVIE_TITLE_COUNT = 100
GENRE_TITILE_COUNT = 400
PROFILE_COUNT = 100

assert GENRE_TITILE_COUNT <= (USER_COUNT * MOVIE_TITLE_COUNT)


def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&', # valid pw characters
            k=random.randint(8, 15) # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


def truncate_tables():
    """Delete all rows from database tables"""
    #db.session.execute(likes_table.delete())
    Movies.query.delete()
    UserAccount.query.delete()
    Profiles.query.delete()
    db.session.commit()


def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()

    last_profile = None  # save last user
    for _ in range(PROFILE_COUNT):
        last_profile = Profiles(
            name=fake.unique.first_name().lower() + str(random.randint(1,150)),
            
        )
        db.session.add(last_profile)

    db.session.commit()

    last_user = None  # save last user
    for _ in range(USER_COUNT):
        last_user = UserAccount(
            username=fake.unique.first_name().lower() + str(random.randint(1,150)),
            password=random_passhash(),
            profiles_id=int(random.randint(1, 50))
        )
        db.session.add(last_user)

    # insert users
    db.session.commit()

    last_movie = None  # save last user
    for _ in range(MOVIE_TITLE_COUNT):
        last_movie = Movies(
            title=fake.unique.name().lower() + str(random.randint(1,150)),
            year=int(random.randint(1934, 2021)),
            length=int(random.randint(100, 999)),
            profiles_id=int(random.randint(1, 50))
        )
        db.session.add(last_movie)
     # insert users
    db.session.commit()

    
# run script
main()

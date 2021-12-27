from flask import Blueprint
from flask import Blueprint, jsonify, abort, request
from ..models import Movies, UserAccount, db, Profiles
import secrets
import hashlib
import random


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('user_account', __name__, url_prefix='/user_account')



@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = UserAccount.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) 
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = UserAccount.query.get_or_404(id)
    return jsonify(u.serialize())  

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len('username') < 3:
        return abort(400)
    if len('password') < 8:
        return abort(400)   
   
    u = UserAccount(
        username=request.json['username'],
        password=scramble(request.json['password']),
        profiles_id=int(random.randint(51, 100))
    )
    db.session.add(u) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(u.serialize())  


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = UserAccount.query.get_or_404(id)
    try:
        db.session.delete(u) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)   

@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    u = UserAccount.query.get_or_404(id)
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len('username') < 3:
        return abort(400)
    if len('password') < 8:
        return abort(400)   

    u.username = request.json['username']
    u.passwored = scramble(request.json['password'])
   
    try: 
        db.session.commit() 
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)         
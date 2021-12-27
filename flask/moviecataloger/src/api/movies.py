from flask import Blueprint, jsonify, abort, request
from ..models import Movies, UserAccount, db

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    movies = Movies.query.all() # ORM performs SELECT query
    result = []
    for m in movies:
        result.append(m.serialize()) # build list of Movies as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    m = Movies.query.get_or_404(id)
    return jsonify(m.serialize())



@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    m = Movies.query.get_or_404(id)
    try:
        db.session.delete(m) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)    
from flask import Blueprint, jsonify, request
from inventory.database import db_session
from inventory.models import *

bp = Blueprint('inventory', __name__)

@bp.route('/')
def index():
    return jsonify({'test': 'Hello, world'}), 201

@bp.route('/categories/get')
def get_categories():
    categories = Category.query.all()
    categories_dict = [category.to_dict() for category in categories]

    return jsonify({'objects': categories_dict}), 201

@bp.route('/categories/create', methods=['POST'])
def create_category():
    error = None
    if request.method == 'POST':
        data = request.json
        name = data['name']
        description = data['description']

        if (len(name.strip()) == 0 or len(name.strip()) > 32):
            error = 'Name is not valid'

        if (len(description.strip()) == 0 or len(description.strip()) > 128):
            error = 'Description is not valid'

        if not error:
            category = Category(name=name, description=description)
            db_session.add(category)
            db_session.commit()

            return jsonify({'message': 'successfully created new category.'}), 201
        else:
            return jsonify({'message': 'error when trying to create new category.', 'error': error}), 201

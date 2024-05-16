from flask import Blueprint, jsonify, request
from inventory.database import db_session
from inventory.models import *

bp = Blueprint('inventory', __name__)

@bp.route('/')
def index():
    return jsonify({'test': 'Hello, world'}), 201

@bp.route('/categories', methods=['GET', 'POST'])
def get_categories():
    if request.method == "GET":
        categories = Category.query.all()
        categories_dict = [category.to_dict() for category in categories]

        return jsonify({'objects': categories_dict}), 201
    
    elif request.method == "POST":
        error = None
        
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

@bp.route('/categories/<int:object_id>', methods=['GET', 'DELETE', 'PATCH'])
def get_category_details(object_id):
    if request.method == "GET":
        category = Category.query.get(object_id)

        if category:
            return jsonify({'object': category.to_dict()}), 201
        else:
            return 'Category not found', 404
        
    elif request.method == "DELETE":
        category = Category.query.get(object_id)

        if category:
            db_session.delete(category)
            db_session.commit()

            return jsonify({'message': 'success'}), 201
        else:
            return jsonify({'message': 'failed to find category'}), 400

    elif request.method == "PATCH":
        category = Category.query.get(object_id)

        if category:
            data = request.json
            name = data['name']
            description = data['description']

            category.name = name
            category.description = description

            db_session.commit()

            return jsonify({'message': 'success'}), 201
        else:
            return jsonify({'message': 'failed to find category'}), 400
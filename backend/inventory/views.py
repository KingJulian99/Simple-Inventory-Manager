from flask import Blueprint, jsonify, request
from inventory.database import db_session
from inventory.models import *
from inventory.setup import generate_random_string

bp = Blueprint('inventory', __name__)

@bp.route('/fill')
def index():
    for _ in range(5):
        category = Category(generate_random_string(), generate_random_string())
        db_session.add(category)

        supplier = Supplier(generate_random_string(), generate_random_string(), generate_random_string(),generate_random_string(),generate_random_string())
        db_session.add(supplier)

        db_session.commit()

    return jsonify({'test': 'Filled'}), 201

@bp.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    if request.method == "GET":
        suppliers = Supplier.query.all()
        suppliers_dict = [supplier.to_dict() for supplier in suppliers]

        return jsonify({'objects': suppliers_dict}), 201
    
    elif request.method == "POST":
        error = None
        
        data = request.json
        name = data['name']
        description = data['description']
        email = data['email']
        address = data['address']
        contact_number = data['number']

        if (len(name.strip()) == 0 or len(name.strip()) > 32):
            error = 'Name is not valid'

        if (len(description.strip()) == 0 or len(description.strip()) > 128):
            error = 'Description is not valid'

        if (len(email.strip()) == 0 or len(email.strip()) > 128 or email.find('@') == -1):
            error = 'Email is not valid'

        if (len(address.strip()) == 0 or len(address.strip()) > 128):
            error = 'Address is not valid'
        
        if (len(str(contact_number)) != 10):
            error = 'Contact number is not valid'

        if not error:
            supplier = Supplier(name=name, description=description, address=address, email=email, contact_number=contact_number)
            db_session.add(supplier)
            db_session.commit()

            return jsonify({'message': 'successfully created new supplier.'}), 201
        else:
            return jsonify({'message': 'error when trying to create new supplier.', 'error': error}), 201
        
@bp.route('/suppliers/<int:object_id>', methods=['GET', 'DELETE', 'PATCH'])
def supplier_details(object_id):
    if request.method == "GET":
        supplier = Supplier.query.get(object_id)

        if supplier:
            return jsonify({'object': supplier.to_dict()}), 201
        else:
            return 'Supplier not found', 404
        
    elif request.method == "DELETE":
        supplier = Supplier.query.get(object_id)

        if supplier:
            db_session.delete(supplier)
            db_session.commit()

            return jsonify({'message': 'success'}), 201
        else:
            return jsonify({'message': 'failed to find supplier'}), 400

    elif request.method == "PATCH":
        supplier = Supplier.query.get(object_id)

        if supplier:
            data = request.json
            name = data['name']
            description = data['description']

            supplier.name = name
            supplier.description = description

            db_session.commit()

            return jsonify({'message': 'success'}), 201
        else:
            return jsonify({'message': 'failed to find supplier'}), 400

@bp.route('/categories', methods=['GET', 'POST'])
def categories():
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
def category_details(object_id):
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
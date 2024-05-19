from flask import Blueprint, jsonify, request
from inventory.database import db_session
from inventory.models import *

bp = Blueprint('inventory', __name__)

@bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == "GET":
        inventory = InventoryItem.query.all()
        inventory_dict = [item.to_dict() for item in inventory]

        return jsonify({'objects': inventory_dict}), 201
    
    elif request.method == "POST":
        error = None
        
        data = request.json
        purchase_price = data['purchase_price']
        quantity = data['quantity']
        product_id = data['product_id']
        supplier_id = data['supplier_id']

        if (purchase_price < 0):
            error = 'Purchase price is not valid'

        if (quantity <= 0):
            error = 'Quantity is not valid'

        product = Product.query.get(product_id)
        if not product:
            error = 'Unable to find product'

        supplier = Supplier.query.get(supplier_id)
        if not supplier:
            error = 'Unable to find supplier'

        if not error:
            for _ in range(quantity):
                item = InventoryItem(product=product, supplier=supplier, purchase_price=purchase_price)
                db_session.add(item)

            db_session.commit()

            return jsonify({'message': 'successfully created new inventory item.'}), 201
        else:
            return jsonify({'message': 'error when trying to create new inventory item.', 'error': error}), 201
        
@bp.route('/inventory/<int:object_id>', methods=['GET', 'DELETE', 'PATCH'])
def inventory_details(object_id):
    if request.method == "GET":
        item = InventoryItem.query.get(object_id)

        if item:
            return jsonify({'object': item.to_dict()}), 201
        else:
            return 'Inventory item not found', 404
        
    elif request.method == "DELETE":
        item = InventoryItem.query.get(object_id)

        if item:
            db_session.delete(item)
            db_session.commit()

            return jsonify({'message': 'success'}), 201
        else:
            return jsonify({'message': 'failed to find inventory item'}), 400

    elif request.method == "PATCH":
        error = None

        item = InventoryItem.query.get(object_id)

        if item:
            data = request.json
            purchase_price = data['purchase_price']
            product_id = data['product_id']
            supplier_id = data['supplier_id']

            if (purchase_price < 0):
                error = 'Purchase price is not valid'

            product = Product.query.get(product_id)
            if not product:
                error = 'Unable to find product'

            supplier = Supplier.query.get(supplier_id)
            if not supplier:
                error = 'Unable to find supplier'

            if not error:
                item.purchase_price = purchase_price
                item.product = product
                item.supplier = supplier

                db_session.commit()

                return jsonify({'message': 'success'}), 201
            
            else:
                return jsonify({'error': 'failed to validate data'}), 400
            
        else:
            return jsonify({'message': 'failed to find inventory item'}), 400

@bp.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == "GET":
        products = Product.query.all()
        products_dict = [product.to_dict() for product in products]

        return jsonify({'objects': products_dict}), 201
    
    elif request.method == "POST":
        error = None
        
        data = request.json
        name = data['name']
        description = data['description']
        category_ids = data['category_ids']

        if (len(name.strip()) == 0 or len(name.strip()) > 32):
            error = 'Name is not valid'

        if (len(description.strip()) == 0 or len(description.strip()) > 128):
            error = 'Description is not valid'

        if not error:
            product = Product(name=name, description=description)
            for category_id in category_ids:
                category = Category.query.get(category_id)
                product.categories.append(category)

            db_session.add(product)
            db_session.commit()

            return jsonify({'message': 'successfully created new product.'}), 201
        else:
            return jsonify({'message': 'error when trying to create new product.', 'error': error}), 201
        
@bp.route('/products/<int:object_id>', methods=['GET', 'DELETE', 'PATCH'])
def product_details(object_id):
    if request.method == "GET":
        product = Product.query.get(object_id)

        if product:
            return jsonify({'object': product.to_dict()}), 201
        else:
            return 'Product not found', 404
        
    elif request.method == "DELETE":
        product = Product.query.get(object_id)

        if product:
            db_session.delete(product)
            db_session.commit()

            return jsonify({'message': 'success'}), 201
        else:
            return jsonify({'message': 'failed to find supplier'}), 400

    elif request.method == "PATCH":
        error = None

        product = Product.query.get(object_id)

        if product:
            data = request.json
            name = data['name']
            description = data['description']
            category_ids = data['category_ids']

            if (len(name.strip()) == 0 or len(name.strip()) > 32):
                error = 'Name is not valid'

            if (len(description.strip()) == 0 or len(description.strip()) > 128):
                error = 'Description is not valid'

            if not error:
                product.name = name
                product.description = description
                product.categories.clear()
                
                for category_id in category_ids:
                    category = Category.query.get(category_id)
                    product.categories.append(category)

                db_session.commit()

                return jsonify({'message': 'success'}), 201
            
            else:
                return jsonify({'error': 'failed to validate data'}), 400
            
        else:
            return jsonify({'message': 'failed to find product'}), 400

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
        error = None

        supplier = Supplier.query.get(object_id)

        if supplier:
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
                supplier.name = name
                supplier.description = description
                supplier.email = email
                supplier.address = address
                supplier.contact_number = contact_number

                db_session.commit()

                return jsonify({'message': 'success'}), 201
            
            else:
                return jsonify({'error': 'failed to validate data'}), 400
            
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
        



# Endpoint for filling DB when necessary (testing).
# visit /management in the frontend.
@bp.route('/fill')
def fill():
    categories = ['Consoles', 'PC', 'Controllers', 'CPUs', 'GPUs', 'Headsets', 'Peripherals', 'Hardware']
    suppliers = [
        {
            'name': 'Evetech',
            'address': '12 Eve road',
            'description': 'A PC hardware seller.',
            'email': 'evetech@gmail.com',
            'contact_number': '0742557767'
        },
        {
            'name': 'Takealot',
            'address': '12 Takealot road',
            'description': 'A seller.',
            'email': 'tklt@gmail.com',
            'contact_number': '0821231231'
        },
        {
            'name': 'GamingStuff',
            'address': '12 GamingStuff road',
            'description': 'A gaming hardware seller.',
            'email': 'gamingsff@gmail.com',
            'contact_number': '0827787762'
        },
        {
            'name': 'Super Electronics',
            'address': '12 Super road',
            'description': 'A discount electronics seller.',
            'email': 'superelectronicz@gmail.com',
            'contact_number': '0723157767'
        },
        {
            'name': 'Communica',
            'address': '12 Communica road',
            'description': 'An electronics seller.',
            'email': 'communica@gmail.com',
            'contact_number': '0212557767'
        },
    ]
    products = [
        {
            'name': 'PlayStation 5',
            'description': 'The overpriced next generation console you can\'t afford! Free multiplayer not included.',
            'categories': [1, 8]
        },
        {
            'name': 'Xbox Series X',
            'description': 'Halo',
            'categories': [1, 7, 8]
        },
        {
            'name': 'AMD Ryzen 7600',
            'description': 'CPU of the year.',
            'categories': [2, 4, 8]
        },
        {
            'name': 'LogicTech Mouse',
            'description': 'Great gaming mouse for all gamers!',
            'categories': [2, 7]
        },
        {
            'name': 'Corsair RGB fans',
            'description': 'For all your RGB needs (and cooling).',
            'categories': [2, 8]
        },
        {
            'name': '27-inch OLED Samsung Monitor',
            'description': 'Unparalleled pixels.',
            'categories': [7, 8]
        },
    ]
    inventory_items = [
        {
            'purchase_price': 13000,
            'product_id': 1,
            'supplier_id': 2,
            'quantity': 5
        },
        {
            'purchase_price': 11000,
            'product_id': 1,
            'supplier_id': 4,
            'quantity': 3
        },
        {
            'purchase_price': 12000,
            'product_id': 2,
            'supplier_id': 3,
            'quantity': 8
        },
        {
            'purchase_price': 14000,
            'product_id': 2,
            'supplier_id': 2,
            'quantity': 6
        },
        {
            'purchase_price': 11000,
            'product_id': 2,
            'supplier_id': 4,
            'quantity': 4
        },
        {
            'purchase_price': 7000,
            'product_id': 3,
            'supplier_id': 1,
            'quantity': 15
        },
        {
            'purchase_price': 7000,
            'product_id': 6,
            'supplier_id': 1,
            'quantity': 3
        },
        {
            'purchase_price': 12000,
            'product_id': 6,
            'supplier_id': 2,
            'quantity': 2
        },
        {
            'purchase_price': 1000,
            'product_id': 5,
            'supplier_id': 1,
            'quantity': 5
        },
        {
            'purchase_price': 1200,
            'product_id': 5,
            'supplier_id': 2,
            'quantity': 8
        },
    ]

    for i in range(len(categories)):
        category = Category(categories[i], f'All relating to {categories[i]}')
        db_session.add(category)

    for i in range(len(suppliers)):
        supplier = Supplier(name=suppliers[i]['name'], description=suppliers[i]['description'], contact_number=suppliers[i]['contact_number'], address=suppliers[i]['address'], email=suppliers[i]['email'])
        db_session.add(supplier)

    db_session.commit()

    for i in range(len(products)):
        product = Product(name=products[i]['name'], description=products[i]['description'])
        for category_id in products[i]['categories']:
                category = Category.query.get(category_id)
                product.categories.append(category)
        db_session.add(product)

    db_session.commit()

    for i in range(len(inventory_items)):
        product = Product.query.get(inventory_items[i]['product_id'])
        supplier = Supplier.query.get(inventory_items[i]['supplier_id'])
        for _ in range(inventory_items[i]['quantity']):
            item = InventoryItem(product=product, supplier=supplier, purchase_price=inventory_items[i]['purchase_price'])
            db_session.add(item)

    db_session.commit()

    return jsonify({'test': 'Filled'}), 201
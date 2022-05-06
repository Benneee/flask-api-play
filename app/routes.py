from crypt import methods
from flask import jsonify, request
from app import app


stores = [
    {
        'id': 1,
        'name': 'Ali Stores',
        'type': 'bookshop',
        'items': []
    },
    {
        'id': 2,
        'name': 'Bala Stores',
        'type': 'supermarket',
        'items': []
    },
    {
        'id': 3,
        'name': 'Iya Gbogo Stores',
        'type': 'confectionery store',
        'items': [
            {
                "id": 1,
                "name": "Corn Flakes",
                "price": 600
            },
            {
                "id": 2,
                "name": "Salt",
                "price": 200
            },
            {
                "id": 3,
                "name": "Corned beef",
                "price": 1200
            }
        ]
    },
    {
        "id": 4,
        "items": [],
        "name": "Sola Enterprises",
        "type": "building materials"
    }
]

@app.route('/')
def index():
    return 'Welcome to stores app!'


@app.route('/stores')
def get_stores():
    return jsonify(stores=stores)


@app.route('/stores/<int:id>', methods=['GET'])
def get_store(id):
    for item in stores:
        if item['id'] == int(id):
            return jsonify({'store': item})
    return jsonify({'message': 'store not found'})

@app.route('/stores/<string:type>')
def get_store_by_type(type):
    for item in stores:
        if item['type'].lower() == type.lower():
            return jsonify({'store': item})
    return jsonify({'message': 'store with that type could not be found'}) 


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    index_num = len(stores) + 1
    new_store = {
        'id': index_num,
        'name': request_data['name'],
        'type': request_data['type'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({ 'message': 'store created', 'store': new_store })

@app.route('/store/<int:id>/items', methods=['POST'])
def add_items_to_store(id):
    # First we find the store
    store = [store for store in stores if store['id'] == id]

    if store[0]:
        # Get all the items the user intends to add
        data = request.get_json()
        items = data['items']
        # Get all the existing items in the store
        store_items = store[0]['items']
        store_name = store[0]['name']

        # Check the items to be added and add each to the store's items
        if len(items) > 0:
            for item in items:
                store_items.append(item)
        return jsonify({'message': f'Items added to {store_name}', 'store': store[0]})
    return jsonify({'message': 'store not found'})

@app.route('/store/<int:id>/item', methods=['POST'])
def add_item_to_store(id):
    store = [store for store in stores if store['id'] == id]
    
    if store[0]:
        data = request.get_json()
        store_items = store[0]['items']
        new_index = len(store_items) + 1
        new_item = {
            'id': new_index,
            'name': data['name'],
            'price': data['price']
        }
        store_items.append(new_item)
        store_name = store[0]['name']
        return jsonify({'message': f'Items added to {store_name}', 'store': store[0]})
    return jsonify({'message': 'store not found'})
from crypt import methods
from flask import jsonify, request
from app import app


stores = [
    {
        'id': 1,
        'name': 'Ali Stores',
        'type': 'Bookshop',
        'items': []
    },
    {
        'id': 2,
        'name': 'Bala Stores',
        'type': 'Supermarket',
        'items': []
    },
    {
        'id': 3,
        'name': 'Iya Gbogo Stores',
        'type': 'Confectionery Store',
        'items': []
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


@app.route('/stores/<int:id>')
def get_store(id):
    for item in stores:
        if item['id'] == int(id):
            return jsonify({'store': item})
    return jsonify({'message': 'store not found'})

@app.route('/stores/<string:type>/item')
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
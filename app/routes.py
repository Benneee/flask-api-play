from flask import jsonify, request
from app import app


stores = [
    {
        'id': 1,
        'name': 'Ali Stores',
        'type': 'Bookshop'
    },
    {
        'id': 2,
        'name': 'Bala Stores',
        'type': 'Supermarket'
    },
    {
        'id': 3,
        'name': 'Iya Gbogo Stores',
        'type': 'Confectionery Store'
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
    store_item = None
    for item in stores:
        if item['id'] == int(id):
            print('item: ', item)
            store_item = item
            
    return store_item
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample inventory data
inventory = []

# Endpoint to get all items in the inventory
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

# Endpoint to add a new item to the inventory
@app.route('/inventory', methods=['POST'])
def add_item():
    item = request.json
    inventory.append(item)
    return jsonify(item), 201

# Endpoint to update an existing item
@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in inventory if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    data = request.json
    item.update(data)
    return jsonify(item), 200

# Endpoint to delete an item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    inventory = [item for item in inventory if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
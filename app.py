from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = {"book":"Modern C++","phone":"iPhone 14"}

@app.route('/intro', methods=['GET'])
def hello():
    return "This is HTTP REST API."

@app.route('/product/<key>', methods=['GET'])
def get_product(key):
    return jsonify({key: data_store.get(key, "Not found")})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(data_store)

@app.route('/product/<key>', methods=['POST'])
def create_product(key):
    value = request.json.get('value')
    data_store[key] = value
    return jsonify({key: value}), 201

@app.route('/product/<key>', methods=['PUT'])
def update_product(key):
    value = request.json.get('value')
    if key in data_store:
        data_store[key] = value
        return jsonify({key: value})
    return "Not found", 404

@app.route('/product/<key>', methods=['DELETE'])
def delete_product(key):
    if key in data_store:
        del data_store[key]
        return "Deleted", 204
    return "Not found", 404

@app.route('/lab15/operation/', methods=['POST'])
def do_operation():
    data = request.get_json()
    numa = data['a']
    numb = data['b']
    oper = data['operator']
    if oper == "+":
        result = numa + numb
    elif oper == "-":
        result = numa - numb
    else:
        result = "uildlee zov oruulna uu!"
    return jsonify({"result": str(result)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
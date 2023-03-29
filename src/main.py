from flask import Flask, jsonify, request
import json

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/')
def main():
    info = {
        "Message": "API REST with FLASK"
    }
    return jsonify(info)

@app.route('/api/saludo', methods=['GET'])
def get_saludo():
    return jsonify({ "Message": "Hello World from GET Method" })

@app.route('/api/saludo', methods=['POST'])
def post_saludo():
    return jsonify({ "Message": "Hello World from POST Method" })

@app.route('/api/saludo', methods=['PUT'])
def put_saludo():
    return jsonify({ "Message": "Hello World from PUT Method" })

@app.route('/api/saludo', methods=['DELETE'])
def delete_saludo():
    return jsonify({ "Message": "Hello World from DELETE Method" })

@app.route('/api/despedida', methods=['GET', 'POST', 'PUT', 'DELETE'])
def despedida():
    if request.method == 'GET':
        return jsonify({ "Message": "Good Bye! from GET Method" })

    if request.method == 'POST':
        return jsonify({ "Message": "Good Bye! from POST Method" })

    if request.method == 'PUT':
        return jsonify({ "Message": "Good Bye! from PUT Method" })

    if request.method == 'DELETE':
        return jsonify({ "Message": "Good Bye! from DELETE Method" })

@app.route('/api/test', methods=['POST', 'PUT'])
def test():
    if request.method == 'POST':
        # using request.data
        print(request.data)
        data = json.loads(request.data)
        print(data)
        print(data['name'], " ", data['lastname'])

        # using request.get_json()
        data = request.get_json()
        print(data['name'], " ", data['lastname'])

        # using request.json.get('field')
        name = request.json.get('name')
        lastname = request.json.get('lastname')
        print(name, " ", lastname)

        return "POST"

    if request.method == 'PUT':
        return "PUT"

@app.route('/api/saludo/<name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def all_saludo_by_name(name):
    if request.method == 'GET':
        return jsonify({ "Message": f"Good Morning! {name} from GET Method" })

    if request.method == 'POST':
        return jsonify({ "Message": f"Good Morning! {name} from POST Method" })

    if request.method == 'PUT':
        return jsonify({ "Message": f"Good Morning! {name} from PUT Method" })

    if request.method == 'DELETE':
        return jsonify({ "Message": f"Good Morning! {name} from DELETE Method" })

if __name__ == '__main__':
    app.run()
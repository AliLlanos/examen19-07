from flask import Flask, jsonify, request
from repository import UserRepo

app = Flask(__name__)

user_repo = UserRepo()

@app.route('/create/user', methods=['POST'])
def create_user():
    data = request.get_json()
    id_user = data.get('id')
    name = data.get('name')
    age = data.get('age')

    user = user_repo.add_user(id_user, name, age)
    return jsonify({'message': 'se ha creado el usuario'}), 201

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = user_repo.get_user(id)
    if user:
        return jsonify(user)
    return jsonify({'message': 'no se encontro al usuario'}), 404

if __name__ == '__main__':
    app.run(debug=True)







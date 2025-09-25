from flask import Blueprint, request, jsonify
from user_model import create_new_user,update_user,delete_user

bp_user = Blueprint('users', __name__)

@bp_user.route('/users',methods=['POST'])
def create_user():
    try:
        response = request.json
        user = create_new_user(response)
        return jsonify(user)
    except Exception as e:
        return jsonify({'erro': str(e)})
    
@bp_user.route('/user/<id>', methods=['PUT'])
def update_user(id):
    try:
        response = request.json
        user_atualizado = update_user(id,response)
        return jsonify(user_atualizado)
    except Exception as e:
        return jsonify({'erro': str(e)})
    
@bp_user.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user_deletado = delete_user(id)
        return jsonify(user_deletado)
    except Exception as e:
        return jsonify({'erro':str(e)})


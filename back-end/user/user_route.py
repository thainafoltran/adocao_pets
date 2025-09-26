from flask import Blueprint, request, jsonify
from .user_model import create_new_user,update_user,delete_user, get_all_users

bp_user = Blueprint('users', __name__)

@bp_user.route('/users', methods=['POST'])
def create_user():
    try:
        response = request.json
        data, status = create_new_user(response)  
        return jsonify(data), status
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    
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
    
@bp_user.route('/users', methods=['GET'])
def get_users():
    return jsonify(get_all_users())
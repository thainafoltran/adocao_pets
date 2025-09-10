from flask import Blueprint, request, jsonify
from model import cadastrar_pet


pet_bp = Blueprint('pets', __name__)


@pet_bp.route('/cadastro', methods=['POST'])
def create_pet():
    new = request.get_json()
    cadastrar_pet(new.get)
    return jsonify ({'cadastrado com sucesso!'}), 201
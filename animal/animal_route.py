from flask import Blueprint, request, jsonify
from .animal_model import get_pets, get_pet_by_id, create_pet, update_pet, delete_pet


pet_bp = Blueprint('pets', __name__)

@pet_bp.route('/pets', methods=['GET'])
def getPets():
    return jsonify(get_pets)

@pet_bp.route('/pets/<id>', methods=['GET'])
def getById(id):
    try:
        pet = get_pet_by_id(id)
        return jsonify(pet)
    except Exception as e:
        return jsonify({'erro': str(e)})

@pet_bp.route('/pets', methods=['POST'])
def createPet():
    try:
        response = request.json
        pet = create_pet(response)
        return jsonify(pet)
    except Exception as e:
        return jsonify({'erro': str(e)})
    
@pet_bp.route('/pets/<id>', methods=['PUT'])
def updatePet(id):
    try:
        response = request.get_json()
        pet_atualizado = update_pet(response)
        return jsonify(pet_atualizado)
    except Exception as e:
        return jsonify({'erro': str(e)})

@pet_bp.route('/pets/<id>', methods=['DELETE'])
def deletePet(id):
    try:
        pet_deletado = delete_pet(id)
        return jsonify(pet_deletado)
    except Exception as e:
        return jsonify({'erro': str(e)})
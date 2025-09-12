from flask import jsonify
from config import db

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    especie = db.Column(db.String(100), nullable = False)
    localizacao = db.Column(db.String(100), nullable = False)
    idade = db.Column(db.Integer, nullable = False)

    def __init__(self, nome, especie, localizacao, idade):
        self.nome = nome
        self.especie = especie
        self.localizacao = localizacao
        self.idade = idade
    
    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "especie":self.especie,
            "localizacao":self.localizacao,
            "idade":self.idade
        }
    
    #função rotas

def get_pets():
    pets = Pet.query.all()
    return [pet.to_dict() for pet in pets]

def get_pet_by_id(id_pet):
    pet = Pet.query.get(id_pet)
    if pet:
        return pet.to_dict()

def create_pet(pet):
    if not pet or 'nome' not in pet:
        return jsonify({'error':'pet sem nome'})
    novo_pet = Pet(
        nome = pet['nome'],
        especie = pet['especie'],
        localizacao = pet['localizacao'],
        idade = pet['idade']
    )
    db.session.add(novo_pet)
    db.session.commit()

    return{"mensagem":"Pet cadastrado com sucesso!"}

def update_pet(id_pet, alteracao_pet):
    pet = Pet.query.get(id_pet)
    if not pet:
        return jsonify({'error':'pet não cadastrado'})
    if "nome" in alteracao_pet:
        pet.nome = alteracao_pet["nome"]
    if "especie" in alteracao_pet:
        pet.especie = alteracao_pet["especie"]
    if "localizacao" in alteracao_pet:
        pet.localizacao = alteracao_pet["localizacao"]
    if "idade" in alteracao_pet:
        pet.idade = alteracao_pet["idade"]

    db.session.commit()
    return {"mensagem":"Pet atualizado com sucesso!"}

def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        return jsonify({'erro':'pet não encontrado'})
    db.session.delete(pet)
    db.session.commit()
    return {"mensagem":"Pet deletado com sucesso"}
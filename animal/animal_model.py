from flask import jsonify
from config import db

class Pet(db.Model):
    __tablename__ = "pets"


    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    especie = db.Column(db.String(100), nullable = False)
    localizacao = db.Column(db.String(100), nullable = False)
    idade = db.Column(db.Integer, nullable = False)

    def __init__(self, id, nome, especie, localizacao, idade):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.localizacao = localizacao
        self.idade = idade
from flask import jsonify

#só teste
pets_cadastrados = []

class Animais():
    __tablename__ = "pets"


    def __init__(self, nome_pet, raça, especie, localizaçao, idade):
        self.nome_pet = nome_pet
        self.raça = raça
        self.especie = especie #gato ou cachorro. não sei se tira ou deixa
        self.localizaçao = localizaçao
        self.idade = idade


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

#funções 

def cadastrar_pet(add_pet):
    novo_pet = Animais(
        nome_pet=add_pet['nome do pet'],
        raça=add_pet['raça'],
        especie=add_pet['especie'],
        localizaçao=add_pet['localizaçao'],
        idade=add_pet['idade']
    )

    pets_cadastrados.append(novo_pet)
    return novo_pet
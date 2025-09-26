from flask import jsonify
from config import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False)
    senha = db.Column(db.String(20), nullable = False)
    nome = db.Column(db.String(20), nullable = False)
    phone = db.Column(db.String(11), nullable = False)

    def __init__(self, email, senha, nome, phone):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.phone = phone

def create_new_user(user):
    user_existing = User.query.filter_by(email=user['email']).first()
    if user_existing:
        return {'msg': 'Email já cadastrado'}, 400
    senha = user.get('senha', '')
    if len(senha) < 8:
        return {'msg': 'Sua senha deve ter pelo menos 8 caracteres'}, 400
    novo_user = User(
        nome=user['nome'],
        email=user['email'],
        senha=user['senha'],
        phone=user['phone']
    )

    db.session.add(novo_user)
    db.session.commit()
    return {"mensagem": "User cadastrado com sucesso!"}, 201

def update_user(id_user, alteracao_user):
    user = User.query.get(id_user)
    if not user:
        return {'error':'user não cadastrado'}
    if "nome" in alteracao_user:
        user.nome = alteracao_user["nome"]
    if "email" in alteracao_user:
        user.email = alteracao_user["email"]
    if "phone" in alteracao_user:
        user.phone = alteracao_user["phone"]
    if "senha" in alteracao_user:
        user.senha = alteracao_user["senha"]

    db.session.commit()
    return {"msg":"user atualizado com sucesso!"}

def delete_user(id_user):
    pass

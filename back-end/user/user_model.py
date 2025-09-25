from flask import jsonify
from config import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False)
    senha = db.Column(db.String(20), nullable = False)
    nome = db.Column(db.String(20), nullable = False)

    def __init__(self, email, senha, nome):
        self.email = email
        self.senha = senha
        self.nome = nome

def create_new_user(user):
    user_existing = User.query.filter_by(email=user['email']).first()
    if user_existing:
        return jsonify({'msg': 'email já cadastrado'}), 400
    senha = user.get('senha', '')
    if len(senha) < 8:
        return jsonify({'msg':'sua senha deve ter pelo menos 8 caracteres'})
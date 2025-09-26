from flask import Blueprint, jsonify, request
from config import db
from user.user_model import User

login_bp = Blueprint("login_bp", __name__)


@login_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")

    if not email or not senha:
        return jsonify({"msg": "Usuário e senha são obrigatórios"}), 400
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"msg":"Usuário não encontrado"}), 404
    
    if user.senha != senha:
        return jsonify({"msg": "Senha incorreta"}), 401
    
    return jsonify({"msg": "Login realizado com sucesso"})
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token,get_jwt_identity,jwt_required
from config import db
from werkzeug.security import check_password_hash
from user_model import User

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "senha-super-secreta"

jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Usuário e senha são obrigatórios"}), 400
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"msg":"Usuário não encontrado"}), 404
    
    if user.password != password:
        return jsonify({"msg": "Senha incorreta"}), 401
    
    return jsonify({"msg": "Login realizado com sucesso", "user_id": user.id})
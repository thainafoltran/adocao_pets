from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
app.config['PORT']=5000
app.config['DEBUG'] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)#apenas para testes
db = SQLAlchemy(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
app.config['PORT']=5000
app.config['DEBUG'] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r"/pets": {"origins": "http://127.0.0.1:5500"}})
CORS(app, resources={r"/users": {"origins": "http://127.0.0.1:5500"}})
CORS(app, resources={r"/login": {"origins": "http://127.0.0.1:5500"}})

db = SQLAlchemy(app)
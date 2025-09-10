from flask import Flask, render_template
from route import pet_bp


app = Flask(__name__)

app.register_blueprint(pet_bp)

if __name__ == '__main__':
    app.run(debug=True)
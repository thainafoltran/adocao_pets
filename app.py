from config import app, db
from animal.animal_route import pet_bp

app.register_blueprint(pet_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
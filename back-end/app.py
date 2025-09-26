from config import app, db
from animal.animal_route import pet_bp
from user.user_route import bp_user
from user.login import login_bp

app.register_blueprint(pet_bp)
app.register_blueprint(bp_user)
app.register_blueprint(login_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi database
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Places(db.Model):
   __tablename__ = 'place'

   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(120), unique=True)

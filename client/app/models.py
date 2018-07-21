from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    code = db.Column(db.TEXT)
    body = db.Column(db.TEXT)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)

    def __repr__(self):
        return '<Contract {}:{}>'.format(User.query.get(self.owner_id).username, self.title)

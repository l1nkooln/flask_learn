from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(200))
    logiks = db.Column(db.Integer, default = 0)

    projects = db.relationship('Project', backref = 'author')

    def __repr__(self):
        return f"User: {self.username}"
    
    def set_password_hash(self, original_password):
        self.password  = generate_password_hash(original_password)

    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    link = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Project: {self.title}"

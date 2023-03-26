from app import *


with app.app_context():
    db.create_all()
    user = User(name='John', username = 'john222', password = '23232')
    db.session.add(user)
    db.session.commit()

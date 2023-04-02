from app import *


with app.app_context():
    db.create_all()
    user = User(name='Вова', username = 'bvodfjkfkdf', password = '23bgf232')
    db.session.add(user)
    db.session.commit()


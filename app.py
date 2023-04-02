from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # створюємо  БД
app = Flask(__name__) # Створюємо веб–додаток Flask

app.config['SECRET_KEY'] = "680581c5172841f87212bf4f927279ef4c860f9c"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

from routes import *

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5001, debug=True) # Запускаємо веб-сервер з цього файлу
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # створюємо  БД
app = Flask(__name__) # Створюємо веб–додаток Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(200))
    logiks = db.Column(db.Integer, default = 0)

    projects = db.relationship('Project', backref = 'author')

    def __repr__(self):
        return f"User: {self.username}"
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    link = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Project: {self.title}"

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    users = User.query.all()
    print(users)
    return render_template("index.html", users = users)#Результат, що повертається у браузер

@app.route("/signup", methods = ["POST", "GET"])
def signup():
    return render_template("signup.html")

@app.route("/signin", methods = ["POST", "GET"])
def signin():
    return render_template("login.html")


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5001, debug=True) # Запускаємо веб-сервер з цього файлу
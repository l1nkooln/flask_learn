from flask import Flask

app = Flask(__name__) # Створюємо веб–додаток Flask

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    return "Hello, World!" #Результат, що повертається у браузер

if __name__ == "__main__":
    app.run() # Запускаємо веб-сервер з цього файлу
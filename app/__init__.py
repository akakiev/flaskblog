# В цьому файлі ми ініціалізуємо нашу програму та базу даних
# Імпортуємо клас Flask з бібліотеки flask та клас SQLAlchemy з бібліотеки flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    from app.routes import main
    app.register_blueprint(main)

    return ap
# Створюємо екземпляр класу Flask
# app = Flask(__name__)
# Встановлюємо конфігурацію для бази даних та секретного ключа
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/flaskblog.sqlite'
app.config['SECRET_KEY'] = 'your_secret_key'
# Ініціалізуємо базу даних
db = SQLAlchemy(app)




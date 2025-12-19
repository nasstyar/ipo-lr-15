from flask import jsonify, request
from datetime import datetime
from app import app

@app.route('/')
def index():
    return "Добро пожаловать в Flask-сервис!"

@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"

@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"Квадрат числа {number} равен {result}."

@app.route('/sum')
def sum_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        return f"Сумма {a} и {b} равна {result}."
    except (TypeError, ValueError):
        return "Ошибка: передайте числа в параметрах a=... и b=...", 400

@app.route('/info')
def info():
    info_data = {
        "version": "1.0",
        "author": "Козлова Анастасия", 
        "launch_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(info_data)
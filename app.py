"""
Flask server for culculator
"""
from flask import Flask, render_template, request, make_response, jsonify
# from upd import calculate
from calc import calculate
# Создание веб-приложения Flask
app = Flask(__name__)

# Обработка обращения к главной странице
@app.route('/')
def index():
    return render_template('index.html')

# Обработка запроса на вычисление
@app.route('/calculate', methods=['POST'])
def take_send():
    req = request.get_json()
    ans = calculate(req)
    res = make_response(jsonify({'rez': ans[0], 'rez_dec': ans[1]}), 200)
    return res

@app.route('/game_mode', methods=['GET'])
def game_mode():
    req = request.get_json()
    ans = calculate(req)
    res = make_response(jsonify({'rez': ans[0], 'rez_dec': ans[1]}), 200)
    return res

# Запуск сервера на порту 4567
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567, debug=False)

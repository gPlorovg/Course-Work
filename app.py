from flask import Flask, render_template, request, make_response, jsonify

import calc
from calc import calculate

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def take_send():
    req = request.get_json()
    res = make_response(jsonify({'rez': calc.calculate(req)}), 200)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567, debug=False)

#TODO: не работают вычисления с прописными буквами
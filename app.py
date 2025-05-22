from flask import Flask, request, jsonify
from number_set import NumberSet100

app = Flask(__name__)

@app.route('/api/extract', methods=['POST'])
def extract_number():
    data = request.get_json()

    if 'number' not in data:
        return jsonify({'error': 'Se requiere el campo "number"'}), 400

    try:
        number = int(data['number'])
    except ValueError:
        return jsonify({'error': 'El número debe ser un entero válido'}), 400

    conjunto = NumberSet100()

    try:
        conjunto.extract(number)
        missing = conjunto.find_missing_number()
        return jsonify({'numero_extraido': missing}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

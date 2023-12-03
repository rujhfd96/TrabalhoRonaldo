from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/converter', methods=['POST'])
def converter():
    data = request.get_json()

    valor = data.get('valor')
    moeda = data.get('moeda')

    # Lógica para converter moeda (exemplo: fixar valor da cotação)
    cotacao_dolar = 5.2
    valor_convertido = valor * cotacao_dolar

    return jsonify({'valor_convertido': valor_convertido, 'moeda_destino': 'Real'})

if __name__ == '__main__':
    app.run(debug=True)

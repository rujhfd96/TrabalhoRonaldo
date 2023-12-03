from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/converter', methods=['POST'])
def converter():
    data = request.get_json()

    valor = data.get('valor')
    moeda = data.get('moeda')

    # Lógica para converter moeda (exemplo: fixar valor da cotação)
    cotacao_dolar = 5.2
    cotacao_euro = 6.2

    if moeda == 'Dólar':
        valor_convertido = valor * cotacao_dolar
    elif moeda == 'Euro':
        valor_convertido = valor * cotacao_euro
    else:
        return jsonify({'erro': 'Moeda não suportada'}), 400

    return jsonify({'valor_convertido': valor_convertido, 'moeda_destino': 'Real'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/converter', methods=['POST'])
def converter():
    data = request.get_json()

    valor = data.get('valor')
    moeda = data.get('moeda')

    
    cotacao_dolar = 4.9
    cotacao_euro = 5.2

    if moeda == 'Dólar':
        valor_convertido = valor * cotacao_dolar
    elif moeda == 'Euro':
        valor_convertido = valor * cotacao_euro
    else:
        return jsonify({'erro': 'Moeda não suportada'}), 400

    return jsonify({'valor_convertido': valor_convertido, 'moeda_destino': 'Real'})

if __name__ == '__main__':
    app.run(debug=True)

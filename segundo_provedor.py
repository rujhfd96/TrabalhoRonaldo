

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/converter2', methods=['POST'])
def converter2():
    data = request.get_json()

    valor = data.get('valor')
    moeda_origem = data.get('moeda')

    cotacao_bitcoin = 0.0000048  
    cotacao_ethereum = 0.000090  

    if moeda_origem == 'Real':
        return jsonify({'erro': 'Moeda de origem não suportada'}), 400
    elif moeda_origem == 'Dólar':
        valor_convertido_bitcoin = valor * cotacao_bitcoin
        valor_convertido_ethereum = valor * cotacao_ethereum
    elif moeda_origem == 'Euro':
        valor_convertido_bitcoin = valor * cotacao_bitcoin * 1.1  
        valor_convertido_ethereum = valor * cotacao_ethereum * 1.1

    return jsonify({
        'valor_convertido_bitcoin': valor_convertido_bitcoin,
        'valor_convertido_ethereum': valor_convertido_ethereum,
        'moeda_destino': 'Criptomoedas'
    })

if __name__ == '__main__':
    app.run(debug=True)

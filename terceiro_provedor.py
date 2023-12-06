from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/converter3', methods=['POST'])
def converter3():
    data = request.get_json()

    valor = data.get('valor')
    destino = data.get('destino')

    cotacao_usd = 4.9  
    cotacao_eur = 5.2  
    cotacao_gbp = 7.4  
    cotacao_jpy = 0.049  
    cotacao_inr = 0.071  
    cotacao_aud = 4.0  
    cotacao_cad = 4.2  
    cotacao_chf = 5.8  
    cotacao_cny = 0.82  
    cotacao_sek = 0.6  

    if destino == 'EUA':
        valor_convertido = valor * cotacao_usd
        moeda_destino = 'Dólar (USD)'
    elif destino == 'Europa':
        valor_convertido = valor * cotacao_eur
        moeda_destino = 'Euro (EUR)'
    elif destino == 'Reino Unido':
        valor_convertido = valor * cotacao_gbp
        moeda_destino = 'Libra Esterlina (GBP)'
    elif destino == 'Japão':
        valor_convertido = valor * cotacao_jpy
        moeda_destino = 'Iene Japonês (JPY)'
    elif destino == 'Índia':
        valor_convertido = valor * cotacao_inr
        moeda_destino = 'Rúpia Indiana (INR)'
    elif destino == 'Austrália':
        valor_convertido = valor * cotacao_aud
        moeda_destino = 'Dólar Australiano (AUD)'
    elif destino == 'Canadá':
        valor_convertido = valor * cotacao_cad
        moeda_destino = 'Dólar Canadense (CAD)'
    elif destino == 'Suíça':
        valor_convertido = valor * cotacao_chf
        moeda_destino = 'Franco Suíço (CHF)'
    elif destino == 'China':
        valor_convertido = valor * cotacao_cny
        moeda_destino = 'Yuan Chinês (CNY)'
    elif destino == 'Suécia':
        valor_convertido = valor * cotacao_sek
        moeda_destino = 'Coroa Sueca (SEK)'
    else:
        return jsonify({'erro': 'País de destino não suportado'}), 400

    return jsonify({'valor_convertido': valor_convertido, 'moeda_destino': moeda_destino})

if __name__ == '__main__':
    app.run(debug=True, port=5002)  

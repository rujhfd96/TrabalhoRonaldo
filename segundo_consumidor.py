
import requests

def consumir_provedor2(url_provedor2, data):
    response = requests.post(url_provedor2, json=data)

    if response.status_code == 200:
        resultado = response.json()
        return resultado
    else:
        print(f'Erro na solicitação: {response.status_code}')
        return None

url_provedor2 = 'http://127.0.0.1:5001/converter2'

valor = float(input('Valor a converter: '))
moeda_origem = input('Moeda de origem (Dólar ou Euro): ')

data = {'valor': valor, 'moeda': moeda_origem}
resultado_consumidor_2 = consumir_provedor2(url_provedor2, data)

if resultado_consumidor_2:
    valor_convertido_bitcoin = resultado_consumidor_2['valor_convertido_bitcoin']
    valor_convertido_ethereum = resultado_consumidor_2['valor_convertido_ethereum']
    valor_convertido_litecoin = resultado_consumidor_2['valor_convertido_litecoin']
    valor_convertido_ripple = resultado_consumidor_2['valor_convertido_ripple']

    print(f'Valor convertido para Bitcoin: {valor_convertido_bitcoin:.8f} BTC')
    print(f'Valor convertido para Ethereum: {valor_convertido_ethereum:.6f} ETH')
    print(f'Valor convertido para Litecoin: {valor_convertido_litecoin:.6f} LTC')
    print(f'Valor convertido para Ripple: {valor_convertido_ripple:.6f} XRP')

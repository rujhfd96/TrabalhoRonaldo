import requests

url_provedor2 = 'http://127.0.0.1:5001/converter2'

valor = float(input('Valor a converter: '))
moeda_origem = input('Moeda de origem (Dólar ou Euro): ')

data = {'valor': valor, 'moeda': moeda_origem}
response = requests.post(url_provedor2, json=data)

if response.status_code == 200:
    resultado = response.json()
    valor_convertido_bitcoin = resultado['valor_convertido_bitcoin']
    valor_convertido_ethereum = resultado['valor_convertido_ethereum']
    valor_convertido_litecoin = resultado['valor_convertido_litecoin']
    valor_convertido_ripple = resultado['valor_convertido_ripple']

    print(f'Valor convertido para Bitcoin: {valor_convertido_bitcoin:.8f} BTC')
    print(f'Valor convertido para Ethereum: {valor_convertido_ethereum:.6f} ETH')
    print(f'Valor convertido para Litecoin: {valor_convertido_litecoin:.6f} LTC')
    print(f'Valor convertido para Ripple: {valor_convertido_ripple:.6f} XRP')
else:
    print(f'Erro na solicitação: {response.status_code}')



import requests

url_provedor2 = 'http://127.0.0.1:5000/converter2'

valor = float(input('Valor a converter: '))
moeda_origem = input('Moeda de origem (Dólar ou Euro): ')

data = {'valor': valor, 'moeda': moeda_origem}
response = requests.post(url_provedor2, json=data)

if response.status_code == 200:
    resultado = response.json()
    valor_convertido_bitcoin = resultado['valor_convertido_bitcoin']
    valor_convertido_ethereum = resultado['valor_convertido_ethereum']

    print(f'Valor convertido para Bitcoin: {valor_convertido_bitcoin:.8f} BTC')
    print(f'Valor convertido para Ethereum: {valor_convertido_ethereum:.6f} ETH')
else:
    print(f'Erro na solicitação: {response.status_code}')

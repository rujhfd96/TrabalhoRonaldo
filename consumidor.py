import requests

url_provedor = 'http://127.0.0.1:5000/converter'


valor = float(input('Valor a converter: '))
moeda = input('Moeda a converter (Dólar ou Euro): ')


data = {'valor': valor, 'moeda': moeda}
response = requests.post(url_provedor, json=data)


if response.status_code == 200:
    resultado = response.json()
    valor_convertido = resultado['valor_convertido']
    print(f'Valor convertido: {valor_convertido:.2f} Real')
else:
    print(f'Erro na solicitação: {response.status_code}')

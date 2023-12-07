
import requests

def consumir_provedor(url_provedor, data):
    response = requests.post(url_provedor, json=data)

    if response.status_code == 200:
        resultado = response.json()
        return resultado
    else:
        print(f'Erro na solicitação: {response.status_code}')
        return None

url_provedor = 'http://127.0.0.1:5000/converter'

valor = float(input('Valor a converter: '))
moeda = input('Moeda a converter (Dólar ou Euro): ')

data = {'valor': valor, 'moeda': moeda}
resultado_consumidor_1 = consumir_provedor(url_provedor, data)

if resultado_consumidor_1:
    valor_convertido = resultado_consumidor_1['valor_convertido']
    print(f'Valor convertido: {valor_convertido:.2f} Real')

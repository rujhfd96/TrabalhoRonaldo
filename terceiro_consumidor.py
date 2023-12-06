import requests

url_provedor3 = 'http://127.0.0.1:5002/converter3'

valor = float(input('Quantia de dinheiro a levar: '))
print("Opções de países: EUA, Europa, Reino Unido, Japão, Índia, Austrália, Canadá, Suíça, China, Suécia")

destino = input('País de destino: ')

data = {'valor': valor, 'destino': destino}
response = requests.post(url_provedor3, json=data)

if response.status_code == 200:
    resultado = response.json()
    valor_convertido = resultado['valor_convertido']
    moeda_destino = resultado['moeda_destino']
    print(f'Valor convertido para {moeda_destino}: {valor_convertido:.2f}')
else:
    print(f'Erro na solicitação: {response.status_code}')
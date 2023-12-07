
import requests

def consumir_provedor3(url_provedor3, data):
    response = requests.post(url_provedor3, json=data)

    if response.status_code == 200:
        resultado = response.json()
        return resultado
    else:
        print(f'Erro na solicitação: {response.status_code}')
        return None

url_provedor3 = 'http://127.0.0.1:5002/converter3'

valor = float(input('Quantia de dinheiro a levar: '))
print("Opções de países: EUA, Europa, Reino Unido, Japão, Índia, Austrália, Canadá, Suíça, China, Suécia")

destino = input('País de destino: ')

data = {'valor': valor, 'destino': destino}
resultado_consumidor_3 = consumir_provedor3(url_provedor3, data)

if resultado_consumidor_3:
    valor_convertido = resultado_consumidor_3['valor_convertido']
    moeda_destino = resultado_consumidor_3['moeda_destino']
    print(f'Valor convertido para {moeda_destino}: {valor_convertido:.2f}')

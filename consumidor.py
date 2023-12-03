import requests

url_provedor = 'http://127.0.0.1:5000/converter'

# Solicitamos ao usuário os detalhes da conversão
valor = float(input('Valor a converter: '))
moeda = input('Moeda a converter (Dólar ou Euro): ')

# Enviando a solicitação para o provedor
data = {'valor': valor, 'moeda': moeda}
response = requests.post(url_provedor, json=data)

# Exibindo o resultado
if response.status_code == 200:
    resultado = response.json()
    valor_convertido = resultado['valor_convertido']
    print(f'Valor convertido: {valor_convertido:.2f} Real')
else:
    print(f'Erro na solicitação: {response.status_code}')

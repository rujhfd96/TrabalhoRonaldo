import requests

url_provedor = 'URL_DO_WEBSERVICE_PROVEDOR/converter'

data = {
    'valor': 50.00,
    'moeda': 'Dólar'
}

response = requests.post(url_provedor, json=data)

resultado = response.json()

print(f"Valor convertido: {resultado['valor_convertido']} {resultado['moeda_destino']}")

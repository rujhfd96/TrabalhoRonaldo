import subprocess
import os

# Obtém o diretório atual do script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói os caminhos absolutos para os scripts
provedor1_path = os.path.join(script_directory, "provedor.py")
provedor2_path = os.path.join(script_directory, "segundo_provedor.py")
consumidor1_path = os.path.join(script_directory, "consumidor.py")
consumidor2_path = os.path.join(script_directory, "segundo_consumidor.py")

# Iniciar provedores
provedor1 = subprocess.run(["python", provedor1_path])
provedor2 = subprocess.run(["python", provedor2_path])

# Aguardar um curto período para garantir que os provedores estejam prontos
time.sleep(2)

# Iniciar consumidores
consumidor1 = subprocess.run(["python", consumidor1_path])
consumidor2 = subprocess.run(["python", consumidor2_path])

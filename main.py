import subprocess
import time

# Iniciar provedores
provedor1 = subprocess.run(["python", "primeiro_provedor.py"])
provedor2 = subprocess.run(["python", "segundo_provedor.py"])

# Aguardar um curto período para garantir que os provedores estejam prontos
time.sleep(2)

# Iniciar consumidores
consumidor1 = subprocess.run(["python", "primeiro_consumidor.py"])
consumidor2 = subprocess.run(["python", "segundo_consumidor.py"])

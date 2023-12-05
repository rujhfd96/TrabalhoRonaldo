import subprocess
import time


subprocess.Popen(["python", "primeiro_provedor.py"])


time.sleep(1)


subprocess.Popen(["python", "segundo_provedor.py"])


time.sleep(1)


subprocess.Popen(["python", "primeiro_consumidor.py"])


subprocess.Popen(["python", "segundo_consumidor.py"])

import subprocess
import os


script_directory = os.path.dirname(os.path.abspath(__file__))


provedor1_path = os.path.join(script_directory, "provedor.py")
provedor2_path = os.path.join(script_directory, "segundo_provedor.py")
consumidor1_path = os.path.join(script_directory, "consumidor.py")
consumidor2_path = os.path.join(script_directory, "segundo_consumidor.py")


provedor1 = subprocess.run(["python", provedor1_path])
provedor2 = subprocess.run(["python", provedor2_path])


time.sleep(2)


consumidor1 = subprocess.run(["python", consumidor1_path])
consumidor2 = subprocess.run(["python", consumidor2_path])

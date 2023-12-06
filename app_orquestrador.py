import subprocess

def main():
    print("Escolha uma opção:")
    print("1. Converter moeda")
    print("2. Converter para criptomoedas")
    print("3. Viajar")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        subprocess.run(['python', 'consumidor.py'])
    elif opcao == '2':
        subprocess.run(['python', 'segundo_consumidor.py'])
    elif opcao == '3':
        subprocess.run(['python', 'terceiro_consumidor.py'])
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    main()

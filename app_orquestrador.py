
import subprocess

def main():
    opcoes = ["Converter moeda", "Converter para criptomoedas", "Viajar"]
    print("Escolha uma opção:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

    escolhas = []

    while True:
        opcao = input("Digite o número da opção desejada (0 para encerrar): ")
        if opcao == '0':
            break
        escolhas.append(int(opcao))

    for escolha in escolhas:
        if escolha == 1:
            subprocess.run(['python', 'consumidor.py'])
        elif escolha == 2:
            subprocess.run(['python', 'segundo_consumidor.py'])
        elif escolha == 3:
            subprocess.run(['python', 'terceiro_consumidor.py'])
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()

try:
    from time import sleep
    from os import system
    from sys import platform
    from analise_musica import *
    from KNeighbors import *
    from grafico import *
except ImportError as error:
    print("Import Error : %s" %error)
    quit(1)

def apagar_terminal():
    """Identifica o sistema operacional em uso para usar o comando adequado"""

    if platform.startswith("linux"):
        system("clear")
    elif platform.startswith("win32"):
        system("cls")

def escolha_analise():
    musica = input("Digite o nome da música: ").title()
    print("Método para analise: \n1 - KNeighborsClassifier\n2 - Plotar gráfico")
    while True:
        try:
            opcao = int(input("Opção desejada: "))
            break
        except ValueError:
            print("Digite uma opção válida")
    apagar_terminal()
    print("\n")
    if opcao == 1:
        if buscar(musica) == False:
            analise_musica(musica)
    elif opcao == 2:
        if resultado(musica) == False:
            analise_musica(musica)
        sleep(1)
    else:
        print("Opção escolhida não existente. Escolha uma opção valida")

def opcoes(escolha):
    """Recebe a escolha do usuario e retorna o que foi pedido"""

    apagar_terminal()
    if escolha == 1:
        escolha_analise()
    elif escolha == 2:
        musica = input("Digite o nome da música que deseja procurar (Banda - Nome): ").title()
        apagar_terminal()
        buscar_musica(musica)
    elif escolha == 3:
        musica_link = input("Informe o link do vídeo: ")
        apagar_terminal()
        baixar_musica(musica_link)
    elif escolha == 4:
        print("\n--------Saindo--------")
        fechar_banco()
        return "Sair"
    else:
        print("Escolha uma opção válida")

def main():
    while True:
        print("\n--------Escolha a operação desejada--------\n")

        print("1 - Analisar uma música.\n"
              "2 - Procurar por uma música no banco de dados (Banda - Nome).\n"
              "3 - Baixar vídeo do youtube.\n"
              "4 - Sair do programa.\n")

        while True:
            try:
                escolha = int(input("Digite a opção desejada: "))
                break
            except ValueError:
                print("Digite um valor válido!")

        if opcoes(escolha) == "Sair":
            break

main()
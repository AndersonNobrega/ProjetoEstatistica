try:
    from os import system
    from sys import platform
    from analise_musica import *
except ImportError as error:
    print("Import Error : %s" %error)

def apagar_terminal():
    """Identifica o sistema atual para usar o comando certo"""

    if platform.startswith("linux"):
        system("clear")
    elif platform.startswith("win32"):
        system("CLS")

def opcoes(escolha):
    """Recebe a escolha do usuario e retorna o que foi pedido"""

    if escolha == 1:
        musica = input("Digite o nome da música: ")
        apagar_terminal()
        analise_musica(musica)
    elif escolha == 2:
        musica = input("Digite o nome da música que deseja procurar: ")
        apagar_terminal()
        buscar_musica(musica)
    elif escolha == 3:
        musica_link = input("Informe o link do vídeo: ")
        apagar_terminal()
        baixar_musica(musica_link)
    elif escolha == 4:
        print("\n--------Saindo--------")
        return "Sair"
    else:
        print("Escolha uma opção válida")

def main():
    while True:
        print("--------Escolha a operação desejada--------\n")

        print("1 - Analisar uma música.\n"
              "2 - Procurar por uma música.\n"
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
from modos.retro import modo_retro
from modos.treino import modo_treino
from core.utils import escolher_tabuada

def menu():

    while True:

        print("+=================================================+")
        print("|               TABUADA RETRÔ                     |")
        print("+=================================================+")

        print("1 - Modo Retrô")
        print("2 - Modo Treino")
        print("3 - Modo Desafio")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            numero = escolher_tabuada()
            modo_retro(numero)

        elif opcao == "2":
            numero = int(input("Escolha a Tabuada"))
            modo_treino(numero)
            

        elif opcao == "3":
            print("\n🚧 Em desenvolvimento...\n")
            input("Pressione Enter...")

        elif opcao == "0":
            print("\nAté a próxima!")
            break

        else:
            print("\nOpção inválida.")
            input("Pressione Enter...")
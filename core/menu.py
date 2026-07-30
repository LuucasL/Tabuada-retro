from modos.retro import modo_retro

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
            modo_retro()

        elif opcao == "2":
            print("\n🚧 Em desenvolvimento...\n")
            input("Pressione Enter...")

        elif opcao == "3":
            print("\n🚧 Em desenvolvimento...\n")
            input("Pressione Enter...")

        elif opcao == "0":
            print("\nAté a próxima!")
            break

        else:
            print("\nOpção inválida.")
            input("Pressione Enter...")
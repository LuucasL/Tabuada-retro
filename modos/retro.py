from core.utils import limpar, cabecalho

def modo_retro():

    limpar()

    cabecalho()

    numero = int(input("Escolha a tabuada: "))

    for i in range(1, 11):

        limpar()

        cabecalho()

        print(f"\n{numero} x {i} = ?")

        input("\nPressione Enter para revelar...")

        print(f"\n{numero} x {i} = {numero * i}")

        input("\nPressione Enter para continuar...")

    limpar()

    print("Fim da Tabuada!")

    input("\nPressione Enter para voltar ao menu...")
from core.utils import limpar, cabecalho

def modo_retro(numero):

    limpar()

    cabecalho()

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
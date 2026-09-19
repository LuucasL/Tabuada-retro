from core.utils import limpar, cabecalho

def modo_retro(numero):
    
    limpar()

    cabecalho()
    
    for i in range(1, 11):

        limpar()

        cabecalho()
       
        print(f"\n{numero} x {i} = ?")

        input("\nPressione Enter para revelar...")

        limpar()
        cabecalho()

        print(f"\n {numero * i}")

        input("\nPressione Enter para continuar...")

    limpar()
    cabecalho()

    print("Fim da Tabuada!")

    input("\nPressione Enter para voltar ao menu...") 
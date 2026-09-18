from core.utils import limpar



def modo_treino(numero):

    acertos = 0

    limpar()

    for i in range(1, 11):
            limpar()
            
            print(f"\n questão {i} de 10")
            print(f"\n{numero} x {i} = ?")

            resposta = int(input("Resposta: "))

            resultado = numero * i

            if resposta == resultado:
                print("\n Resposta correta!")
                acertos += 1
            else:
                print("\n Resposta incorreta!")
                print(f"\nO resultado correto é: {resultado}")
    erros = 10 - acertos     
    limpar()

    print("\n==============================")
    print("          RESULTADO           ")
    print("==============================")
    print(f"\nTabuada escolhida: {numero}")
    print(f"\n acertos: {acertos} de 10!")
    print(f"\n erros: {erros}")
    input("\n Pressione Enter para continuar...")

import os

def limpar():

    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def cabecalho():

    print("+=================================================+")
    print("|               TABUADA RETRÔ                     |")
    print("+=================================================+")
import os
from time import sleep


def cabeçalho(txt, sinal="==="):
    limpartela()
    cor = "\033[31m"
    reset = "\033[0m"
    sn = sinal
    sncor = f"{cor}{sn}{reset}"
    l1 = sncor * len(txt)
    print(f"{cor}{l1:^20}{reset}")
    print(f"{cor}{txt:^20}{reset}")
    print(f"{cor}{l1:^20}{reset}")

def limpartela():
    os.system("cls" if os.name == "nt" else "clear")


def linha(tp="=", qtde=20):
    cor = "\033[31m"
    reset = "\033[0m"
    sn = tp
    sncor = f"{cor}{sn}{reset}"

    if qtde == 20:
        print(sncor*qtde)
    else:
        print(sncor*qtde)



def estatistica(kills=0,deaths=0):
    derrotados = kills
    morto = deaths
    print(f"VOÇÊ MORREU {morto} VEZES")
    print(f"VOCÊ MATOU {derrotados} INIMIGOS")


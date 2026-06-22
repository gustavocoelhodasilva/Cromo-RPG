import os
from time import sleep


def cabeçalho(txt, sinal="==="):
    limpartela()
    l1 = sinal * len(txt)
    print(f"{l1:^20}")
    print(f"{txt:^20}")
    print(f"{l1:^20}")

def limpartela():
    os.system("cls" if os.name == "nt" else "clear")


def linha(tp="=", qtde=20):
    if qtde == 20:
        print(tp*qtde)
    else:
        print(tp*qtde)



def estatistica(kills=0,deaths=0):
    derrotados = kills
    morto = deaths
    print(f"VOÇÊ MORREU {morto} VEZES")
    print(f"VOCÊ MATOU {derrotados} INIMIGOS")


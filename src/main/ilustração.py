import os
from time import sleep
def cabeçalho(txt, sinal="="):
    limpartela()
    global cor, reset
    cor = "\033[31m"
    reset = "\033[0m"

  
    titulo = txt.upper()
    l1 = sinal * 40

    print(f"{cor}{l1:^20}{reset}")
    print(f"{cor}{txt.center(35)}{reset}")
    print(f"{cor}{l1:^20}{reset}")


def limpartela():
    os.system("cls" if os.name == "nt" else "clear")


def linha(tp="=", qtde=20):
    sn = tp
    sncor = f"{cor}{sn}{reset}"

    if qtde == 20:
        print(sncor*qtde)
    else:
        print(sncor*qtde)



def estatistica(kills=0,deaths=0):
    derrotados = kills
    morto = deaths
    limpartela()
    print(f"\033[36mESTATISTICA DE JOGO:\033[0m")
    linha()
    print(f"VOCÊ MORREU {cor}{morto}{reset} VEZES")
    linha()
    print(f"VOCÊ MATOU {cor}{derrotados}{reset} INIMIGOS")
    linha()
    print("\033[32mTIPO DE SOBREVIVENTE:\033[0m")
    linha()
    if derrotados == 0:
        print("\033[33mSOBREVIVENTE PACIFICO\033[0m")
        linha()
    elif derrotados < 10:
        print("\033[33mCAÇADOR MIRIM\033[0m")
        linha()
    elif derrotados > 10 and derrotados < 50:
        print("\033[33mBERSEKER\033[0m")
        linha()
    elif derrotados == 100:
        print("\033[33mEXTERMINADOR DO FUTURO\033[0m")
        linha()
    if morto == 100:
        print("\033[33mWILIAM AFTON\033[0m")
        linha()
    
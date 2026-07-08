from time import sleep
from ilustração import limpartela, cabeçalho, linha

# Variáveis globais
personagem = {}
ps = ""



def criar_personagem():
    global ps
    nm = input("\033[35mDigite o seu nome:\033[0m ").strip()
    if not nm:
        nm = "Sobrevivente"

    ps = nm
    sleep(1.5)
    cabeçalho(f"\t\t\tBem vindo ao futuro {ps}", sinal="**")
    sleep(2)
    limpartela()


def atributos(vida=100, defesa=4, ataque=1000, cura=10, xp=0, nivel=0):
    global personagem, ps

    personagem["nome"] = ps
    personagem["vida"] = vida
    personagem["defesa"] = defesa
    personagem["ataque"] = ataque
    personagem["cura"] = cura
    personagem["xp"] = xp
    personagem["nivel"] = nivel
atributos()

def nivel(xp=0):
    personagem["xp"] += xp
    nivel = (personagem["xp"] // 10) + 1
   
    print(f"seu nivel é {nivel}")
    

    




















def mostrar_atributos():
    cabeçalho("STATUS INICIAL", sinal="=")
    sleep(2)
    largura = 35
    cor1 = "\033[33m"
    cor2 = "\033[1;34m"
    reset = "\033[0m"
    for k, v in personagem.items():
        print(f"{cor1}{k.capitalize():^20}{reset}: {cor2}{v:^10}{reset}")
        linha(tp="--")
        sleep(0.3)
    linha("==")
    sleep(4)


def iniciar_jogador():
    global personagem, ps
    ps = ""

    criar_personagem()
    atributos()
    mostrar_atributos()


def get_ps():
    return ps


def get_personagem():
    return personagem


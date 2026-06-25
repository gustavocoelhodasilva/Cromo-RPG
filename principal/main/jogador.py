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
    cabeçalho(f"Bem vindo ao futuro {ps}", sinal="*")
    sleep(2)
    limpartela()


def atributos(vida=100, defesa=4, ataque=20, cura=5, xp=10, nivel=1):
    global personagem, ps
    personagem["nome"] = ps
    personagem["vida"] = vida
    personagem["defesa"] = defesa
    personagem["ataque"] = ataque
    personagem["cura"] = cura
    personagem["xp"] = xp
    personagem["nivel"] = nivel


def mostrar_atributos():
    cabeçalho("\033[36mSTATUS INICIAL\033[0m", sinal="=+")
    sleep(2)
    for k, v in personagem.items():
        print(f"\033[33m{k.capitalize()}:\033[0m \033[1;34m{v}\033[0m")
        sleep(0.3)
    linha("=")
    sleep(1)


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
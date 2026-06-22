from time import sleep

from ilustração import limpartela, cabeçalho, linha

# Variáveis globais
personagem = {}
ps = ""


def criar_personagem():
    global ps
    nm = input("Digite o seu nome: ").strip()
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
    cabeçalho("STATUS INICIAL", sinal="=+")
    sleep(2)
    for k, v in personagem.items():
        print(f"{k.capitalize()}: {v}")
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
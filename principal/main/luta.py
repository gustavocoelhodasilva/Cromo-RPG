import os
import sys
_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
while _root and not os.path.exists(os.path.join(_root, 'principal')):
    _parent = os.path.dirname(_root)
    if _parent == _root: break
    _root = _parent
if _root not in sys.path: sys.path.append(_root)
if os.path.join(_root, 'principal') not in sys.path: sys.path.append(os.path.join(_root, 'principal'))

import random
from time import sleep
from sys import exit
from jogador.jogador import get_ps, get_personagem
from inimigo.inimigo import criarinimigo
from ilustração.ilustração import limpartela, estatistica
from cenario.cenario import mudarcenario, escolhe

fuga = (1,2,3,4,5)

def calcular_ataque(atacante, defensor):
    dano = atacante["ataque"] - defensor["defesa"]
    if dano < 1:
        dano = 1
    defensor["vida"] -= dano    
    return dano 


def executar_cura(quem_cura, vida=100):
    if quem_cura["vida"] < vida:
        quem_cura["vida"] += quem_cura["cura"]
    else:
        quem_cura["vida"] = vida
    return quem_cura["cura"]


def verifica_morte(entidade):
    return entidade.get("vida", 0) <= 0


def turno(nome_jogador, nome_inimigo="walker"):
    turn = [nome_jogador, nome_inimigo]
    random.shuffle(turn)
    return turn


def turno_inimigo(inimigo, jogador):
    print("\nVEZ DO INIMIGO:")
    sleep(1)
    
    escolha = random.choice(["atacar", "curar"])
    
    if escolha == "atacar":
        print("O INIMGO ESCOLHEU: ATACAR")
        dano = calcular_ataque(inimigo, jogador)
        print(f"O INIMIGO DEU {dano} DE DANO.")
        print(f"VIDA RESTANTE: {max(0, jogador.get('vida', 0))}HP")
    else:
        if inimigo["vida"] < 100:
            cura = executar_cura(inimigo)
            print(f"o inimigo se curou em {cura}")
        else:
            print("o inimigo tentou se curar mas tava de hp cheio")
    sleep(1.5)


def combate():
    global jogador
    jogador_original = get_personagem()
    if not jogador_original:
        # Fallback caso o jogador não tenha sido inicializado
        jogador = {"nome": "Teste", "vida": 100, "defesa": 4, "ataque": 20, "cura": 5}
    else:
        jogador = jogador_original.copy()
        
    nome = get_ps() or "Jogador"
    
    inimigo = criarinimigo()
    
    print("UM COMBATE COMEÇOU")
    sleep(1)
    
    while jogador.get("vida", 0) > 0 and inimigo.get("vida", 0) > 0:
        
        ordem = turno(nome, "walker")

        for atacante in ordem:
            limpartela()
            
            if atacante == nome:   # Vez do jogador
                print(f"VEZ DE {nome.upper()}:")
                mudarcenario("Atacar", "fugir")
                opcao = escolhe()

                if opcao == 0:
                    dano = calcular_ataque(jogador, inimigo)
                    print(f"{nome} deu {dano} de dano!")
                    print(f"O inimigo está com {inimigo['vida']} de HP\n")
                    sleep(2)
                
                elif opcao == 1:
                    print("Você tentou fugir!")
                    tentativa = random.choice(fuga)
                    if tentativa == 1:
                        print("você fugiu com sucesso")
                        exit()
                    else:
                        print("Mas não conseguiu")
                    sleep(1.5)
                
                elif opcao == 2:
                    exit()
                else:
                    print("opcao invalida")
                    sleep(1)

                if verifica_morte(inimigo):
                    print("VOCÊ DERROTOU O ROBÔ")
                    estatistica(kills=1)
                    return

            else:   # Vez do inimigo
                turno_inimigo(inimigo, jogador)

            # Checa morte do jogador
            if verifica_morte(jogador):
                estatistica(deaths=1)
                print("\nvocê morreu.")
                while True:
                    try:
                        per = input("tentar denovo? [s/n]").upper()[0]
                        if per in "SN":
                            break
                    except IndexError:
                        continue
                if per == "N":
                    exit()
                else:
                    jogador["vida"] = 100
                    inimigo["vida"] = 100
                    continue

    limpartela()

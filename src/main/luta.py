import random
from time import sleep
from sys import exit
from jogador import get_ps, get_personagem
from inimigo import criarinimigo
from ilustração import limpartela,linha
from cenario import mudarcenario, escolhe
from ilustração import estatistica
fuga = (1, 2, 3, 4, 5)

COR_PLAYER = "\033[1;32m"
COR_INIMIGO = "\033[34m"
COR_SISTEMA = "\033[33m"
RESET = "\033[0m"


def calcular_ataque(atacante, defensor):
    atk = random.randint(10, atacante["ataque"])
    print(f"Ataque bruto: {atk} | Defesa do alvo: {defensor['defesa']}")
    dano = atk - defensor["defesa"]
    if dano < 1:
        dano = 1
    defensor["vida"] -= dano
    return dano


def executar_cura(quem_cura, vida=100,inimi=True):
    if quem_cura["vida"] < vida:
        quem_cura["vida"] += quem_cura["cura"]
        sleep(1)
    else:
        quem_cura["vida"] = vida
        sleep(1)
    return quem_cura["cura"]


def verifica_morte(entidade):
    return entidade.get("vida", 0) <= 0


def turno(nome_jogador, nome_inimigo="walker"):
    turn = [nome_jogador, nome_inimigo]
    random.shuffle(turn)
    return turn


def turno_inimigo(inimigo, jogador):
    print(f"\033[36mVEZ DO INIMIGO:\033[0m")
    linha()
    sleep(1)

    escolha = random.choice(["atacar", "curar"])

    if escolha == "atacar":
        print(f"{COR_INIMIGO}O INIMGO ESCOLHEU:{RESET} \033[33mATACAR\033[0m")
        sleep(2)
        dano = calcular_ataque(inimigo, jogador)
        print(f"{COR_INIMIGO}O INIMIGO DEU: {RESET} \033[33m{dano} DE DANO.\033[0m")
        sleep(1)
        linha()
        print(f"{COR_SISTEMA}Sua vida restante: {max(0, jogador.get('vida', 0))}HP{RESET}")
        sleep(3)
    else:
        if inimigo["vida"] < 75:
            cura = executar_cura(inimigo)
            print(f"{COR_INIMIGO}O INIMIGO ACABA DE SE CURAR EM: {RESET}\033[32m{cura}\033[0mHP")
            print(f"\033[32mVida do inimigo: {inimigo["vida"]}\033[0m")
        else:
            print(f"{COR_INIMIGO}O INIMIGO TENTA SE CURAR. MAIS ESTA COM O HP CHEIO.{RESET}")
    sleep(1.5)


def combate():
    global jogador
    jogador = get_personagem().copy()
    nome = get_ps()

    inimigo = criarinimigo()

    print(f"{COR_SISTEMA}UM COMBATE COMEÇOU{RESET}")
    sleep(1)

    while jogador.get("vida", 0) > 0 and inimigo.get("vida", 0) > 0:

        ordem = turno(nome, "walker")

        for atacante in ordem:
            limpartela()

            if atacante == nome:
                print(f"{COR_PLAYER}VEZ DE {nome.upper()}:{RESET}")
                mudarcenario("Atacar", "Fugir","Curar")
                opcao = escolhe()

                if opcao == 0:
                    dano = calcular_ataque(jogador, inimigo)
                    print(f"{COR_PLAYER}{nome} deu {dano} de dano!{RESET}")
                    print(f"{COR_SISTEMA}O inimigo está com {inimigo['vida']} de HP\n{RESET}")
                    sleep(3)

                elif opcao == 1:
                    print(f"{COR_PLAYER}VOCÊ TENTA FUGIR{RESET}")
                    sleep(2)
                    tentativa = random.choice(fuga)
                    if tentativa == 1:
                        print(f"{COR_PLAYER}VOCÊ FUGIU COM SUCESSO!{RESET}")
                        exit()
                    else:
                        print(f"{COR_PLAYER}MAS NÃO CONSEGUIU{RESET}")
                    sleep(1.5)
                elif opcao  == 2:
                   if jogador["vida"] < 100:
                        cura = executar_cura(jogador)
                        print(f"{COR_PLAYER}VOCÊ ACABA DE SE CURAR EM: {RESET}\033[32m{cura}\033[0mHP")
                        print(f"\033[32mSua vida: {jogador["vida"]}\033[0m")
                        sleep(3)
                   else:
                        print(f"{COR_PLAYER}VOCÊ TENTA SE CURAR. MAIS ESTA COM O HP CHEIO.{RESET}")
                        sleep(3)
                       
                elif opcao == 3:
                    print("fechando jogo...")
                    exit()
                else:
                    print(f"{COR_SISTEMA}Opcao INVALIDA{RESET}")
                    sleep(1)

                if verifica_morte(inimigo):
                    print(f"{COR_SISTEMA}VOCÊ DERROTOU O ROBÔ{RESET}")
                    linha()
                    estatistica(kills=1)
                    return

            else:
                turno_inimigo(inimigo, jogador)

            if verifica_morte(jogador):
                estatistica(deaths=1)
                print(f"\n{COR_SISTEMA}VOCÊ MORREU{RESET}")
                while True:
                    per = input(f"{COR_SISTEMA}Tentar denovo? [s/n]{RESET}").upper()
                    if per in "SN":
                        break
                if per == "N":
                    exit()
                else:
                    jogador["vida"] = 100
                    inimigo["vida"] = 100
                    continue

    limpartela()

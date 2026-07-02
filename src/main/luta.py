import random
from time import sleep
from sys import exit
from jogador import get_ps, get_personagem
from inimigo import criarinimigo
from ilustração import limpartela,linha
from cenario import mudarcenario, escolhe
from ilustração import estatistica
fuga = (1, 2, 3, 4, 5)
chance = (1,2,3)

COR_PLAYER = "\033[1;32m"
COR_INIMIGO = "\033[34m"
COR_SISTEMA = "\033[33m"
RESET = "\033[0m"


def calcular_ataque(atacante=None, defensor=None, is_player=True, nome_atacante=""):
    """
    Executa um ataque de 'atacante' contra 'defensor' e imprime todo o
    diálogo do ataque (jogador ou inimigo, conforme is_player).

    atacante/defensor: dicts com "ataque"/"defesa"/"vida". Se não forem
        passados, usa as globais jogador/inimigo com base em is_player.
    is_player: True se quem ataca é o jogador, False se é o inimigo.
    nome_atacante: nome exibido no diálogo quando is_player=True.
    """
    global jogador, inimigo
    if atacante is None:
        atacante = jogador if is_player else inimigo
    if defensor is None:
        defensor = inimigo if is_player else jogador

    if not is_player:
        print(f"{COR_INIMIGO}O INIMGO ESCOLHEU:{RESET} \033[33mATACAR\033[0m")
        sleep(2)


    desvio = (1,2,3)
    if random.choice(desvio) == 3:
        if is_player:
            print(f"{COR_INIMIGO}O INIMIGO ESQUIVA DO SEU ATAQUE {RESET}")
            sleep(3)
        else:
            print(f"{COR_INIMIGO}VOCÊ ESQUIVOU DO ATAQUE INIMIGO {RESET}")
            sleep(3)
        return 0
    



    atk = random.randint(10, atacante["ataque"])
    print(f"Ataque bruto: {atk} | Defesa do alvo: {defensor['defesa']}")
    dano = atk - defensor["defesa"]
    if dano < 0:
        dano = 0
    defensor["vida"] -= dano

    if is_player:
        print(f"{COR_PLAYER}{nome_atacante} deu {dano} de dano!{RESET}")
        print(f"{COR_SISTEMA}O inimigo está com {defensor['vida']} de HP\n{RESET}")
        sleep(3)
    else:
        print(f"{COR_INIMIGO}O INIMIGO DEU: {RESET} \033[33m{dano} DE DANO.\033[0m")
        sleep(1)
        linha()
        print(f"{COR_SISTEMA}Sua vida restante: {max(0, defensor.get('vida', 0))}HP{RESET}")
        sleep(3)

    return dano









def executar_cura(quem_cura, status, is_player=True, vida_maxima=100):
    """
    status:
        "sucesso"   -> a cura pode ser aplicada
        "cheio"     -> quem tenta curar já está com o HP cheio
        "bloqueado" -> (apenas jogador) a cura foi impedida pelo inimigo
    """
    if status == "sucesso":
        if quem_cura["vida"] < vida_maxima:
            quem_cura["vida"] += quem_cura["cura"]
            sleep(1)
        else:
            quem_cura["vida"] = vida_maxima
            sleep(1)

        if is_player:
            print(f"{COR_PLAYER}VOCÊ ACABA DE SE CURAR EM: {RESET}\033[32m{quem_cura['cura']}\033[0mHP")
            print(f"\033[32mSua vida: {quem_cura['vida']}\033[0m")
            sleep(3)
        else:
            print(f"{COR_INIMIGO}O INIMIGO ACABA DE SE CURAR EM: {RESET}\033[32m{quem_cura['cura']}\033[0mHP")
            print(f"\033[32mVida do inimigo: {quem_cura['vida']}\033[0m")
            sleep(1.5)

    elif status == "cheio":
        if is_player:
            print(f"{COR_PLAYER}VOCÊ TENTA SE CURAR. MAS ESTA COM O HP CHEIO.{RESET}")
            sleep(3)
        else:
            print(f"{COR_INIMIGO}O INIMIGO TENTA SE CURAR. MAIS ESTA COM O HP CHEIO.{RESET}")
            sleep(1.5)

    elif status == "bloqueado":
        print(f"{COR_PLAYER}VOCê TENTA SE CURAR. MAS O INIMIGO NÃO DA BRECHA{RESET} ")
        sleep(3)

    return quem_cura.get("cura", 0)


def verifica_morte(entidade):
    """Retorna True se a vida da entidade (jogador ou inimigo) chegou a 0 ou menos."""
    return entidade.get("vida", 0) <= 0


def turno(nome_jogador, nome_inimigo="walker"):
    """Sorteia a ordem de ação entre jogador e inimigo neste round."""
    turn = [nome_jogador, nome_inimigo]
    random.shuffle(turn)
    return turn


def turno_inimigo(inimigo, jogador):
    """
    Executa a ação do inimigo no turno: sorteia entre atacar, curar ou
    esquivar e chama a função correspondente.
    """
    nome_inimigo = inimigo.get("nome", "INIMIGO")
    print(f"\033[36mVEZ DE {nome_inimigo.upper()}:\033[0m")
    linha()
    sleep(1)
    escolha = random.choice(["atacar", "curar"])

    if escolha == "atacar":
        calcular_ataque(inimigo, jogador, is_player=False)


    elif escolha == "curar":
        status = "sucesso" if inimigo["vida"] < 75 else "cheio"
        executar_cura(inimigo, status, is_player=False)


def combate():
    """Loop principal do combate: alterna turnos entre jogador e inimigo até um dos dois morrer."""
    global jogador,inimigo
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
                    calcular_ataque(jogador, inimigo, is_player=True, nome_atacante=nome)

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
                   curachance = random.choice(chance)
                   if jogador["vida"] < 100 and curachance == 2:
                       status = "sucesso"
                   elif jogador["vida"] == 100:
                       status = "cheio"
                   else:
                       status = "bloqueado"
                   executar_cura(jogador, status, is_player=True)

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
import random
import items
from time import sleep
from sys import exit
from jogador import get_ps, get_personagem
from inimigo import criarinimigo
from ilustração import limpartela, linha
from cenario import mudarcenario, escolhe
from ilustração import estatistica
from inventario import inventario,exibiritemns

fuga = (1, 2, 3, 4, 5, 6)
chance = (1, 2, 3, 4)
moedas = random.randint(0,10)
matou = 0
morreu = 0
COR_PLAYER = "\033[1;32m"
COR_INIMIGO = "\033[1;31m"
COR_SISTEMA = "\033[1;33m"
COR_AÇÃO = "\033[1;34m"
COR_MENU = "\033[1;36m"
RESET = "\033[0m"
BOLD = "\033[1m"


def calcular_ataque(atacante=None, defensor=None, is_player=True, nome_atacante=""):
    global jogador, inimigo
    if atacante is None:
        atacante = jogador if is_player else inimigo
    if defensor is None:
        defensor = inimigo if is_player else jogador

    if not is_player:
        print(f"\n{COR_INIMIGO}╔══════════════════════════════════════╗{RESET}")
        print(f"{COR_INIMIGO}║   O INIMIGO PREPARA UM ATAQUE!       ║{RESET}")
        print(f"{COR_INIMIGO}╚══════════════════════════════════════╝{RESET}")
        sleep(1.5)

    # Chance de esquiva
    desvios = (1, 2, 3)
    if random.choice(desvios) == 3:
        if is_player:
            print(f"\n{COR_INIMIGO}╔══════════════════════════════════════╗{RESET}")
            print(f"{COR_INIMIGO}║  O inimigo SE ESQUIVOU do seu golpe! ║{RESET}")
            print(f"{COR_INIMIGO}╚══════════════════════════════════════╝{RESET}")
        else:
            print(f"\n{COR_PLAYER}╔══════════════════════════════════════╗{RESET}")
            print(f"{COR_PLAYER}║     Você se ESQUIVOU com sucesso!    ║{RESET}")
            print(f"{COR_PLAYER}╚══════════════════════════════════════╝{RESET}")
        sleep(2.5)
        return 0

    atk = random.randint(10, atacante["ataque"])
    dano = max(0, atk - defensor["defesa"])
    defensor["vida"] -= dano
    limpartela()
    print(f"\n{COR_AÇÃO}╔════════════════════════════════════════╗{RESET}")
    if is_player:
        print(f"{COR_PLAYER}║   {nome_atacante.upper()} DESFERE UM GOLPE PODEROSO!  {RESET}")
        print(f"{COR_AÇÃO}╠═══════════════════════════════════════╣{RESET}")
        print(f" Dano causado: {BOLD}{dano}{RESET} | Defesa do inimigo: {defensor['defesa']}")
        print(f"\n{COR_SISTEMA}  Inimigo agora tem {max(0, defensor['vida'])} HP{RESET}")
    else:
        print(f"{COR_INIMIGO}║     O INIMIGO ACERTA VOCÊ!           ║{RESET}")
        print(f"{COR_AÇÃO}╠═════════════════════════════════════════╣{RESET}")
        print(f"   Dano recebido: {BOLD}{dano}{RESET} | Sua defesa: {defensor['defesa']}")
        print(f"\n{COR_SISTEMA}   Sua vida restante: {max(0, defensor['vida'])} HP{RESET}")
    print(f"{COR_AÇÃO}╚════════════════════════════════════════╝{RESET}")
    sleep(4)

    return dano


def executar_cura(quem_cura, status, is_player=True):
    print(f"\n{COR_AÇÃO}╔══════════════════════════════════════╗{RESET}")
    
    if status == "sucesso":
        vida_total = 75
        if quem_cura["vida"] < vida_total:
            quem_cura["vida"] += quem_cura["cura"]
            if quem_cura["vida"] > vida_total:
                quem_cura["vida"] = vida_total

        if is_player:
            print(f"{COR_PLAYER}║     CURA APLICADA COM SUCESSO!       ║{RESET}")
            print(f"   Recuperou {quem_cura['cura']} HP | Vida atual: {quem_cura['vida']} HP")
        else:
            print(f"{COR_INIMIGO}║     O INIMIGO SE RECUPEROU!          ║{RESET}")
            print(f"     Vida do inimigo: {quem_cura['vida']} HP")
       

    elif status == "cheio":
        if is_player:
            print(f"{COR_PLAYER}║     SUA VIDA JÁ ESTÁ NO MÁXIMO       ║{RESET}")
        else:
            print(f"{COR_INIMIGO}║   INIMIGO JÁ ESTÁ TOTALMENTE CURADO  ║{RESET}")
       
    elif status == "bloqueado":
        print(f"{COR_INIMIGO}║  CURA BLOQUEADA PELO INIMIGO!        ║{RESET}")
        
        
    print(f"{COR_AÇÃO}╚══════════════════════════════════════╝{RESET}")
    sleep(2.5)

def verifica_morte(entidade):
    return entidade.get("vida", 0) <= 0


def turno(nome_jogador, nome_inimigo="walker"):
    turn = [nome_jogador, nome_inimigo]
    random.shuffle(turn)
    return turn


def turno_inimigo(inimigo, jogador):
    nome_inimigo = inimigo.get("nome").upper()
    print(f"\n{COR_INIMIGO}╔══════════════════════════════════════╗{RESET}")
    print(f"{COR_INIMIGO}║      VEZ DE {nome_inimigo:<18}       ║{RESET}")
    print(f"{COR_INIMIGO}╚══════════════════════════════════════╝{RESET}")
    sleep(1.3)

    escolha = random.choice(["atacar", "curar"])
    if escolha == "atacar":
        calcular_ataque(inimigo, jogador, is_player=False)
    elif escolha == "curar":
        status = "sucesso" if inimigo["vida"] < 75 else "cheio"
        executar_cura(inimigo, status, is_player=False)


def combate(robo="comum",qtd=0):
    global jogador, inimigo, chance, fuga, moedas,matou,morreu
    jogador = get_personagem().copy()
    vida_maxima_jogador = jogador.get("vida", 100)
    nome = get_ps()
    inimigo = criarinimigo(robo)

    limpartela()
    print(f"{COR_SISTEMA}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{COR_SISTEMA}║                    O COMBATE COMEÇOU                         ║{RESET}")
    print(f"{COR_SISTEMA}╚══════════════════════════════════════════════════════════════╝{RESET}")
    sleep(2)

    while jogador.get("vida", 0) > 0 and inimigo.get("vida", 0) > 0:
        ordem = turno(nome, "walker")
        
        for atacante in ordem:
            if verifica_morte(jogador) or verifica_morte(inimigo):
                break
                
            limpartela()
     
            if atacante == nome:
                # Menu do jogador alinhado
                print(f"{COR_AÇÃO}╔══════════════════════════════════════════════════════════════╗{RESET}")
                print(f"{COR_AÇÃO}║                     SUA VEZ - {nome.upper():<25}      ║{RESET}")
                print(f"{COR_AÇÃO}╠══════════════════════════════════════════════════════════════╣{RESET}")
                print(f"   {COR_PLAYER}Sua Vida{RESET}     : {jogador['vida']} HP")
                print(f"   {COR_INIMIGO}Vida Inimigo{RESET} : {inimigo['vida']} HP")
                print(f"{COR_AÇÃO}╠══════════════════════════════════════════════════════════════╣{RESET}")
                print(f"{COR_MENU}   [0] ⚔️  Atacar")
                print(f"   [1] 🏃 Fugir")
                print(f"   [2] ❤️  Curar")
                print(f"   [3] 🎒 Inventário")
                print(f"   [4] Sair{RESET}")
                print(f"                                               {COR_AÇÃO}Inimigo nº {qtd} {RESET}")
                print(f"{COR_AÇÃO}╚══════════════════════════════════════════════════════════════╝{RESET}")
                
                mudarcenario("Atacar", "Fugir", "Curar", "Inventario")
                opcao = escolhe()
              
                if opcao == 0:  # Atacar
                    calcular_ataque(jogador, inimigo, is_player=True, nome_atacante=nome)

                elif opcao == 1:  # Fugir
                    print(f"\n{COR_SISTEMA}Você procura uma brecha para escapar...{RESET}")
                    sleep(1.5)
                    tentativa = random.choice(fuga)
                    if tentativa == 1:
                        print(f"\n{COR_PLAYER}╔══════════════════════════════════════╗{RESET}")
                        print(f"{COR_PLAYER}║     FUGA BEM SUCEDIDA!               ║{RESET}")
                        print(f"{COR_PLAYER}╚══════════════════════════════════════╝{RESET}")
                        sleep(1.5)
                        exit()
                    else:
                        print(f"\n{COR_INIMIGO}O inimigo bloqueia sua fuga!{RESET}")
                    sleep(2)

                elif opcao == 2:  # Curar
                    curachance = random.choice(chance)
                    if jogador["vida"] < vida_maxima_jogador and curachance == 2:
                        status = "sucesso"
                    elif jogador["vida"] == vida_maxima_jogador:
                        status = "cheio"
                    else:
                        status = "bloqueado"
                    executar_cura(jogador, status, is_player=True)
                
                elif opcao == 3:  # Inventário
                    inv = inventario()
                    if inv:
                        nomes = [t[0] for t in items.SERINGAS]
                        if inv.get("nome") in nomes:
                            if inv["tipo"] == "dano":
                                jogador["ataque"] += inv["efeito"]
                                print(f"\n{COR_PLAYER}╔══════════════════════════════════════╗{RESET}")
                                print(f"{COR_PLAYER}║  SERINGA DE DANO APLICADA!           ║{RESET}")
                                print(f"   Ataque aumentado em +{inv['efeito']}!")
                                print(f"{COR_PLAYER}╚══════════════════════════════════════╝{RESET}")
                            elif inv["tipo"] == "cura":
                                jogador["vida"] += inv["efeito"]
                                if jogador["vida"] > vida_maxima_jogador:
                                    jogador["vida"] = vida_maxima_jogador
                                print(f"\n{COR_PLAYER}╔══════════════════════════════════════╗{RESET}")
                                print(f"{COR_PLAYER}║     SERINGA DE CURA USADA!           ║{RESET}")
                                print(f"   Recuperou +{inv['efeito']} HP")
                                print(f"{COR_PLAYER}╚══════════════════════════════════════╝{RESET}")
                            elif inv["tipo"] == "sorte":
                                metade_chance = len(chance) // 2
                                metade_fuga = len(fuga) // 2
                                chance = chance[:metade_chance]
                                fuga = fuga[:metade_fuga]
                                moedas = moedas * 2
                                print(f"\n{COR_PLAYER}╔══════════════════════════════════════╗{RESET}")
                                print(f"{COR_PLAYER}║     SERINGA DA SORTE APLICADA!       ║{RESET}")
                                print(f"  Sua sorte aumentou significativamente!")
                                print(f"{COR_PLAYER}╚══════════════════════════════════════╝{RESET}")
                            sleep(2.5)
                            
                elif opcao == 4:
                    print(f"\n{COR_SISTEMA}Encerrando o jogo...{RESET}")
                    sleep(1)
                    exit()
                else:
                    print(f"\n{COR_SISTEMA}Opção inválida. Escolha com atenção.{RESET}")
                    sleep(1.5)

                if verifica_morte(inimigo):
                    print(f"\n{COR_PLAYER}╔══════════════════════════════════════╗{RESET}")
                    print(f"{COR_PLAYER}║VITÓRIA! {inimigo["nome"]} DERROTADO!║{RESET}")
                    print(f"{COR_PLAYER}╚══════════════════════════════════════╝{RESET}")
                    
                    print(f"\n{COR_SISTEMA}O inimigo te transferiu {moedas} CriptoMoedas{RESET}")
                    sleep(2)
                    
                    for fileira, item  in enumerate(items.ITENS):
                        nome,tipo,efeito,qtde = item
                        if nome == "CriptoMoedas":
                            novaqtde = moedas + qtde
                            print(f"{COR_SISTEMA}Agora Você possui {novaqtde} de CriptoMoedas{RESET}")
                            sleep(4)
                            items.ITENS[fileira] = (nome,tipo,efeito,novaqtde)
                    matou += 1
                    horda = str(qtd)
                    
                    if horda[-1] == "0" or horda[-1] == "5" or horda == "16":
                        op = input(f"{COR_SISTEMA}Você quer enfrentar a horda de droides?[s/n]{RESET} ").strip()[0]
                        
                        while True:
                            if op == "s":
                                return "continue"
                            elif op == "n":
                                exibiritemns("EM BREVE")
                                sleep(3)
                                exit()
                            else:
                                print("Digite s ou n corretamente")
                                sleep(2)






            else:
                turno_inimigo(inimigo, jogador)

            if verifica_morte(jogador):
              
                print(f"\n{COR_INIMIGO}╔══════════════════════════════════════╗{RESET}")
                print(f"{COR_INIMIGO}║        VOCÊ FOI DERROTADO...         ║{RESET}")
                print(f"{COR_INIMIGO}╚══════════════════════════════════════╝{RESET}")
                morreu += 1
                
                
                while True:
                    per = input(f"{COR_SISTEMA}Deseja tentar novamente? [s/n]: {RESET}").strip().upper()
                    if per in ["S", "N"]:
                        break
                if per == "N":
                    exit()
                else:
                    jogador["vida"] = vida_maxima_jogador
                    print(f"\n{COR_AÇÃO}Reiniciando o combate... Boa sorte.{RESET}")
                    sleep(2)
                    break
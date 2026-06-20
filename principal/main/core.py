from time import sleep
import os
from sys import exit
import random
cenarios = [
    ["Sair da capsula", "Caminhar até a cidade"]  # inicial


]

personagem = {}

def estatistica(kills=0,deaths=0):
    derrotados = kills
    morto = deaths
    print(f"VOÇÊ MORREU {derrotados} VEZES")
    print(f"VOCÊ MATOU {morto} INIMIGOS")



def cabeçalho(txt, sinal="==="):
    l1 = sinal * len(txt)
    print(f"{l1:^20}")
    print(f"{txt:^20}")
    print(f"{l1:^20}")


def linha(tp="=", qtde=20):
    if qtde == 20:
        print(tp*qtde)
    else:
        print(tp*qtde)


def inicio():
    sleep(2)
    print("EM UM FUTURO DISTANTE ALGO ACONTECE")
    sleep(2)
    os.system("cls")


def criarpersonagem(txt):
    global ps
    ps = txt
    sleep(2)
    cabeçalho(f"Bem vindo ao futuro {ps}", sinal="*")
    sleep(3)
    os.system("cls")
    



def atributos(vida=100, defesa=4, ataque=20, cura=5, xp=10, nivel=1):
    personagem["vida"] = vida
    personagem["defesa"] = defesa
    personagem["ataque"] = ataque
    personagem["cura"] = cura
    personagem["xp"] = xp
    personagem["nivel"] = nivel


def mostraratributos():
    cabeçalho("STATUS INICIAL", sinal="=+")
    sleep(3)
    for k, v in personagem.items():
        print(f"{k}: {v}")
        sleep(0.3)
    linha("=")

def verificarnumero(prompt=">>>>"):
    while True:
        try:
            n = int(input(prompt))
            return n
        except:
            print("Digite apenas numeros")
        


def arrumarlista():
    for lista in cenarios:
        if "Sair" not in lista:
            lista.append("Sair")
        else:
            lista.remove("Sair")
    


def mostraropcoes():
     for lista in cenarios: 
        for c, op in enumerate(lista):
            print(f"{c:.<10} {op}")
     
def escolhe():
   mostraropcoes()
   opcao  =  verificarnumero(">>>>>")
   return opcao




def inicial():
    arrumarlista()
    while True:
        opcao = escolhe()
        if opcao == 0: 
            sleep(1)
            print("VOCÊ VE UM MUNDO INCRIVEL E NÃO ACREDITA EM SEUS OLHOS O MUNDO MUDOU TANTO")    
            sleep(3)
            os.system("cls")
            sleep(2)
            print("mas")
            sleep(2)
            os.system("cls")
            sleep(2)
            print("porque...")
            sleep(2)
            os.system("cls")
        elif opcao == 1:
            print("Você decide caminhar até a megacidade")
            sleep(2)
            break
            os.system("cls")
        elif opcao == 2:
            print("fechando o jogo")
            exit()
        else:
            print("opção invalida")
    os.system("cls")



def cidade():
    print("Você vê um cenario caótico")
    sleep(1)
    print("Predios combrem o céu")
    sleep(1)   
    print("arvores não existem")  
    sleep(1)  
    print("Cadê as pessoas")
    sleep(1)
    print("Apenas telas gigantes")
    sleep(1)
    print("o mundo é dos robôs e não existe mais humanidade")
    sleep(1)
    os.system("cls")
    sleep(1)
    print("Derrepente você no desespero tromba em um robô")
    sleep(1)
    print("O derrubando..")
    sleep(1)
    print("o robo se estressa")
    sleep(0.5)
    print("e então: ")



# === CORREÇÃO DO DICSTATUS ===
def dicstatus(
    ataque=20,
    vida=75,
    defesa=5,
    cura=3,
    segundaforma=False,
    furia=False,
    fatordecura=False,
):
    # Se for Boss (Segunda forma + Fúria)
    if segundaforma == True:
        walkerboss = dict()
        walkerboss["ataque"] = ataque + 3
        walkerboss["defesa"] = defesa + 1
        walkerboss["cura"] = cura + 3
        walkerboss["vida"] = vida * 2
        walkerboss["furia"] = ataque * 2
        return walkerboss

    elif furia == True:
        walkerraivoso = dict()
        walkerraivoso["ataque"] = ataque
        walkerraivoso["defesa"] = defesa
        walkerraivoso["cura"] = cura
        walkerraivoso["vida"] = vida
        walkerraivoso["furia"] = ataque * 2
        return walkerraivoso

    elif fatordecura == True:
        walkermedico = dict()
        walkermedico["ataque"] = ataque
        walkermedico["defesa"] = defesa + 4
        walkermedico["cura"] = cura * 2
        walkermedico["vida"] = vida + 5
        return walkermedico

    else:
        # Walker Comum normal
        walker = dict()
        walker["ataque"] = ataque
        walker["defesa"] = defesa
        walker["cura"] = cura
        walker["vida"] = vida
        return walker


walkercomum = dicstatus()
walkerboss = dicstatus(segundaforma=True, furia=True)
walkermedico = dicstatus(fatordecura=True)

def calcular_ataque(atacante,defensor):
    dano = atacante["ataque"] - defensor["defesa"]
    if dano < 1:
        dano = 1
    defensor["vida"] -= dano    
    return dano 
def executar_cura(quem_cura,vida=100):
    if quem_cura["vida"] < vida:
        quem_cura["vida"] += quem_cura["cura"]
    else:
        quem_cura["vida"] = vida
    return quem_cura["cura"]

def verifica_morte(entidade):
    if entidade["vida"] <= 0:
        return True
    return False



def combate(inimigo=False, opional=False):
    global jogador
    jogador = personagem
    print("UM COMBATE COMEÇOU")
    
    acoes_inimgo = ["atacar", "curar"]
 
    while jogador["vida"] > 0 and walkercomum["vida"] > 0:
       

       

        ordem = turno(jogador=ps, inimigo=True, nomeini="walker")
    

        for atacante in ordem:
            if atacante == ps:
                print(f"VEZ DE {ps.upper()}:")
                mudarcenario("Atacar", "fugir")
                opcao = escolhe()

                if opcao == 0:
                    dano = calcular_ataque(jogador, walkercomum)
                    print(f"{ps} deu {dano} de dano!")
                    print(
                        f"O inimigo está com {walkercomum['vida']} de HP\n"
                    )
                    sleep(2)
                    os.system("cls")
                
                elif opcao == 1:
                    print("Você tentou fugir!")
                    print("Mas não conseguiu")
                    
                
                elif opcao == 2:
                    exit()
                else:
                    print("opcao invalida")


                if verifica_morte(walkercomum) == True:
                    print("VOCÊ DERROTOU O ROBÔ")
                    count = 0
                    count += 1
                    estatistica(kills=count)


            turno_inimigo(walkercomum,*acoes_inimgo)
            
            if verifica_morte(jogador) == True:
                c = 0
                c += 1
                estatistica(deaths=c)
                while True:
                    per= input("você morreu. tentar denovo? [s/n]").upper()[0]
                    if per in "SN":
                        break
                    print("resposta invalida")    
                if per == "N":
                    exit()        
                else:
                    jogador["vida"] = 100
                    walkercomum["vida"] = 100
                    continue
                    



















def turno_inimigo(inimigo,*acoes):
    print("VEZ DO INIMIGO:")
    

    escolha = random.choice(acoes)
                        
    if escolha == "atacar":
        print(f"O INIMGO ESCOLHEU: ATACAR")
        escudo = calcular_ataque(inimigo,jogador)
        print(f"O INIMIGO DEU {escudo} DE DANO.")
        print(f"VIDA RESTANTE: {max(0, jogador["vida"])}HP")

    elif escolha == "curar":
        if inimigo["vida"] < 100: 
            executar_cura(inimigo)
        elif inimigo["vida"] == 100:
            print(f"o inimigo tentou se curar mas tava de hp cheio")
           













def turno(jogador,inimigo=False, nomeini="txt"):
    if inimigo == True:
        inimigo =  nomeini

    turn = [jogador,inimigo]
    random.shuffle(turn)
    return turn
       
   


def mudarcenario(*cenario):
    cenarios[0] = list(cenario)
    arrumarlista()
    linha("=")
  

    









  




    
            
        










                   
       

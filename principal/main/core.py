from time import sleep
import os
from sys import exit
import random
cenarios = [
    ["Sair da capsula", "Caminhar até a cidade"]  # inicial


]

personagem = {}


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
    



def atributos(vida=100, defesa=20, ataque=10, cura=5, xp=10, nivel=1):
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

def verificarnumero(num=0):
    nu = num
    while True:
        try:
            n = int(input(nu))
            ok = True
        except:
            print("Digite apenas numeros")
            ok = False
        else:
            if ok:
                return n 


def arrumarlista():
    for lista in cenarios:
        if "Sair" not in lista:
            lista.insert(len(lista), "Sair")
    


def mostraropcoes():
     for lista in cenarios: 
        for c, op in enumerate(lista):
            print(f"{c:.<10} {op}")
     
def escolha():
   mostraropcoes()
   opcao  =  verificarnumero(">>>>>")
   return opcao




def inicial():
    arrumarlista()
    while True:
        opcao = escolha()
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
    defesa=15,
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



def combate(inimigo=False, opional=False):
    global jogador
    jogador = personagem
    print("UM COMBATE COMEÇOU")

    ordem = turno(jogador=ps, inimigo=True, nomeini="walker")

    while jogador["vida"] > 0 and walkercomum["vida"] > 0:
        for atacante in ordem:
            if jogador["vida"] <= 0 or walkercomum["vida"] <= 0:
                break

            linha("-")
            sleep(1.5)
            
            if atacante == ps:
                print(f"VEZ DE {ps.upper()}:")
                mudarcenario("Atacar", "fugir")
                opcao = escolha()

                if opcao == 0:
            
                    dano = jogador["ataque"] - walkercomum["defesa"]
                    if dano < 1:
                        dano = 1  
                    walkercomum["vida"] -= dano

                    print(f"{ps} deu {dano} de dano!")
                    print(
                        f"O inimigo está com {walkercomum['vida']} de HP\n"
                    )

                elif opcao == 1:
                    print("Você tentou fugir!")













def turno(jogador,inimigo=False, nomeini="txt"):
    if inimigo == True:
        inimigo =  nomeini
        print(inimigo)
    
    turn = [jogador,inimigo]
    escolhido = random.sample(turn,k=2)
    return escolhido 
ordem = turno

def mudarcenario(*cenario):
    for item in cenarios[:]:
        item.clear()
    for i in cenario:
        item.append(i)
    arrumarlista()
    linha("=")
    mostraropcoes()
    linha("=")



def combate(inimigo=False,opional=False):
    global jogador
    jogador = personagem
    print("UM COMBATE COMEÇOU")
    print('O ESCOLHIDO FOI:')
    ordem = turno(jogador=ps,inimigo=True, nomeini="walker")
    while jogador["vida"] > 0 and walkercomum["vida"] > 0:
        for atacante in ordem:
            if jogador["vida"] <= 0 or walkercomum["vida"] <= 0:
                break
            sleep(1.5)
        if atacante == ps:
            print(f"VEZ DE {ps.upper()}:")
            mudarcenario("Atacar", "fugir")
            opcao = escolha()
            if opcao == 0:
                escudo =  walkercomum["defesa"] =- jogador["ataque"]
                dano = escudo =- walkercomum["vida"]
                print(f"{ps} deu {dano} de dano ")
                print(f"o inimigo esta com {walkercomum["vida"]} de hp")


    









  




    
            
        










                   
       

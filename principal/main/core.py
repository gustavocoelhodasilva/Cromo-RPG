from time import sleep
import os
import sys
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
    ps = txt
    sleep(2)
    cabeçalho(f"Bem vindo ao futuro {ps}", sinal="*")
    sleep(3)
    os.system("cls")
    return ps


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
            sys.exit()
        else:
            print("opção invalida")
    os.system("cls")
if escolha() == 1:
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

def dicstatus(ataque=20, vida = 75, defesa = 15, cura = 3, segundaforma = False, furia = False, fatordecura = False):
    if segundaforma and furia and fatordecura == False:
        walker = dict()
        walker["ataque"] = ataque
        walker["defesa"] = defesa
        walker["cura"] = cura
        walker["vida"] = vida
        return walker
    elif furia == True:
        walkerraivoso = dict()
        walkerraivoso["ataque"] = ataque
        walkerraivoso["defesa"] = defesa
        walkerraivoso["cura"] = cura
        walkerraivoso["vida"] = vida
        walkerraivoso["furia"] = ataque * 2
        return walkerraivoso
    elif segundaforma == True:
        walkerboss = dict()
        walkerboss["ataque"] = ataque + 3
        walkerboss["defesa"] = defesa + 1
        walkerboss["cura"] = cura + 3
        walkerboss["vida"] = vida * 2
        walkerboss["furia"] = ataque * 2
        return walkerboss
    elif fatordecura == True:
        walkermedico = dict()
        walkermedico["ataque"] = ataque
        walkermedico["defesa"] = defesa + 4
        walkermedico["cura"] = cura * 2
        walkermedico["vida"] = vida + 5
        return walkermedico
walkercomum = dicstatus()
walkerboss = dicstatus(segundaforma=True,furia=True)
walkermedico = dicstatus(fatordecura=True)






  




    
            
        










                   
       

from time import sleep
from ilustração import limpartela
from cenario import arrumarlista,escolhe

def inicio():
    sleep(2)
    print("EM UM FUTURO DISTANTE ALGO ACONTECE")
    sleep(2)
    limpartela()






def inicial():
    arrumarlista()
    while True:
        opcao = escolhe()
        if opcao == 0: 
            sleep(1)
            print("VOCÊ VE UM MUNDO INCRIVEL E NÃO ACREDITA EM SEUS OLHOS O MUNDO MUDOU TANTO")    
            sleep(3)
            limpartela()
            sleep(2)
            print("mas")
            sleep(2)
            limpartela()
            sleep(2)
            print("porque...")
            sleep(2)
            limpartela()
        elif opcao == 1:
            print("Você decide caminhar até a megacidade")
            sleep(2)
            cidade()
            break
            limpartela()
        elif opcao == 2:
            print("fechando o jogo")
            exit()
        else:
            print("opção invalida")
    limpartela()




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
    limpartela()
    sleep(1)
    print("Derrepente você no desespero tromba em um robô")
    sleep(1)
    print("O derrubando..")
    sleep(1)
    print("o robo se estressa")
    sleep(0.5)
    print("e então: ")


from time import sleep
from ilustração import limpartela
from cenario import arrumarlista, escolhe


COR_LORE = "\033[32m"
RESET = "\033[0m"


def print_lore(texto):
    print(f"{COR_LORE}{texto}{RESET}")

def inicio():
    sleep(2)
    print_lore("EM UM FUTURO DISTANTE ALGO ACONTECE")
    sleep(2)
    limpartela()

count = 0 
def inicial():
    global count
    arrumarlista()
    while True:
        opcao = escolhe()
        if opcao == 0 and count < 1: 
            sleep(1)
            print_lore("VOCÊ VE UM MUNDO INCRIVEL E NÃO ACREDITA EM SEUS OLHOS O MUNDO MUDOU TANTO")    
            sleep(3)
            limpartela()
            sleep(2)
            print_lore("mas")
            sleep(2)
            limpartela()
            sleep(2)
            print_lore("porque...")
            sleep(2)
            limpartela()
            count += 1
       
        elif opcao == 0 and count == 1:
            print_lore("Você ja saiu da capsula")
            sleep(2)
            limpartela()
        elif opcao == 1 and count == 1:
            print_lore("Você decide caminhar até a megacidade")
            sleep(2)
            cidade()
            limpartela()
            break
    
        elif opcao == 1 and count < 1:
            print_lore("SAIA DA CAPSULA PRIMEIRO")
            sleep(2)
            limpartela()
            
        elif opcao == 2:
            print("\033[31mfechando o jogo\033[0m")
            exit()
        else:
            print("\033[31mopção invalida\033[0m")
limpartela()

def cidade():
    print_lore("Você vê um cenario caótico")
    sleep(1)
    print_lore("Predios combrem o céu")
    sleep(1)   
    print_lore("arvores não existem")  
    sleep(1)  
    print_lore("Cadê as pessoas")
    sleep(1)
    print_lore("Apenas telas gigantes")
    sleep(1)
    print_lore("o mundo é dos robôs e não existe mais humanidade")
    sleep(1)
    limpartela()
    sleep(1)
    print_lore("Derrepente você no desespero tromba em um robô")
    sleep(1)
    print_lore("O derrubando..")
    sleep(1)
    print_lore("o robo se estressa")
    sleep(0.5)
    print_lore("e então: ")

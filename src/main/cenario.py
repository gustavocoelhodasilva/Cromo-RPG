from verificadores import verificarnumero
from ilustração import linha
from time import sleep
cenarios = [
    ["Sair da capsula", "Caminhar até a cidade"]  # inicial

]
def arrumarlista():
    for lista in cenarios:
        if "Sair" not in lista:
            lista.append("Sair")
        else:
            lista.remove("Sair")
    

def mostraropcoes():
     for lista in cenarios: 
        for c, op in enumerate(lista): 
            sleep(0.5)
            print(f"\033[34m{c:.<10} {op}\033[0m")


def escolhe():
   mostraropcoes()
   opcao  =  verificarnumero("\033[33m>>>>>\033[0m")
   return opcao



def mudarcenario(*cenario):
    cenarios[0] = list(cenario)
    arrumarlista()
    linha("=")
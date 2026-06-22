from verificadores import verificarnumero
from ilustração import linha
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
            print(f"{c:.<10} {op}")


def escolhe():
   mostraropcoes()
   opcao  =  verificarnumero(">>>>>")
   return opcao



def mudarcenario(*cenario):
    cenarios[0] = list(cenario)
    arrumarlista()
    linha("=")
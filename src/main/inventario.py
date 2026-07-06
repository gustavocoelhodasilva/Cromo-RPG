from ilustração import cabeçalho,limpartela,linha
from verificadores import verificarnumero
from jogador import atributos,mostrar_atributos,get_personagem
from items import ARMAS,SERINGAS,ITENS
from cenario import escolhe,mudarcenario
from time import sleep
atributos()
personagem = get_personagem()



def seringas(*seringas):

    armazenamento = list(seringas)
    lista = []
    

    for caixa in armazenamento:
       tiposdeseringa = {}
       tiposdeseringa["nome"] = caixa[0]
       tiposdeseringa["tipo"] = caixa [1]
       tiposdeseringa["efeito"] = caixa[2]
       lista.append(tiposdeseringa)
    

    nomes = []
    tipo = []
    efeito = []


    for item in lista:
        if item["nome"]:
           nomes.append(item.get('nome')) 
           
        if item["tipo"]:
            tipo.append(item.get('tipo'))

        if item["efeito"]:
            efeito.append(item.get('efeito'))    



    return nomes,tipo,efeito


def exibiritemns(txt="ITEMS", sn="=", qtde= 30, cor ="\033[34m", reset ="\033[0m"):
    sinal = sn * qtde
    print(f"{cor}{sinal}{reset}")
    print(f"{txt}".center(qtde))
    print(f"{cor}{sinal}{reset}")
   







def inventario():
    limpartela()
    cabeçalho("INVENTARIO")
    sleep(2)
    nome = seringas(*SERINGAS)[0]
    Itens = seringas(*ITENS)[0]
    Armas = seringas(*ARMAS)[0]


    categorias = {
        "Seringas": nome,
        "Armas": Armas,
        "Itens": Itens,
    }
    

    for c in categorias.keys():
        exibiritemns(f'{c}',sn="-", qtde=40)

    linha(qtde=40)
    
    mudarcenario("Seringas", "Armas", "itens")
    escolha = escolhe()
    
    if escolha == 0:
        
        exibiritemns("Seringas Disponiveis")
        for i in nome:
            print(F"- {i}")
        print("\033[34m=\033[0m"*30)
        mudarcenario(*nome)
        escolha_seringa = escolhe()   
        seringa_escolhida = nome[escolha_seringa]
        print("\033[34m=\033[0m"*30)
        print(f"Você escolheu \033[31m{seringa_escolhida}\033[0m")
        sleep(3)
        return seringa_escolhida
    
    if escolha == 1:
        exibiritemns("Armas Disponiveis")
        for i in Armas:
            print(F"- {i}")
        print("\033[34m=\033[0m"*30)
        mudarcenario(*Armas)
        escolha_Arma = escolhe()   
        Arma_escolhida = Armas[escolha_Arma]
        print("\033[34m=\033[0m"*30)
        print(f"Você escolheu \033[31m{Arma_escolhida}\033[0m")
        sleep(3)
        return Arma_escolhida
   
    if escolha == 2:
        exibiritemns("Items Disponiveis")
        for i in Itens:
            print(F"- {i}")
        print("\033[34m=\033[0m"*30)
        mudarcenario(*Itens)
        escolha_Item = escolhe()   
        Item_escolhido = Itens[escolha_Item]
        print("\033[34m=\033[0m"*30)
        print(f"Você escolheu \033[31m{Item_escolhido}\033[0m")
        sleep(3)
        
        return Item_escolhido
    if escolha == 3:
        return escolha
    
    print("\033[34m=\033[0m"*30)



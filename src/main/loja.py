from inventario import exibiritemns
from cenario import mudarcenario, escolhe
from ilustração import cabeçalho, limpartela,linha
from items import ITENS, ARMAS, SERINGAS
from time import sleep
from jogador import get_personagem,atributos, mostrar_atributos
status = get_personagem()
def loja(armas=ARMAS, items=ITENS, seringas=SERINGAS, jg=status):
    nome = []
    moedas = 0
    while True:     
        cenario = mudarcenario("Status", "Armas", "Seringas", "Molde de mascara","ver status")
        op = escolhe()
        limpartela()




        if cenario[0][op] == "Status":
            status = {
                "aumentar vida": {"preco": 10, "efeito": 15, "unidade": "HP"},
                "aumentar defesa": {"preco": 15, "efeito": 15, "unidade": "DEF"},
                "aumentar ataque": {"preco": 20, "efeito": 10, "unidade": "ATQ"},
                "aumentar cura": {"preco": 20, "efeito": 10, "unidade": "Cura"}
            }


            for c in status.keys():
                exibiritemns(c, cor="\033[33m", sn="-")


            nome = list(status.keys())

            sub = mudarcenario(*nome)
            sub_op = escolhe()
            limpartela()
            item_escolhido = sub[0][sub_op]

            if item_escolhido == "Sair":
                continue

            if item_escolhido in status:
                cabeçalho(item_escolhido.replace("aumentar ", "").title())
                
                preco = status[item_escolhido]["preco"]
                efeito = status[item_escolhido]["efeito"]
                unidade = status[item_escolhido]["unidade"]

                print(f"\033[34m- Preço: {preco}$\033[m")
                print(f"\033[34m- Efeito: +{efeito} {unidade}\033[m")
                linha()
                cenario = mudarcenario("comprar")
                sb = escolhe()
                qtdemoeda = items[0]["qtde"]
                moedas += qtdemoeda
                if moedas >= preco and sb == 0 :
                    print(f"voce comprou {item_escolhido}")
                    if unidade == "HP":
                        jg["vida"] += 15
                        
                    sleep(1)
                else:
                    if sb != 1:
                        print("saldo insuficiente")
                    sleep(1)
                limpartela()
            else:
                if item_escolhido != "Sair":
                    print("escolha um item valido")


lo
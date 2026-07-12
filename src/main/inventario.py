import items
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

       lista.append(
           {"nome":caixa["nome"],
            "tipo": caixa["tipo"],
            "efeito": caixa["efeito"],
            "qtde": caixa["qtde"]
            })
         
  
       
    
    return lista

def exibiritemns(txt="ITEMS", sn="=", qtde= 30, cor ="\033[34m", reset ="\033[0m"):
    sinal = sn * qtde
    print(f"{cor}{sinal}{reset}")
    print(f"{txt}".center(qtde))
    print(f"{cor}{sinal}{reset}")


def inventario():
    limpartela()
    cabeçalho("INVENTARIO")
    sleep(2)
    dados_seringas = seringas(*SERINGAS)
    dados_armas = seringas(*ARMAS)
    dados_itens = seringas(*ITENS)
    
    nome = [item["nome"] for item in dados_seringas]
    Itens = [item["nome"] for item in dados_itens]
    Armas = [item["nome"] for item in dados_armas]
   
    categorias = {
        "Seringas": nome,
        "Armas": Armas,
        "Itens": Itens,
    }

    while True:
        limpartela()
        cabeçalho("INVENTARIO")
        for c in categorias.keys():
            exibiritemns(f'{c}', sn="-", qtde=40)
        linha(qtde=40)

        
        cenario = mudarcenario("Seringas", "Armas", "Itens")
        escolha = escolhe()

       
        saiu_do_menu_principal = False
        for i in cenario:
            for c in i: 
                if escolha == len(i) - 1:
                    saiu_do_menu_principal = True
        if saiu_do_menu_principal:
            return 

        if escolha == 0:
            limpartela()
            exibiritemns("Seringas Disponiveis")
            
            for i in nome:
                print(F"- {i}")
            print("\033[34m=\033[0m"*30)
            cenario_seringa = mudarcenario(*nome)
            escolha_seringa = escolhe()

            saiu_do_submenu = False
            for i in cenario_seringa:
                for c in i:
                    if escolha_seringa == len(i) - 1:
                        saiu_do_submenu = True
            if saiu_do_submenu:
                continue 

            seringa_escolhida = dados_seringas[escolha_seringa]
            while True:
                limpartela()
                exibiritemns(f"Você escolheu \033[31m{seringa_escolhida['nome']}\033[0m")
                print(f"\033[34mTipo: {seringa_escolhida['tipo']}\033[0m")
                if seringa_escolhida["tipo"] == "dano":
                    print(f"\033[34mEfeito: {seringa_escolhida['efeito']} de dano a mais\033[0m")
                elif seringa_escolhida["tipo"] == "cura":
                    print(f"\033[34mEfeito: {seringa_escolhida['efeito']}HP\033[0m")
                elif seringa_escolhida["tipo"] == "sorte":
                    print(f"\033[34mEfeito: {seringa_escolhida['efeito']}% de sorte\033[0m")
                
                if seringa_escolhida["qtde"] > 0:
                    print(f"\033[34mQuantidade: {seringa_escolhida['qtde']} Restantes\033[0m")
                else:
                    print(f"\033[34mNão há mais seringas\033[0m")
                print("\033[34m=\033[0m"*30)
                
                mudarcenario("equipar")
                escolheu = escolhe()
                if escolheu == 0:
                    if seringa_escolhida["qtde"] == 0:
                        print("Você não tem esse item")
                        sleep(2)
                    else:
                     
                        items.SERINGAS[escolha_seringa]["qtde"]  -= 1
                      

                        print("Item equipado")
                        print(f"quantidade restante {items.SERINGAS[escolha_seringa]["qtde"]}")

                        sleep(2)
                        return seringa_escolhida
            
                if escolheu == 1:
                    break

        elif escolha == 1:
            limpartela()
            exibiritemns("Armas Disponiveis")
            for i in Armas:
                print(F"- {i}")
            print("\033[34m=\033[0m"*30)
            cenario_arma = mudarcenario(*Armas)
            escolha_Arma = escolhe()

            saiu_do_submenu = False
            for i in cenario_arma:
                for c in i:
                    if escolha_Arma == len(i) - 1:
                        saiu_do_submenu = True
            if saiu_do_submenu:
                continue

            arma_escolhida = dados_armas[escolha_Arma]
            while True:
                limpartela()
                exibiritemns(f"Você escolheu \033[31m{arma_escolhida['nome']}\033[0m")
                print(f"\033[34mTipo de Dano: {arma_escolhida['tipo']}\033[0m")
              
                if arma_escolhida["tipo"] == "Contato":
                    print(f"\033[34mEfeito: causa {arma_escolhida['efeito']} de dano físico\033[0m")
                elif arma_escolhida["tipo"] == "Raio":
                    print(f"\033[34mEfeito: causa {arma_escolhida['efeito']} de dano elétrico\033[0m")
                elif arma_escolhida["tipo"] == "Fogo":
                    print(f"\033[34mEfeito: causa {arma_escolhida['efeito']} de dano de queimadura\033[0m")
                elif arma_escolhida["tipo"] == "Agua":
                    print(f"\033[34mEfeito: causa {arma_escolhida['efeito']} de dano de impacto hidráulico\033[0m")
                elif arma_escolhida["tipo"] == "Pedra":
                    print(f"\033[34mEfeito: causa {arma_escolhida['efeito']} de dano de esmagamento\033[0m")
                
                if arma_escolhida["qtde"] > 0:
                    print(f"\033[34mQuantidade: {arma_escolhida['qtde']} No Estoque\033[0m")
                else:
                    print(f"\033[34mNão há mais armas deste tipo disponíveis\033[0m")
                    
                print("\033[34m=\033[0m"*30)
                mudarcenario("equipar")
                escolheu = escolhe()
                if escolheu == 0:
                    if arma_escolhida["qtde"] == 0:
                        print("Você não liberou esta arma")
                        sleep(2)
                    else:
                        items.ARMAS[escolha_Arma]["qtde"] -= 1
                       
                        print(f"quantidade restante {items.ARMAS[escolha_Arma]["qtde"]}")
                        print("Item equipado")
                        sleep(2)
                        return arma_escolhida
            
                if escolheu == 1:
                    break

        elif escolha == 2:
            limpartela()
            exibiritemns("Items Disponiveis")
            for i in Itens:
                print(F"- {i}")
            print("\033[34m=\033[0m"*30)
            cenario_item = mudarcenario(*Itens)
            escolha_Item = escolhe()

            saiu_do_submenu = False
            for i in cenario_item:
                for c in i:
                    if escolha_Item == len(i) - 1:
                        saiu_do_submenu = True
            if saiu_do_submenu:
                continue

            item_escolhido = dados_itens[escolha_Item]
            while True:
                limpartela()
                exibiritemns(f"Você escolheu \033[31m{item_escolhido['nome']}\033[0m")
                print(f"\033[34mTipo: {item_escolhido['tipo']}\033[0m")
                
                if item_escolhido["qtde"] > 0:
                    print(f"\033[34mQuantidade: {item_escolhido['qtde']} Restantes\033[0m")
                else:
                    print(f"\033[34mNão há mais itens\033[0m")
                print("\033[34m=\033[0m"*30)
                
                mudarcenario("equipar")
                escolheu = escolhe()
                if escolheu == 0:
                    if item_escolhido["qtde"] == 0:
                        print("Você não tem mais moedas. POBRE")
                        sleep(2)
                    else:
                        items.ITENS[escolha_Item]["qtde"] -= 1

    
                        print("Item equipado")
                        print(f"quantidade restante {items.ITENS[escolha_Item]["qtde"]}")
                        sleep(2)
                        return item_escolhido

                if escolheu == 1:
                    break

        else:
            print("Escolha uma opção válida")
            sleep(2)

print("\033[34m=\033[0m"*30)

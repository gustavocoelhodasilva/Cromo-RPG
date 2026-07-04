from ilustração import cabeçalho,limpartela
from verificadores import verificarnumero
from jogador import atributos,mostrar_atributos,get_personagem

atributos()
personagem = get_personagem()



def pocoes(*seringas):

    armazenamento = list(seringas)
    lista = []
    

    for caixa in armazenamento:
       tiposdeseringa = {}
       tiposdeseringa["nome"] = caixa[0]
       tiposdeseringa["tipo"] = caixa [1]
       tiposdeseringa["efeito"] = caixa[2]
       lista.append(tiposdeseringa)
    
    nomes = []
    for item in lista:
        if item["nome"]:
           nomes.append(f"{item.get('nome')}") 
 







def inventario():
    limpartela()
    cabeçalho("INVENTARIO")

    categorias = {
        "Seringas":"em breve",
        "Armas": "em breve",
        "Itens": "em breve",
    }
    print(categorias)




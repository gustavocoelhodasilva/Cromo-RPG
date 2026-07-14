from ilustração import limpartela
import readchar
from time import sleep
mapa = [
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"]
]           


# o jogador clicar em uma tecla expecifica a tecla vai ser equivalente a posição que ele ira
                                # exemplo:
                                # W subir para a lista de cima
                                # s para descer nas listas
                                # d para direta andar positivo na msm lista
                                # a para a esquerda andar negativo na msm lista        
                                # meu primeiro objetivo vai ser fazer andar pro lado pelas teclas     

# mapa[5][0] = 0 # substitui pelo padrao
mapa[5][0] = "🧑" # adicionei na nova posicao

 

def exibirmapa():
    for linha in mapa:
        print("".join(linha).center(150))

def posicao():
    linha = 0
    pos = 0
    for i, li in enumerate(mapa):
        for ind, obj in enumerate(li):
            if obj == "🧑":
                linha = i
                pos = ind           
    return linha,pos

altura = len(mapa) #6
largura = len(mapa[0]) #7


linha,pos = posicao()

def andar(y=linha,x=pos,letra="w"):
    letra.strip()
    if letra == "w":
        novay = y - 1
        mapa[novay][x] = "🧑"
        mapa[y][x] = "⬛"
    elif letra == "s":
        novay = y + 1
        mapa[novay][x] = "🧑"
        mapa[y][x] = "⬛"
    elif letra == "d":
        novax = x + 1
        mapa[y][novax] = "🧑"
        mapa[y][x] = "⬛"
        return y, novax
    elif letra == "a":
        novax = x - 1
        mapa[y][novax] = "🧑"
        mapa[y][x] = "⬛"
        return y, novax

    return novay,x
    

exibirmapa()
while True:

    mov = readchar.readkey().strip().lower()[0]
    if mov == "w":
        if linha > 0:
            linha,pos = andar(linha,pos,mov)
        else:
            print(".")
           
    elif mov == "s":
        if linha < 5:
            linha,pos = andar(linha,pos,mov)
        else:
            print(".")
           
    elif mov == "d":
        if pos < 6:
            linha,pos = andar(linha,pos,mov)
        else:
            print(".")
            
    elif mov == "a":
        if pos > 0:
            linha,pos = andar(linha,pos,mov)
        else:
            print(".")
            sleep(1)
    else:
        print("digite apenas WASD")
        sleep(1)
   
    limpartela()
    exibirmapa()
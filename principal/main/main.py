
from jogador import iniciar_jogador
from prelore import inicial, inicio
from ilustração import limpartela
from luta import combate

def main():
    inicio()
    limpartela()
    iniciar_jogador()
    limpartela()
    inicial()
    combate()

if __name__ == "__main__":
    main()

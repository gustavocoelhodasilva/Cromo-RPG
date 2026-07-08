from jogador import iniciar_jogador
from prelore import inicial,revelacao
from ilustração import limpartela
from luta import combate
import random
def main():
    limpartela()
    iniciar_jogador()
    limpartela()
    inicial()

    comb = combate()

    revelacao()

    print("\033[33m[ ALERTA DE SISTEMA: As hordas de robôs estão se aproximando... ]\033[0m\n")
    c = 0
    aleatorios = ["comum","medico","raivoso"]
    c += 1
    while c < 6:
        if c == 5:
            c = 0
        else:
            esc = random.choice(aleatorios)
            if comb == "continue":
                combate(esc,c)
                c += 1
        


if __name__ == "__main__":
    main()
from jogador import iniciar_jogador
from prelore import inicial,revelacao,dialogo_pre_horda,dialogo_encontro_ravi,tubulacao
from ilustração import limpartela
from luta import combate
import random
def main():
    limpartela()
    iniciar_jogador()
    limpartela()
    inicial()


    
    



    
    aleatorios = ["comum","medico","raivoso"] # primeira batalha/tutorial
    combate(qtd=16)
    dialogo_pre_horda()
    


    while True:
         escolha = random.choice(aleatorios)
         for numero, inimigo in  enumerate(range(1,6)):
             inimigo = escolha
             horda = combate(inimigo,numero + 1)
         if horda == "continuou":
             pass
         elif horda == "fugiu":
             revelacao()
             dialogo_encontro_ravi()
             tubulacao()
             break
if __name__ == "__main__":
    main()
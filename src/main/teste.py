from inventario import inventario,seringas
from items import SERINGAS,ARMAS,ITENS
from time import sleep
import random
seringa =   SERINGAS
aleatorio = random.choice(seringa)
aleatorio["qtde"] += 1
print(aleatorio)


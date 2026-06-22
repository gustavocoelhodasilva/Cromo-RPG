import os
import sys
_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
while _root and not os.path.exists(os.path.join(_root, 'principal')):
    _parent = os.path.dirname(_root)
    if _parent == _root: break
    _root = _parent
if _root not in sys.path: sys.path.append(_root)
if os.path.join(_root, 'principal') not in sys.path: sys.path.append(os.path.join(_root, 'principal'))

from verificadores.verificadores import verificarnumero
from ilustração.ilustração import linha

cenarios = [
    ["Sair da capsula", "Caminhar até a cidade"]  # inicial
]

def arrumarlista():
    for lista in cenarios:
        if "Sair" not in lista:
            lista.append("Sair")
        # Removido o else que removia o Sair, para evitar comportamento inesperado


def mostraropcoes():
     for lista in cenarios: 
        for c, op in enumerate(lista): 
            print(f"{c:.<10} {op}")


def escolhe():
   mostraropcoes()
   opcao = verificarnumero(">>>>>")
   return opcao


def mudarcenario(*cenario):
    cenarios[0] = list(cenario)
    arrumarlista()
    linha("=")

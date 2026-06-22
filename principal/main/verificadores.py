import os
import sys
_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
while _root and not os.path.exists(os.path.join(_root, 'principal')):
    _parent = os.path.dirname(_root)
    if _parent == _root: break
    _root = _parent
if _root not in sys.path: sys.path.append(_root)
if os.path.join(_root, 'principal') not in sys.path: sys.path.append(os.path.join(_root, 'principal'))


def verificarnumero(prompt=">>>>"):
    while True:
        try:
            n = int(input(prompt))
            return n
        except:
            print("Digite apenas numeros")
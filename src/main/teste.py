from inventario import inventario
import items
inv = inventario() 
#print(inv.values())
nomes = []
for t in items.SERINGAS:
    nomes.append(t[0])
if inv["nome"] in nomes:
    print("certo")
else:
    print("errado")
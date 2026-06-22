
def dicstatus(
    ataque=20,
    vida=75,
    defesa=5,
    cura=3,
    segundaforma=False,
    furia=False,
    fatordecura=False,
):
    # Se for Boss (Segunda forma + Fúria)
    if segundaforma == True:
        walkerboss = dict()
        walkerboss["ataque"] = ataque + 3
        walkerboss["defesa"] = defesa + 1
        walkerboss["cura"] = cura + 3
        walkerboss["vida"] = vida * 2
        walkerboss["furia"] = ataque * 2
        return walkerboss

    elif furia == True:
        walkerraivoso = dict()
        walkerraivoso["ataque"] = ataque
        walkerraivoso["defesa"] = defesa
        walkerraivoso["cura"] = cura
        walkerraivoso["vida"] = vida
        walkerraivoso["furia"] = ataque * 2
        return walkerraivoso

    elif fatordecura == True:
        walkermedico = dict()
        walkermedico["ataque"] = ataque
        walkermedico["defesa"] = defesa + 4
        walkermedico["cura"] = cura * 2
        walkermedico["vida"] = vida + 5
        return walkermedico

    else:
        # Walker Comum normal
        walker = dict()
        walker["ataque"] = ataque
        walker["defesa"] = defesa
        walker["cura"] = cura
        walker["vida"] = vida
        return walker


def criarinimigo(tipo="comum"):
    if tipo == "boss":
        return dicstatus(segundaforma=True)
    elif tipo == "medico":
        return dicstatus(fatordecura=True)
    elif tipo == "raivoso":
        return dicstatus(furia=True)
    else:
        return dicstatus()
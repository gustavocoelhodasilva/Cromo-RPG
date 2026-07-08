def dicstatus(
    nome="Droide Comum",  # Adicionado o parâmetro nome com um padrão
    ataque=25,
    vida=75,
    defesa=5,
    cura=8,
    segundaforma=False,
    furia=False,
    fatordecura=False,
):
    # Se for Boss (Segunda forma + Fúria)
    if segundaforma == True:
        walkerboss = dict()
        walkerboss["nome"] = nome  # Adicionado
        walkerboss["ataque"] = ataque + 3
        walkerboss["defesa"] = defesa + 1
        walkerboss["cura"] = cura + 3
        walkerboss["vida"] = vida * 2
        walkerboss["furia"] = ataque * 2
        return walkerboss

    elif furia == True:
        walkerraivoso = dict()
        walkerraivoso["nome"] = nome  # Adicionado
        walkerraivoso["ataque"] = ataque
        walkerraivoso["defesa"] = defesa
        walkerraivoso["cura"] = cura
        walkerraivoso["vida"] = vida
        walkerraivoso["furia"] = ataque * 2
        return walkerraivoso

    elif fatordecura == True:
        walkermedico = dict()
        walkermedico["nome"] = nome  # Adicionado
        walkermedico["ataque"] = ataque
        walkermedico["defesa"] = defesa + 4
        walkermedico["cura"] = cura * 2
        walkermedico["vida"] = vida + 5
        return walkermedico

    else:
        # Walker Comum normal
        walker = dict()
        walker["nome"] = nome  # Adicionado
        walker["ataque"] = ataque
        walker["defesa"] = defesa
        walker["cura"] = cura
        walker["vida"] = vida
        return walker


def criarinimigo(tipo="comum"):
    if tipo == "boss":
        # Passa o nome imponente para o Boss
        return dicstatus(nome="Soberano da Sucata (BOSS)", segundaforma=True)
    elif tipo == "medico":
        # Passa o nome para o inimigo de cura
        return dicstatus(nome="Unidade Médica Nano", fatordecura=True)
    elif tipo == "raivoso":
        # Passa o nome para o inimigo furioso
        return dicstatus(nome="Droide Supersônico ", furia=True)
    else:
        # Passa o nome para o inimigo padrão
        return dicstatus(nome="Sentinela de Ferro")

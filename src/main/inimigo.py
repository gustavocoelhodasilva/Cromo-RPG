



















HABILIDADES = {
    "ganancia": {
        "nome": "Ganância Absoluta",
        "efeito": "Bloqueia o uso do inventário"
    },
    "esmagamento": {
        "nome": "Esmagamento Hidráulico",
        "efeito": "Rompe escudos e ignora defesa"
    },
    "abaddon_ult": {
        "nome": "0RGULH0 M4LD1T0",
        "efeito": "Reduz status do jogador, e impede fuga"
    },
    "contrato": {
        "nome": "Contrato de Sangue",
        "efeito": "Causa dano direto ignorando defesas"
    },
    "enxerto": {
        "nome": "Enxerto de Metal",
        "efeito": "Ganha um escudo indestrutível por 2 turnos" #loja
    },
    "sinal_besta": {
        "nome": "Sinal da Besta",
        "efeito": "Superaquece o chip neural, causando dano de fogo por turno"
    },
    "suborno": {
        "nome": "Suborno",
        "efeito": "Chance de roubar créditos do jogador a cada ataque"
    },
    "emp": {
        "nome": "Pulso EMP",
        "efeito": "Desativa as habilidades ativas do jogador por 2 turnos" #loja
    }
}


def dicstatus(nome="Droide Comum", ataque=25, vida=75, defesa=5, cura=8, mult_atk=1, mult_def=1, mult_vida=1, mult_cura=1, furia_val=0):
    """
    Função genérica para calcular os status com base em multiplicadores.
    Evita a necessidade de dezenas de 'if/elif' booleanos.
    """
    return {
        "nome": nome,
        "ataque": ataque * mult_atk,
        "defesa": defesa * mult_def,
        "cura": cura * mult_cura,
        "vida": vida * mult_vida,
        "furia": furia_val,
        "habilidade": None
    }


def criarinimigo(tipo="comum"):
    tipo = tipo.lower()
    # --- INIMIGOS ESPECIAIS / BOSSES ---
    if tipo == "boss":
        inimigo = dicstatus(nome="EG01SM0 (BOSS)", mult_atk=4, mult_def=4, mult_cura=5, mult_vida=5)
        inimigo["furia"] = 125
        inimigo["habilidade"] = HABILIDADES["ganancia"]
        return inimigo

    elif tipo == "medico":
        inimigo = dicstatus(nome="Larva Parasitária", defesa=9, mult_cura=4, vida=80)
        return inimigo

    elif tipo == "raivoso":
        inimigo = dicstatus(nome="Flagelo de Gomorra", furia_val=50)
        return inimigo

    elif tipo == "guardiao":
        inimigo = dicstatus(nome="Guardião de G0MORR4 (GUARDIÃO)", mult_atk=4, mult_def=4, mult_cura=4, mult_vida=3)
        inimigo["habilidade"] = HABILIDADES["esmagamento"]
        return inimigo

    elif tipo == "abaddon":
        inimigo = dicstatus(nome="666.sys [4B4DD0N] 666.sys (FINAL BOSS)", mult_atk=6, mult_def=6, mult_cura=6, mult_vida=10)
        inimigo["habilidade"] = HABILIDADES["abaddon_ult"]
        return inimigo

    # --- SETOR: BABILÔNIA ---
    elif tipo in ["babilônia_comum1", "mercador"]:
        inimigo = dicstatus(nome="Mercador", ataque=18, vida=70)
        inimigo["habilidade"] = HABILIDADES["suborno"]
        return inimigo

    elif tipo in ["babilônia_comum2", "corretor"]:
        return dicstatus(nome="Corretor", ataque=22, vida=65, defesa=8)

    elif tipo in ["babilônia_comum3", "bancario"]:
        return dicstatus(nome="Agenciador", defesa=9, mult_cura=4, vida=80)

    elif tipo in ["babilônia_guardiao", "guardiao_babilônia"]:
        inimigo = dicstatus(nome="O C0br4d0r de 4lm45 (GUARDIÃO)", mult_atk=4, mult_def=4, mult_cura=4, mult_vida=3)
        inimigo["habilidade"] = HABILIDADES["contrato"]
        return inimigo

    # --- SETOR: SODOMA ---
    elif tipo in ["sodoma_comum1", "retalhador"]:
        return dicstatus(nome="Flagelo de Sodoma (Ajustado)", furia_val=50)

    elif tipo in ["sodoma_comum2", "cirurgiao"]:
        return dicstatus(nome="Robô Cirúrgico Desertor", ataque=15, vida=85, defesa=12)

    elif tipo in ["sodoma_comum3", "sucateiro"]:
        return dicstatus(nome="Colhedor de Bio-matéria", ataque=20, vida=80)

    elif tipo in ["sodoma_guardiao", "guardiao_sodoma"]:
        inimigo = dicstatus(nome="O Qu1m3r4 de C4rn3 (GUARDIÃO)", mult_atk=4, mult_def=4, mult_cura=4, mult_vida=3)
        inimigo["habilidade"] = HABILIDADES["enxerto"]
        return inimigo

    # --- SETOR: GOMORRA ---
    elif tipo in ["gomorra_comum1", "serafim_ferro"]:
        return dicstatus(nome="Serafim de Ferro", ataque=25, vida=75)

    elif tipo in ["gomorra_comum2", "verme"]:
        inimigo = dicstatus(nome="Verme da Lixeira de Silício", ataque=15, vida=90)
        inimigo["habilidade"] = HABILIDADES["emp"]
        return inimigo

    elif tipo in ["gomorra_comum3", "fundidor"]:
        return dicstatus(nome="Operário Autômato", furia_val=50)

    elif tipo in ["gomorra_guardiao", "guardiao_gomorra_novo"]:
        inimigo = dicstatus(nome="$0b3r4n0 da Fundição (GUARDIÃO)", mult_atk=4, mult_def=4, mult_cura=4, mult_vida=3)
        inimigo["habilidade"] = HABILIDADES["sinal_besta"]
        return inimigo

    # Default
    else:
        return dicstatus(nome="Droide Comum")
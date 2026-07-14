def dicstatus(
    nome="Droide Comum",  # Adicionado o parâmetro nome com um padrão
    ataque=25,
    vida=75,
    defesa=5,
    cura=8,
    segundaforma=False,
    furia=False,
    fatordecura=False,
    terceiraforma = False,
    finalboss = False
):
    # Se for Boss (Segunda forma + Fúria)
    if segundaforma == True:
        walkerboss = dict()
        walkerboss["nome"] = nome  # Adicionado
        walkerboss["ataque"] = ataque * 4
        walkerboss["defesa"] = defesa * 4
        walkerboss["cura"] = cura * 5
        walkerboss["vida"] = vida * 5
        walkerboss["furia"] = ataque * 5
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
        walkermedico["cura"] = cura * 4
        walkermedico["vida"] = vida + 5
        return walkermedico

    elif terceiraforma == True:
        walkerguardiao = dict()
        walkerguardiao["nome"] = nome  # Adicionado
        walkerguardiao["ataque"] = ataque * 4
        walkerguardiao["defesa"] = defesa * 4
        walkerguardiao["cura"] = cura * 4
        walkerguardiao["vida"] = vida * 3
        return walkerguardiao
    elif finalboss == True:
        walkerabbadon = dict()
        walkerabbadon["nome"] = nome  # Adicionado
        walkerabbadon["ataque"] = ataque * 6
        walkerabbadon["defesa"] = defesa * 6
        walkerabbadon["cura"] = cura * 6
        walkerabbadon["vida"] = vida * 10
        return walkerabbadon
    
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
    # Garante compatibilidade caso digite em maiúsculas
    tipo = tipo.lower()

    # --- INIMIGOS ANTIGOS / ORIGINAIS ---
    if tipo == "boss":
      
        inimigo = dicstatus(nome="EG01SM0 (BOSS)", segundaforma=True)
        inimigo["habilidade"] = "Ganancia Absoluta (Bloqueia o inventario)"
        return inimigo
    elif tipo == "medico":
  
        inimigo = dicstatus(nome="larva parasitaria", fatordecura=True)
        inimigo["habilidade"] = "Choro Ilusorio (Drena vida do alvo)"
        return inimigo
    elif tipo == "raivoso":
       
        inimigo = dicstatus(nome="Flagelo de gomorra ", furia=True)
        inimigo["habilidade"] = "Frenesi Quimico (Ataques rapidos e descontrolados)"
        return inimigo
    elif tipo == "guardiao":
       
        inimigo = dicstatus(nome="Guardiao de G0MORR4 (GUARDIÃO) ", terceiraforma=True)
        inimigo["habilidade"] = "Esmagamento Hidraulico (Rompe escudos)"
        return inimigo
    
     # =========================================================================
    # --- ABBADON FINAL BOSS ---
    # =========================================================================
    
    elif tipo == "abaddon":
        # Chefe final do lore
        inimigo = dicstatus(nome = "666.sys [4B4DD0N] 666.sys (F1N4L B0S5)", finalboss=True)
        inimigo["habilidade"] = "0GURLH0 M4LD1T0 (Reduz todos os seus status, não deixa usar o inventario, impossivel fugir)"
        return inimigo

    # =========================================================================
    # --- NOVO SETOR: BABILÔNIA (O MERCADO DE ALMAS) ---
    # =========================================================================
    elif tipo == "babilônia_comum1" or tipo == "mercador":
        inimigo = dicstatus(nome="Mercador", ataque=18, vida=70)
        inimigo["habilidade"] = "Dreno de Moedas (Rouba recursos digitais do jogador)"
        return inimigo
        
    elif tipo == "babilônia_comum2" or tipo == "corretor":
        inimigo = dicstatus(nome="Corretor", ataque=22, vida=65, defesa=8)
        inimigo["habilidade"] = "Sobrecarga de Display (Cega o jogador por 1 turno)"
        return inimigo
        
    elif tipo == "babilônia_comum3" or tipo == "bancario":
        inimigo = dicstatus(nome="Agenciador", fatordecura=True) # Usa estrutura medica
        inimigo["habilidade"] = "Cobranca Compulsoria (Cura aliados confiscando vida)"
        return inimigo
        
    elif tipo == "babilônia_guardiao" or tipo == "guardiao_babilônia":
        inimigo = dicstatus(nome="O C0br4d0r de 4lm45 (GUARDIÃO)", terceiraforma=True)
        inimigo["habilidade"] = "Contrato de Sangue (Causa dano direto ignorando defesas)"
        return inimigo

    # =========================================================================
    # --- NOVO SETOR: SODOMA (A CARNE SINTÉTICA) ---
    # =========================================================================
    elif tipo == "sodoma_comum1" or tipo == "retalhador":
        inimigo = dicstatus(nome="Flagelo de Sodoma (Ajustado)", furia=True) # Usa estrutura de furia do lore
        inimigo["habilidade"] = "Amputacao Voluntaria (Aumenta o proprio ataque e perde defesa)"
        return inimigo
        
    elif tipo == "sodoma_comum2" or tipo == "cirurgiao":
        inimigo = dicstatus(nome="Robo Cirurgico Desertor", ataque=15, vida=85, defesa=12)
        inimigo["habilidade"] = "Mutilacao Biomecanica (Aplica sangramento continuo)"
        return inimigo
        
    elif tipo == "sodoma_comum3" or tipo == "sucateiro":
        inimigo = dicstatus(nome="Colhedor de Bio-materia", ataque=20, vida=80)
        inimigo["habilidade"] = "Injecao de Oleo Poluido (Reduz a velocidade do jogador)"
        return inimigo
        
    elif tipo == "sodoma_guardiao" or tipo == "guardiao_sodoma":
        inimigo = dicstatus(nome="O Qu1m3r4 de C4rn3 (GUARDIÃO)", terceiraforma=True)
        inimigo["habilidade"] = "Enxerto de Metal (Ganha um escudo indestrutivel por 2 turnos)"
        return inimigo

    # =========================================================================
    # --- NOVO SETOR: GOMORRA (A LINHA DE MONTAGEM) ---
    # =========================================================================
    elif tipo == "gomorra_comum1" or tipo == "serafim_ferro":
        inimigo = dicstatus(nome="Serafim de Ferro", ataque=25, vida=75) # Inimigo padrao do lore
        inimigo["habilidade"] = "Varredura Piramidal (Cancela esquivas do jogador)"
        return inimigo
        
    elif tipo == "gomorra_comum2" or tipo == "verme":
        inimigo = dicstatus(nome="Verme da Lixeira de Silicio", ataque=15, vida=90)
        inimigo["habilidade"] = "Ejecao Toxica (Envenena o alvo com fluidos industriais)"
        return inimigo
        
    elif tipo == "gomorra_comum3" or tipo == "fundidor":
        inimigo = dicstatus(nome="Operario Autômato", furia=True)
        inimigo["habilidade"] = "Golpe de Fundicao (Causa dano de fogo acumulativo)"
        return inimigo
        
    elif tipo == "gomorra_guardiao" or tipo == "guardiao_gomorra_novo":
        inimigo = dicstatus(nome="$0b3r4n0 da Fundicao (GUARDIÃO)", terceiraforma=True)
        inimigo["habilidade"] = "Sinal da Besta (Força o chip neural a superaquecer)"
        return inimigo

    else:
        # Passa o nome para o inimigo padrão original
        inimigo = dicstatus(nome="Serafim de Ferro")
        inimigo["habilidade"] = "Varredura Piramidal"
        return inimigo

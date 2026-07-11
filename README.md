# Cromo-RPG

[🇧🇷 Versão em Português](#versão-em-português) | [🇺🇸 English Version](#english-version)


---

## Versão em Português

### 📸 logo
<div align="center">
  <img width="677" height="369" alt="cromologo" src="https://github.com/user-attachments/assets/a3475956-c647-4eec-b7df-15ce6a0c94bf" />

</div>

### 📝 Descrição
O **Cromo-RPG** é um jogo de interpretação de papéis (RPG) baseado em texto desenvolvido em Python. Ambientado em um futuro distópico e tecnológico dominado por inteligências artificiais e hordas de robôs, o jogador assume o papel de um sobrevivente cujo DNA é a única chave para libertar a humanidade de colmeias digitais. O sistema conta com mecânicas de combate por turnos, gerenciamento de inventário, uso de itens (seringas e armas), progressão de nível e estatísticas dinâmicas de fim de jogo.

### 🚀 Funcionalidades Principais (Blocos de Código)

O core do sistema gerencia toda a lógica utilizando estruturas puras de dados e controle de fluxo em Python. Abaixo estão as principais funções do motor do jogo:

#### 1. Fluxo de Execução Principal (`main.py`)
Controla o início do jogo, a inicialização do jogador, a introdução da lore e o loop principal da horda contínua de inimigos aleatórios.
```python
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
```
2. Loop de Combate Turno a Turno (luta.py)
Gerencia o menu iterativo de escolhas do jogador (Atacar, Fugir, Curar, Inventário) e dita as ações aleatórias do oponente robótico.

```python
def combate(robo="comum", qtd=0):
    global jogador, inimigo, chance, fuga, moedas, matou, morreu
    jogador = get_personagem().copy()
    vida_maxima_jogador = jogador.get("vida", 100)
    nome = get_ps()
    inimigo = criarinimigo(robo)

    while jogador.get("vida", 0) > 0 and inimigo.get("vida", 0) > 0:
        ordem = turno(nome, "walker")
        
        for atacante in ordem:
            if verifica_morte(jogador) or verifica_morte(inimigo):
                break
                
            if atacante == nome:
                mudarcenario("Atacar", "Fugir", "Curar", "Inventario")
                opcao = escolhe()
              
                if opcao == 0:
                    calcular_ataque(jogador, inimigo, is_player=True, nome_atacante=nome)
```
3. Gerador de Inimigos com Dicionários (inimigo.py)
Aplica modificadores de atributos (ataque, defesa, vida, cura) dependendo da classe ou comportamento do droide gerado.

```Python
def dicstatus(nome="Droide Comum", ataque=25, vida=75, defesa=5, cura=8, segundaforma=False, furia=False, fatordecura=False):
    if segundaforma == True:
        walkerboss = dict()
        walkerboss["nome"] = nome
        walkerboss["ataque"] = ataque + 3
        walkerboss["defesa"] = defesa + 1
        walkerboss["cura"] = cura + 3
        walkerboss["vida"] = vida * 2
        walkerboss["furia"] = ataque * 2
        return walkerboss
    elif furia == True:
        walkerraivoso = dict()
        walkerraivoso["nome"] = nome
        walkerraivoso["ataque"] = ataque
        walkerraivoso["defesa"] = defesa
        walkerraivoso["cura"] = cura
        walkerraivoso["vida"] = vida
        walkerraivoso["furia"] = ataque * 2
        return walkerraivoso
    elif fatordecura == True:
        walkermedico = dict()
        walkermedico["nome"] = nome
        walkermedico["ataque"] = ataque
        walkermedico["defesa"] = defesa + 4
        walkermedico["cura"] = cura * 2
        walkermedico["vida"] = vida + 5
        return walkermedico
    else:
        walker = dict()
        walker["nome"] = nome
        walker["ataque"] = ataque
        walker["defesa"] = defesa
        walker["cura"] = cura
        walker["vida"] = vida
        return walker
```

🔗 Saiba mais sobre as funções adicionais (Cenários, Itens e Validadores) para facilitar o desenvolvimento.

🛠️ Tecnologias Utilizadas
Python 3: Linguagem base para todo o desenvolvimento.

Dicionários e Estruturas Dinâmicas: Armazenamento em tempo real de inventários e status.

Manipulação de Cores ANSI: Customização estética do terminal para imersão Cyberpunk.

📦 Funções Adicionais - PT
Sistema de Cenários e Escolhas (cenario.py)
```Python
def mudarcenario(*cenario):
    cenarios[0] = list(cenario)
    arrumarlista()
    return cenarios
```
```Python
def escolhe():
   mostraropcoes()
   opcao = verificarnumero("\033[33m>>>>>\033[0m")
   return opcao
```
Estrutura de Itens e Seringas (items.py)
```Python
SERINGAS = [ 
    ("Adrenalina", "dano", 16, 2),
    ("Sangue", "cura", 14, 2),
    ("Trevo", "sorte", 50, 1)
]

ARMAS = [
    ("pé de cabra", "Contato", 15, 0),
    ("Plasma", "Raio", 30, 0),
    ("HellFire", "Fogo", 25, 0),
    ("Tsunami", "Agua", 40, 0),  
    ("TerraForm", "Pedra", 35, 0)
]
```
Tratamento de Erros de Input (verificadores.py)
```Python
def verificarnumero(prompt=">>>>"):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Digite apenas números válidos.")
````
## English Version
📸 Demonstration
📝 Description
Cromo-RPG is a text-based role-playing game developed in Python. Set in a dystopian, technological future dominated by artificial intelligence and cybernetic rogue waves, the player steps into the shoes of a survivor whose DNA holds the master key to saving humanity from digital hives. The project implements procedural turn-based combat, robust inventory management, utility item consumption (syringas and weapons), level progression, and post-game dynamic statistics.

🚀 Main Features (Code Blocks)
The engine coordinates the whole execution using native Python structures and loops. Below are the key functions powering the project:

1. Core Execution Flow (main.py)
Initializes the user parameters, boots the environmental lore narrative, and loops the persistent incoming droid onslaught waves.

```Python
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

    print("\033[33m[ SYSTEM ALERT: Robot hordes are closing in... ]\033[0m\n")
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
```
2. Turn-By-Turn Combat Engine (luta.py)
Draws interactive options menus for the player (Attack, Flee, Heal, Inventory) and simulates random AI actions for hostile targets.

````Python
def combate(robo="comum", qtd=0):
    global jogador, inimigo, chance, fuga, moedas, matou, morreu
    jogador = get_personagem().copy()
    vida_maxima_jogador = jogador.get("vida", 100)
    nome = get_ps()
    inimigo = criarinimigo(robo)

    while jogador.get("vida", 0) > 0 and inimigo.get("vida", 0) > 0:
        ordem = turno(nome, "walker")
        
        for atacante in order:
            if verifica_morte(jogador) or verifica_morte(inimigo):
                break
                
            if atacante == nome:
                mudarcenario("Atacar", "Fugir", "Curar", "Inventario")
                opcao = escolhe()
              
                if opcao == 0:
                    calcular_ataque(jogador, inimigo, is_player=True, nome_atacante=nome)
````
3. Procedural Dictionary Enemy Spawner (inimigo.py)
Applies specific attribute multipliers (attack, defense, health, healing) according to the designated sub-class of the spawned droid unit.

````Python
def dicstatus(nome="Droide Comum", ataque=25, vida=75, defense=5, cura=8, segundaforma=False, furia=False, fatordecura=False):
    if segundaforma == True:
        walkerboss = dict()
        walkerboss["nome"] = nome
        walkerboss["ataque"] = ataque + 3
        walkerboss["defesa"] = defesa + 1
        walkerboss["cura"] = cura + 3
        walkerboss["vida"] = vida * 2
        walkerboss["furia"] = ataque * 2
        return walkerboss
    elif furia == True:
        walkerraivoso = dict()
        walkerraivoso["nome"] = nome
        walkerraivoso["ataque"] = ataque
        walkerraivoso["defesa"] = defesa
        walkerraivoso["cura"] = cura
        walkerraivoso["vida"] = vida
        walkerraivoso["furia"] = ataque * 2
        return walkerraivoso
    elif fatordecura == True:
        walkermedico = dict()
        walkermedico["nome"] = nome
        walkermedico["ataque"] = ataque
        walkermedico["defesa"] = defesa + 4
        walkermedico["cura"] = cura * 2
        walkermedico["vida"] = vida + 5
        return walkermedico
    else:
        walker = dict()
        walker["nome"] = nome
        walker["ataque"] = ataque
        walker["defesa"] = defesa
        walker["cura"] = cura
        walker["vida"] = vida
        return walker
`````
🔗 Learn more about additional functions (Scenes, Items, and Validators) to streamline development.

🛠️ Built With
Python 3: Core language framework.

Dictionaries & Data Mapping: Real-time state structures for game objects.

ANSI Terminal Escape Codes: Terminal rendering coloring for a retro Cyberpunk theme.

📦 Additional Functions - EN
Scenario & Choice System (cenario.py)
````Python
def mudarcenario(*cenario):
    cenarios[0] = list(cenario)
    arrumarlista()
    return cenarios

def escolhe():
   mostraropcoes()
   opcao = verificarnumero("\033[33m>>>>>\033[0m")
   return opcao
````
Items & Syringes Database Structure (items.py)
````Python
SERINGAS = [ 
    ("Adrenalina", "dano", 16, 2),
    ("Sangue", "cura", 14, 2),
    ("Trevo", "sorte", 50, 1)
]

ARMAS = [
    ("pé de cabra", "Contato", 15, 0),
    ("Plasma", "Raio", 30, 0),
    ("HellFire", "Fogo", 25, 0),
    ("Tsunami", "Agua", 40, 0),  
    ("TerraForm", "Pedra", 35, 0)
]
````
Input Exception Handling (verificadores.py)
````Python
def verificarnumero(prompt=">>>>"):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Please enter valid numbers only.")
````

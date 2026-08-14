from time import sleep
from cenario import escolhe, mudarcenario
from ilustração import limpartela
from inventario import inventario
from prelore import print_alerta, print_lore

# Importando a função de combate do arquivo luta.py
from luta import combate

TEMPO_TESTE = 0


def mapa():
    global sub_cenario

    opcoes_gomorra = [
        "Enfrentar o Operário Autômato (Fundição)",
        "Enfrentar o Serafim de Ferro (Descarte)",
        "Enfrentar o Verme da Lixeira (Prensas)",
        "DESAFIAR O GUARDIÃO: Soberano da Fundição",
        "Voltar para a tubulação",
    ]

    opcoes_sodoma = [
        "Enfrentar o Flagelo de Sodoma",
        "Enfrentar o Robô Cirúrgico Desertor",
        "Enfrentar o Colhedor de Bio-matéria",
        "DESAFIAR O GUARDIÃO: O Quimera de Carne",
        "Voltar para a tubulação",
    ]

    opcoes_babilonia = [
        "Enfrentar o Mercador",
        "Enfrentar o Corretor",
        "Enfrentar o Agenciador",
        "DESAFIAR O GUARDIÃO: O Cobrador de Almas",
        "Mercado abandonado",
        "Voltar para a tubulação",
    ]

    while True:
        limpartela()
        print_lore("Diante das saídas da tubulação, Ravi puxa o tablet iluminado.")
        print_lore("Ele gesticula rapidamente e a tela sintética traduz para você:")
        sleep(2 * TEMPO_TESTE)

        print("Escolha para qual setor deseja ir:")
        cenario = mudarcenario("Gomorra", "Sodoma", "Babilônia")
        opcao = escolhe()

        # ==========================================
        #             SETOR GOMORRA
        # ==========================================
        if opcao == 0:
            limpartela()
            print_lore("Você empurra a grade de ferro e pisa em Gomorra.")
            sleep(2 * TEMPO_TESTE)
            print_lore(
                "O ar é denso e pesado. O cheiro nojento de enxofre e óleo queimado impregna na garganta."
            )
            sleep(2.5 * TEMPO_TESTE)

            print_lore("Ravi digita no tablet e mostra a tela:")
            print(
                "\033[36m[TABLET DO RAVI]: 'Em Gomorra precisamos enfrentar as máquinas e derrubar o Guardião do setor!'\033[0m"
            )
            sleep(2.5 * TEMPO_TESTE)

            mudarcenario(*opcoes_gomorra)
            sub_opcao = escolhe()

            # Validação de segurança para evitar IndexError
            if not (0 <= sub_opcao < len(opcoes_gomorra)):
                print_alerta("Opção inválida!")
                continue

            escolha_texto = opcoes_gomorra[sub_opcao]
            venceu = False

            if escolha_texto == "Voltar para a tubulação":
                limpartela()
                print_lore("Vocês recuam para a ventilação antes de atrair mais atenção.")
                continue

            elif escolha_texto == "Enfrentar o Operário Autômato (Fundição)":
                limpartela()
                print_lore("Vocês avançam até o calor dos altos-fornos. Um autômato em fúria opera as máquinas!")
                print("\033[36m[TABLET DO RAVI]: 'Cuidado! É um Operário Autômato! O núcleo dele está superaquecido em FÚRIA!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("gomorra_comum3")

            elif escolha_texto == "Enfrentar o Serafim de Ferro (Descarte)":
                limpartela()
                print_lore("Nas esteiras de descarte, lâminas afiadas cortam o ar. Uma sombra mecânica desce do teto!")
                print("\033[36m[TABLET DO RAVI]: 'Atenção! Um Serafim de Ferro bloqueia a passagem! Não deixe ele cortar suas defesas!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("gomorra_comum1")

            elif escolha_texto == "Enfrentar o Verme da Lixeira (Prensas)":
                limpartela()
                print_lore("Entre o lixo de silício e prensas, algo disforme rasteja em direção aos seus pés.")
                print("\033[36m[TABLET DO RAVI]: 'Um Verme da Lixeira de Silício! Cuidado, ele usa Pulso EMP para desativar nossas habilidades!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("gomorra_comum2")

            elif escolha_texto == "DESAFIAR O GUARDIÃO: Soberano da Fundição":
                limpartela()
                print_lore("O chão treme. As portas da grande fornalha se abrem e o líder de Gomorra surge!")
                print("\033[36m[TABLET DO RAVI]: 'É o $0b3r4n0 da Fundição! Ele carrega o Sinal da Besta! Dê tudo de si nesse combate!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("gomorra_guardiao")

            # Remove o inimigo derrotado mantendo a opção de sair intacta
            if venceu and sub_opcao < len(opcoes_gomorra) - 1:
                opcoes_gomorra.pop(sub_opcao)

        # ==========================================
        #             SETOR SODOMA
        # ==========================================
        elif opcao == 1:
            limpartela()
            print_lore("Você avança pelo túnel úmido e sai no Setor Sodoma.")
            sleep(2 * TEMPO_TESTE)
            print_lore("Luzes violeta neon piscam fracamente enquanto o cheiro de fluídos domina o ar.")
            sleep(2.5 * TEMPO_TESTE)

            mudarcenario(*opcoes_sodoma)
            sub_opcao = escolhe()

            if not (0 <= sub_opcao < len(opcoes_sodoma)):
                continue

            escolha_texto = opcoes_sodoma[sub_opcao]
            venceu = False

            if escolha_texto == "Voltar para a tubulação":
                limpartela()
                print_lore("Vocês dão meia-volta e retornam para o esgoto.")
                continue

            elif escolha_texto == "Enfrentar o Flagelo de Sodoma":
                limpartela()
                print_lore("Uma besta descontrolada surge das sombras com os olhos injetados em sangue!")
                print("\033[36m[TABLET DO RAVI]: 'É o Flagelo de Sodoma! A raiva dele aumenta o ataque a cada segundo!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("sodoma_comum1")

            elif escolha_texto == "Enfrentar o Robô Cirúrgico Desertor":
                limpartela()
                print_lore("Bisturis mecânicos estalam nas trevas de um laboratório abandonado.")
                print("\033[36m[TABLET DO RAVI]: 'Um Robô Cirúrgico Desertor! Ele tem blindagem alta e quer cortar nossa carcaça!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("sodoma_comum2")

            elif escolha_texto == "Enfrentar o Colhedor de Bio-matéria":
                limpartela()
                print_lore("Uma máquina pesada com sacos de coleta avança na Galeria de Ilusões.")
                print("\033[36m[TABLET DO RAVI]: 'Ali está o Colhedor de Bio-matéria! Não deixe ele te acertar com as serras!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("sodoma_comum3")

            elif escolha_texto == "DESAFIAR O GUARDIÃO: O Quimera de Carne":
                limpartela()
                print_lore("O teto racha e uma abominação viva e metálica despenca na sua frente!")
                print("\033[36m[TABLET DO RAVI]: 'O Qu1m3r4 de C4rn3 se revelou! Ele usa Enxerto de Metal para criar escudos invencíveis!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("sodoma_guardiao")
        





            if venceu and sub_opcao < len(opcoes_sodoma) - 1:
                opcoes_sodoma.pop(sub_opcao)

        # ==========================================
        #             SETOR BABILÔNIA
        # ==========================================
        elif opcao == 2:
            limpartela()
            print_lore("Você sobe uma escada de metal e emerge nas ruas de Babilônia.")
            sleep(2 * TEMPO_TESTE)
            print_lore("O brilho incansável dos hologramas de Abaddon cega seus olhos.")
            sleep(2.5 * TEMPO_TESTE)

            mudarcenario(*opcoes_babilonia)
            sub_opcao = escolhe()

            if not (0 <= sub_opcao < len(opcoes_babilonia)):
                print_alerta("Opção inválida!")
                continue

            escolha_texto = opcoes_babilonia[sub_opcao]
            venceu = False

            if escolha_texto == "Voltar para a tubulação":
                limpartela()
                print_lore("Vocês entram no bueiro e recuam para a tubulação.")
                continue

            elif escolha_texto == "Enfrentar o Mercador":
                limpartela()
                print_lore("Um negociante com tentáculos digitais bloqueia o callejón.")
                print("\033[36m[TABLET DO RAVI]: 'Um Mercador! Cuidado, ele usa Suborno para roubar nossos créditos durante a luta!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("babilônia_comum1")

            elif escolha_texto == "Enfrentar o Corretor":
                limpartela()
                print_lore("Um agente engravatado de ferro surge dos guichês do banco.")
                print("\033[36m[TABLET DO RAVI]: 'É o Corretor! A defesa dele é alta, prepare ataques pesados!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("babilônia_comum2")

            elif escolha_texto == "Enfrentar o Agenciador":
                limpartela()
                print_lore("Um droide com módulos médicos e bancários aparece nas ruínas.")
                print("\033[36m[TABLET DO RAVI]: 'O Agenciador está na área! Ele se cura rapidamente se não for destruído logo!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("babilônia_comum3")

            elif escolha_texto == "DESAFIAR O GUARDIÃO: O Cobrador de Almas":
                limpartela()
                print_lore("As luzes neon piscam e uma presença sombria e imponente surge no templo!")
                print("\033[36m[TABLET DO RAVI]: 'Atenção! O C0br4d0r de 4lm45 apareceu! A habilidade Contrato de Sangue dele ignora nossas defesas!'\033[0m")
                sleep(2 * TEMPO_TESTE)
                venceu = combate("babilônia_guardiao")
            
                
            if venceu and sub_opcao < len(opcoes_babilonia) - 1:
                opcoes_babilonia.pop(sub_opcao)

        else:
            print_alerta("Opção inválida! Escolha um caminho válido.")



mapa()
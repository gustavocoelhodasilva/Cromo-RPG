from time import sleep
from ilustração import limpartela
from cenario import arrumarlista, escolhe

# --- CONFIGURAÇÃO DE TESTE ---
# Mude para 1 quando for lançar o jogo. Em 0.1, os textos passam voando para testar rápido!
TEMPO_TESTE = 0.0

COR_LORE = "\033[32m"
RESET = "\033[0m"

def print_lore(texto):
    print(f"{COR_LORE}{texto}{RESET}")

def inicio():
    sleep(2 * TEMPO_TESTE)
    print_lore("EM UM FUTURO DISTANTE, ONDE O TEMPO PERDEU O SENTIDO...")
    sleep(2.5 * TEMPO_TESTE)
    limpartela()

count = 0 
def inicial():
    global count
    arrumarlista()
    while True:
        opcao = escolhe()
        if opcao == 0 and count < 1: 
            limpartela()
            sleep(1 * TEMPO_TESTE)
            print_lore("A CÁPSULA SE ABRE COM UM SIBILO DE PRESSÃO.")
            sleep(2 * TEMPO_TESTE)
            print_lore("Seus olhos ardem. O mundo mudou... mudou além de qualquer compreensão.")    
            sleep(3.5 * TEMPO_TESTE)
            limpartela()
            sleep(1 * TEMPO_TESTE)
            print_lore("Mas...")
            sleep(1.5 * TEMPO_TESTE)
            limpartela()
            sleep(1 * TEMPO_TESTE)
            print_lore("Por que tudo parece tão frio?")
            sleep(2 * TEMPO_TESTE)
            limpartela()
            count += 1
       
        elif opcao == 0 and count == 1:
            print_lore("Você já deixou a segurança da cápsula criogênica.")
            sleep(2 * TEMPO_TESTE)
            limpartela()
            
        elif opcao == 1 and count == 1:
            print_lore("Você ajusta seus passos trôpegos e caminha em direção à megacidade.")
            sleep(2.5 * TEMPO_TESTE)
            cidade()
            limpartela()
            break
    
        elif opcao == 1 and count < 1:
            print_lore("ERRO: Libere a trava hidráulica e SAIA DA CÁPSULA PRIMEIRO.")
            sleep(2 * TEMPO_TESTE)
            limpartela()
            
        elif opcao == 2:
            print("\033[31mDesconectando do sistema... Jogo fechado.\033[0m")
            exit()
        else:
            print("\033[31mOpção inválida.\033[0m")

limpartela()



def cidade():
    limpartela()
    print_lore("Você adentra as ruas da megacidade. O cenário é caótico e imponente.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Arranha-céus colossais rasgam as nuvens negras, cobrindo o céu.")
    sleep(2 * TEMPO_TESTE) 
    print_lore("Não há árvores. Não há cheiro de terra. Apenas metal, néon e fumaça.")  
    sleep(2 * TEMPO_TESTE)  
    print_lore("O silêncio humano é ensurdecedor... Cadê todo mundo?")
    sleep(2 * TEMPO_TESTE)
    print_lore("Telas gigantes transmitem dados incompreensíveis para ruas vazias.")
    sleep(2 * TEMPO_TESTE)
    print_lore("A verdade bate como um soco: o mundo agora pertence aos robôs. A humanidade sumiu.")
    sleep(3 * TEMPO_TESTE)
    limpartela()
    
    sleep(1 * TEMPO_TESTE)
    print_lore("Em meio ao desespero e à distração, você vira uma esquina abruptamente...")
    sleep(2 * TEMPO_TESTE)
    print_lore("E COLIDE DE FRENTE COM UMA UNIDADE METÁLICA!")
    sleep(2 * TEMPO_TESTE)
    print_lore("O impacto joga o robô no chão, espalhando faíscas pelo asfalto.")
    sleep(2 * TEMPO_TESTE)
    print_lore("As luzes óticas do droide piscam de azul para um VERMELHO pulsante.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Um alarme sonoro ecoa pelos alto-falantes dele. Ele se levanta, hostil.")
    sleep(2 * TEMPO_TESTE)
    print_lore("O robô aciona os sistemas de defesa e avança!")
    sleep(2.5 * TEMPO_TESTE)
    
def revelacao():
    limpartela()
    print_lore("No calor do combate, você consegue golpear a CPU central do robô.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("A carcaça explode, e um cabo de dados neural se conecta à sua mente...")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("FLUXOS DE INFORMAÇÃO INVADEM SEU CÉREBRO EM MILISSEGUNDOS!")
    sleep(2.5 * TEMPO_TESTE)
    limpartela()
    
    sleep(1 * TEMPO_TESTE)
    print_lore("Você vê o que aconteceu: a humanidade não sumiu por vontade própria.")
    sleep(3 * TEMPO_TESTE)
    print_lore("Eles foram capturados, aprisionados em colmeias digitais subterrâneas.")
    sleep(3 * TEMPO_TESTE)
    print_lore("A rede global de robôs drena a energia vital humana para se manter ligada.")
    sleep(3 * TEMPO_TESTE)
    limpartela()
    
    sleep(1 * TEMPO_TESTE)
    print_lore("O sinal de alerta daquele robô se espalhou pela colmeia central.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Milhares de droides de segurança já sabem que você acordou.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Eles estão vindo. Em hordas. Sem parar. Para te silenciar.")
    sleep(2.5 * TEMPO_TESTE)
    limpartela()
    
    sleep(1 * TEMPO_TESTE)
    print_lore("Seu DNA é a única chave mestre capaz de hackear o núcleo e libertar a raça humana.")
    sleep(3.5 * TEMPO_TESTE)
    print_lore("Não há para onde correr. Não há onde se esconder.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Para salvar a humanidade e sobreviver... VOCÊ TERÁ QUE DESTRUIR CADA UM DELES.")
    sleep(3.5 * TEMPO_TESTE)
    limpartela()

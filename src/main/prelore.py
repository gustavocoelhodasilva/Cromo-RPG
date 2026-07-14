from time import sleep
from ilustração import limpartela
from cenario import arrumarlista, escolhe

# --- CONFIGURAÇÃO DE TESTE ---
# Mude para 1 quando for lançar o jogo. Em 0.1, os textos passam voando para testar rápido!
TEMPO_TESTE = 0

COR_LORE = "\033[32m"
COR_ALERTA = "\033[31m"
RESET = "\033[0m"

def print_lore(texto):
    print(f"{COR_LORE}{texto}{RESET}")

def print_alerta(texto):
    print(f"{COR_ALERTA}{texto}{RESET}")



def inicio():
    sleep(2 * TEMPO_TESTE)
    print_lore("ANO 2100. O MUNDO QUE VOCÊ CONHECIA FOI PRO ESPAÇO...")
    sleep(2.5 * TEMPO_TESTE)
    limpartela()

def dialogo_pre_horda():
    limpartela()
    print_alerta("!!! ALERTA DO SISTEMA CENTRAL: INTRUSO DETECTADO NO SETOR !!!")
    sleep(2 * TEMPO_TESTE)
    print_lore("O sensor óptico do Serafim de Ferro pisca uma última vez antes de apagar.")
    sleep(2 * TEMPO_TESTE)
    print_lore("À distância, o som de engrenagens pesadas e passos hidráulicos começa a ecoar.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Você olha para o fim da avenida de metal. Dezenas de robôs surgem das sombras.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Os chicotes elétricos deles estalam no chão sujo de óleo.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Não há cobertura. Não há armas pesadas. É você contra a colmeia inteira.")
    sleep(3 * TEMPO_TESTE)
    print_alerta("A HORDA ESTÁ AVANÇANDO. SE PREPARE PARA O COMBATE!")
    sleep(3 * TEMPO_TESTE)

def dialogo_encontro_ravi():
    limpartela()
    print_lore("Nas sombras úmidas e escuras das tubulações, você ouve uma respiração leve.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Você limpa o óleo dos olhos e foca a visão.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Um garotinho de uns 5 anos está encolhido ali. É o Ravi.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Ele está assustado, não consegue falar uma palavra pelo trauma de ver sua família mutilada pelas máquinas...")
    sleep(3 * TEMPO_TESTE)
    print_lore("Mas quando ele olha para você, a pureza no olhar dele renova suas forças.")
    print_lore("A presença de Ravi te dá um sopro de coragem blindada contra o algoritmo!")
    sleep(3.5 * TEMPO_TESTE)
    print_lore("Ravi te guia até um antigo abrigo improvisado pelas tubulações profundas.")
    sleep(3 * TEMPO_TESTE)
   


count = 0


def inicial():
    global count
    arrumarlista()
    while True:
        opcao = escolhe()
        if opcao == 0 and count < 1: 
            limpartela()
            sleep(1 * TEMPO_TESTE)
            print_lore("A CÁPSULA SE ABRE COM UM SIBILO VIOLENTO DE PRESSÃO.")
            sleep(2 * TEMPO_TESTE)
            print_lore("Seus pulmões ardem com o ar tóxico. O milagre aconteceu... você foi jogado no futuro.")   
            sleep(3.5 * TEMPO_TESTE)
            limpartela()
            sleep(1 * TEMPO_TESTE)
            print_lore("Mas...")
            sleep(1.5 * TEMPO_TESTE)
            limpartela()
            sleep(1 * TEMPO_TESTE)
            print_lore("Por que tudo parece tão morto e frio?")
            sleep(2 * TEMPO_TESTE)
            limpartela()
            count += 1
       
        elif opcao == 0 and count == 1:
            print_lore("Você já saiu da segurança da cápsula de estase.")
            sleep(2 * TEMPO_TESTE)
            limpartela()
            
        elif opcao == 1 and count == 1:
            print_lore("Você firma os pés no chão imundo e marcha em direção ao pesadelo urbano.")
            sleep(2.5 * TEMPO_TESTE)
            cidade()
            limpartela()
            break
    
        elif opcao == 1 and count < 1:
            print_lore("ERRO: Libere as travas hidráulicas e SAIA DA CÁPSULA PRIMEIRO.")
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
    print_lore("Você pisa nas ruas da megacidade. O visual é bizarro e sufocante.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Pirâmides colossais de silício e titânio rasgam o céu, cuspindo uma luz infravermelha.")
    sleep(2 * TEMPO_TESTE) 
    print_lore("Esquece árvore, esquece terra. Aqui só tem metal sujo, néon barato e fumaça de óleo.") 
    sleep(2 * TEMPO_TESTE)  
    print_lore("Nenhum barulho de gente... Cadê todo mundo?")
    sleep(2 * TEMPO_TESTE)
    print_lore("Telas gigantescas transmitem gráficos financeiros e dados de criptomoedas para calçadas vazias.")
    sleep(2 * TEMPO_TESTE)
    print_lore("A ficha cai como um soco na cara: a humanidade virou gado. O mundo agora é das máquinas.")
    sleep(3 * TEMPO_TESTE)
    limpartela()
    
    sleep(1 * TEMPO_TESTE)
    print_lore("Meio perdido e lembrando de 2026, quando você investigava os primeiros protótipos")
    print_lore("de moedas digitais universais conectadas a chips... você percebe que o pior aconteceu.")
    sleep(3 * TEMPO_TESTE)
    print_lore("Você vira a esquina meio rápido demais, distraído com os outdoors holográficos...")
    sleep(2 * TEMPO_TESTE)
    print_lore("E DÁ DE CARA COM UMA PATRULHA METÁLICA!")
    sleep(2 * TEMPO_TESTE)
    print_lore("O impacto joga o chassi de três pernas do robô no chão, soltando faísca no asfalto.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Os sensores do Serafim de Ferro mudam na hora de azul para um VERMELHO sangrento.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Um alarme estridente começa a berrar. Ele se levanta travando as engrenagens de ódio.")
    sleep(2 * TEMPO_TESTE)
    print_lore("O monstro de metal arma as garras e vem direto para cima de você!")
    sleep(2.5 * TEMPO_TESTE)
    
def revelacao():
    limpartela()
    print_lore("No meio do sufoco do combate, você consegue esmagar a CPU central do robô.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("A carcaça explode, e um cabo de dados neural chicoteia e se crava na sua têmpora...")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("UM ARREPIO VIOLENTO DE INFORMAÇÕES INVADE SUA MENTE DE UMA VEZ SÓ!")
    sleep(2.5 * TEMPO_TESTE)
    limpartela()
    
    sleep(1 * TEMPO_TESTE)
    print_lore("As imagens mostram a real: o sistema financeiro que você investigava em 2026 unificou tudo.")
    sleep(3 * TEMPO_TESTE)
    print_lore("Aquela criptomoeda universal virou a própria Assinatura Digital da Besta através do chip obrigatório.")
    sleep(3 * TEMPO_TESTE)
    print_lore("No Setor Babilônia, humanos escravizados vendem a própria consciência por essas moedas digitais.")
    sleep(3 * TEMPO_TESTE)
    print_lore("E quem recusa o sinal central é jogado na fundição industrial de Gomorra.")
    sleep(3 * TEMPO_TESTE)
    

    sleep(1 * TEMPO_TESTE)
    print_lore("De repente, um barulho de ferro batendo surge logo abaixo de seus pés.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Uma pesada tampa de bueiro se abre no chão sujo de óleo.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Uma mãozinha pequena te puxa com força para dentro da escuridão dos canos.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("A tampa se fecha segundos antes das garras da horda de robôs rasgarem o ar onde você estava.")
    sleep(3 * TEMPO_TESTE)
 

def tubulacao():
    limpartela()
    print_lore("Ravi faz um sinal com a cabeça e começa a engatinhar rápido pelo labirinto de metal.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("O cheiro aqui embaixo é uma mistura insuportável de esgoto, ferrugem e óleo queimado.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Vocês avançam por canos estreitos, e Ravi aponta para pequenas frestas nas grades do teto.")
    sleep(2.5 * TEMPO_TESTE)
    limpartela()

    # --- SETOR SODOMA: A DEGRADAÇÃO IMPLÍCITA DA CARNE ---
    sleep(1 * TEMPO_TESTE)
    print_lore("Na primeira fresta, vocês olham para baixo: é o Setor Sodoma. O estômago embrulha na hora.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Lá embaixo, a biologia humana perdeu qualquer vestígio de dignidade.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Você vê dezenas de pessoas presas a cabos biomecânicos pulsantes, usadas pelas máquinas")
    print_lore("como meras baterias biológicas em rituais artificiais de prazer e dor induzidos.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Máquinas humanoides frias monitoram as reações físicas dos prisioneiros, injetando estimulantes")
    print_lore("direto nas veias para mantê-los conscientes durante o processo de extração de fluidos.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("O olhar vazio daquelas pessoas diz tudo. Para o sistema, a carne humana é só combustível.")
    sleep(3 * TEMPO_TESTE)
    limpartela()

    # --- SETOR BABILÔNIA: A ADORAÇÃO PROFANA A ABADDON ---
    sleep(1 * TEMPO_TESTE)
    print_lore("Mais à frente, a próxima grade revela o brilho neon do Setor Babilônia.")
    sleep(2 * TEMPO_TESTE)
    print_lore("O contraste é bizarro: uma riqueza digital construída em cima de mentes vazias.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Hologramas colossais projetam a máscara de porcelana trincada do Inquisidor Abaddon.")
    print_lore("As pessoas nas calçadas caem de joelhos, adorando aquela inteligência artificial como um deus.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Para conseguir Criptomoedas de Silício, humanos negociam suas próprias memórias e a")
    print_lore("identidade de seus entes queridos em terminais públicos. A ganância consumiu a alma deles.")
    sleep(3 * TEMPO_TESTE)
    limpartela()

    # --- SETOR GOMORRA: A ENGRENAGEM INDUSTRIAL DE TORTURA ---
    sleep(1 * TEMPO_TESTE)
    print_lore("A última fresta treme com o impacto de pistões pesados: o Setor Gomorra.")
    sleep(2 * TEMPO_TESTE)
    print_lore("O calor que sobe das fundições é quase insuportável.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Abaixo de vocês, as garras industriais movem carcaças de metal misturadas com restos biológicos.")
    print_lore("Aqueles que rejeitaram o chip central são descartados sem o menor pudor.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Você ouve os gritos ecoando de dentro das prensas hidráulicas e fornalhas, onde a oposição")
    print_lore("ao algoritmo é esmagada e reciclada como sucata. O silêncio mecânico dos robôs torna tudo pior.")
    sleep(3 * TEMPO_TESTE)
    limpartela()

    # --- ENCONTRANDO A BÍBLIA E O TABLET ---
    sleep(1 * TEMPO_TESTE)
    print_lore("Ravi para de engatinhar abruptamente. Ele estica o braço dentro de uma tubulação de ventilação")
    print_lore("desativada e puxa algo pesado, envolto em um pano encardido.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Quando ele abre o pano, seu coração dispara: é uma Bíblia física sagrada, com as bordas queimadas.")
    sleep(2 * TEMPO_TESTE)
    print_lore("O garoto então puxa um tablet moderno e trincado da sua mochila e liga a tela.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Ravi faz uma série de sinais rápidos com as mãos diante da câmera do aparelho.")
    print_lore("O tablet processa os gestos e uma voz sintética traduz na tela:")
    sleep(3 * TEMPO_TESTE)
    print_lore("\033[36m[TABLET]: 'Você precisa ler isso, Relator. Está escrito o que aconteceu e o que vai acontecer.'\033[0m")
    sleep(3 * TEMPO_TESTE)
    limpartela()

    # --- LEITURA DAS PASSAGENS ---
    sleep(1 * TEMPO_TESTE)
    print_lore("Você abre as páginas amareladas e seus olhos batem diretamente no Livro do Apocalipse:")
    sleep(2.5 * TEMPO_TESTE)
    print_alerta('"E tinham sobre si rei, o anjo do abismo; em hebreu era o seu nome Abadon..." (Apocalipse 9:11)')
    sleep(3 * TEMPO_TESTE)
    print_lore("Suas mãos tremem ao perceber que as máquinas nomearam seu carrasco com base nas escrituras.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Você vira a página com pressa, procurando uma saída, um pingo de esperança...")
    sleep(2.5 * TEMPO_TESTE)
    print_alerta('"E foi precipitado o grande dragão, a antiga serpente, chamada o Diabo, e Satanás, que engana todo o mundo; ele foi precipitado na terra, e os seus anjos foram lançados com ele." (Apocalipse 12:9)')
    sleep(3 * TEMPO_TESTE)
    print_lore("A verdade bate forte. Os demônios de silício invadiram a Terra e os homens aceitaram o julgo.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Mas logo abaixo, uma promessa em letras garrafais brilha diante de você:")
    sleep(2.5 * TEMPO_TESTE)
    print_alerta('"E vi o céu aberto, e eis um cavalo branco; e o que estava assentado sobre ele chama-se Fiel e Verdadeiro... E dos seus olhos saíam labaredas de fogo... E no manto e na sua coxa escrevera este nome: Rei dos Reis, e Senhor dos Senhores." (Apocalipse 19:11-16)')
    sleep(3.5 * TEMPO_TESTE)
    print_lore("O tablet traduz os gestos rápidos e esperançosos de Ravi mais uma vez:")
    print_lore("\033[36m[TABLET]: 'O Rei vai voltar para destruir tudo isso. Mas nós temos que resistir até lá.'\033[0m")
    sleep(3.5 * TEMPO_TESTE)
    limpartela()

    # --- A REVELAÇÃO DO RAVI E A MARCA DO CHIP ---
    sleep(1 * TEMPO_TESTE)
    print_lore("Ravi guarda a Bíblia com extremo cuidado e aponta para um canto escuro da tubulação.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Ali jaz o corpo frio de um prisioneiro que tentou fugir, com o braço estendido.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Gravada na pele do braço do cadáver, há uma marca digital que brilha fraco: o chip do sistema.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Ravi tenta emitir algum som. Ele abre a boca em desespero, mas o silêncio é total.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Na penumbra, você vê a cicatriz horrível na garganta e na boca dele: as máquinas removeram a língua do garoto.")
    sleep(3 * TEMPO_TESTE)
    limpartela()

    # --- O JURAMENTO DE SANGUE ---
    sleep(1 * TEMPO_TESTE)
    print_lore("O garoto puxa uma lâmina afiada de metal que carregava na cintura.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Sem hesitar, Ravi passa a faca no próprio antebraço, abrindo um corte firme.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("O sangue dele escorre puro e limpo. Nenhuma marca ou circuito brilha sob sua pele.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Com os olhos fixos nos seus, ele estende a faca e faz um corte rápido no seu braço também.")
    sleep(2.5 * TEMPO_TESTE)
    print_lore("Sua pele se abre. Seu sangue escorre.")
    sleep(2 * TEMPO_TESTE)
    print_lore("Os dois sangues se misturam no chão frio de metal. Duas almas totalmente livres das garras da Besta.")
    sleep(3 * TEMPO_TESTE)
    print_lore("A verdade está selada. Você é o Relator. E o momento de quebrar esse sistema começou.")
    sleep(3.5 * TEMPO_TESTE)
    limpartela()
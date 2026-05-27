import random

from combate import iniciar_batalha
from configuracoes import (
    DADOS_ANTI_AUTHORIZATUS,
    DADOS_GLOZIUM,
    DADOS_GLOZIUM_ADMINISTRATUS,
    DADOS_SANDUBINHA_REVERSE,
    DADOS_WORM,
    VIDA_ANTI_AUTHORIZATUS,
    VIDA_GARGULAS_CAPTCHAS,
    VIDA_GLOZIUM,
    VIDA_GLOZIUM_ADMINISTRATUS,
    VIDA_SANDUBINHA_REVERSE,
    VIDA_WORM,
)
from interface import divisor, falar, narrar, pedir_opcao
from itens import (
    AZAH_TRANSMISSAO,
    BOMBA_MAGICA,
    COLAR_ESTATUA_SAGRADA,
    ESPADA_ZG,
    FATURAMENTUS,
    GUIA_ATENDIMENTO,
    ITENS_DA_FORJA,
)
from personagens import Personagem


def finalizar_por_desistencia():
    """Final comum quando o jogador escolhe abandonar a missao."""
    narrar("Hot Dog desistiu da missao.")
    narrar("Sem o heroi, Glozium espalhou a escuridao pela provincia de Hospitalis.")
    narrar("Fim de jogo.")


def ato_um(heroi):
    """Executa a Floresta do Atendimentus e entrega o Guia de Atendimento."""
    divisor()
    narrar("ATO 1 - Floresta do Atendimentus")
    narrar("Mais ameacadora do que nunca, a floresta envolve Hot Dog em paisagens escuras e enevoadas.")
    falar("Sandubinha", "Na floresta de Atendimentus, encontre o ser Processus.")
    narrar("De repente, Salsichinha fareja algo e comeca a correr.")
    narrar("Hot Dog segue seu companheiro ate uma clareira.")
    narrar("Processus estava morto aos pes de uma criatura arrogante e sombria.")
    falar("Hot Dog", "Nao ha duvidas, você e o inimigo!")
    falar("Monstro", "Eu sou Anti-authorizatus! Agora e sua vez!")
    falar("Hot Dog", "Irei me vingar pelo amigo de meu pai!")

    monstro = Personagem(
        "Anti-authorizatus",
        vida_maxima=VIDA_ANTI_AUTHORIZATUS,
        quantidade_dados=DADOS_ANTI_AUTHORIZATUS,
    )
    resultado = iniciar_batalha(heroi, monstro)

    if resultado == "vitoria":
        # O Guia e o primeiro item obrigatorio para a forja da Espada ZG.
        narrar("O filho de Processus surge.")
        falar("Filho de Processus", "Muito obrigado. Tome o artefato Guia de Atendimento.")
        heroi.adicionar_item(GUIA_ATENDIMENTO)
        narrar("Item recebido: Guia de Atendimento.")
        return True

    if resultado == "desistiu":
        finalizar_por_desistencia()
        return False

    narrar("O filho de Processus chora estridentemente.")
    narrar("O monstro matou o filho de Processus e o mundo foi destruido por Glozium. Fim de jogo!")
    return False


def enigma_faturamentus(heroi):
    """Apresenta o enigma da fase 2 e aplica consequencias em caso de erro."""
    divisor()
    narrar("Hot Dog encontra tres passagens e um enigma antigo.")
    narrar('"Do enfermo vem o inicio, do registro o meio, do pagamento fim do anseio."')
    narrar('"Gira sem parar nos saloes do curar. Que ciclo e esse a sustentar?"')
    print("\nA - O Ciclum Receitatus Hospitalis")
    print("B - O Rito dos Curandeiros Eternos")
    print("C - A Roda da Vida e da Cura")

    opcao = pedir_opcao("Escolha a porta correta: ", ["a", "b", "c"])

    if opcao == "a":
        narrar("A passagem correta se abre diante de Hot Dog.")
        return 0

    if opcao == "b":
        heroi.vida_atual = max(1, heroi.vida_atual - 3)
        narrar("Hot Dog cai em uma armadilha e perde 3 de vida.")
        return 0

    narrar("Hot Dog segue pela porta errada. O chefe da fase recebe +7 de vida.")
    return 7


def ato_dois(heroi):
    """Executa as Cavernas de Faturamentus e entrega o item Faturamentus."""
    divisor()
    narrar("ATO 2 - Cavernas de Faturamentus")
    narrar("Avancando pela caverna, Hot Dog distingue ruidos metalicos distantes.")
    narrar("A luz de minerios incomuns revela caminhos perigosos.")

    vida_extra = enigma_faturamentus(heroi)

    narrar("Hot Dog alcanca um local onde os Ancioes do Faturamento trabalham sem notar sua presenca.")
    narrar("Um cavaleiro infernal forjado por Glozium afia sua espada.")
    falar("Glozium Administratus", "Voce e o heroi deste ano? Nao me parece grande coisa.")
    falar("Hot Dog", "Algumas piadas ruins podem ate me fazer rir. Voce e uma dessas.")

    monstro = Personagem(
        "Glozium Administratus",
        # Porta C aumenta a vida deste chefe em 7.
        vida_maxima=VIDA_GLOZIUM_ADMINISTRATUS + vida_extra,
        quantidade_dados=DADOS_GLOZIUM_ADMINISTRATUS,
    )
    resultado = iniciar_batalha(heroi, monstro)

    if resultado == "vitoria":
        narrar("Hot Dog supera o cavaleiro infernal das cavernas.")
        heroi.adicionar_item(FATURAMENTUS)
        narrar("Item recebido: Faturamentus.")
        return True

    if resultado == "desistiu":
        finalizar_por_desistencia()
        return False

    narrar("Glozium Administratus derrota Hot Dog.")
    narrar("O mundo foi destruido por Glozium. Fim de jogo!")
    return False


def ato_tres(heroi):
    """Executa a Vila da Transmissao e introduz a mecanica especial do Worm."""
    divisor()
    narrar("ATO 3 - Vila da Transmissao")
    narrar("Hot Dog e bem recebido em sua chegada.")
    narrar("Ele e convidado para um jantar ritualistico com comidas tipicas.")
    narrar("Enquanto Salsichinha saboreia um bife de calango, os moradores explicam o perigo local.")
    narrar("O monstro da vila se enterra. Para ataca-lo, primeiro sera necessario tira-lo do chao.")
    # A bomba e recebida antes do combate porque e obrigatoria para desenterrar o Worm.
    heroi.adicionar_item(BOMBA_MAGICA)
    narrar("Item recebido: Bomba Magica.")

    monstro = Personagem("Worm", vida_maxima=VIDA_WORM, quantidade_dados=DADOS_WORM)
    # Esta flag ativa as regras especiais de posicao dinamica no modulo combate.
    monstro.eh_worm = True
    resultado = iniciar_batalha(heroi, monstro)

    if resultado == "vitoria":
        narrar("Com Worm derrotado, a Vila da Transmissao volta a respirar em paz.")
        heroi.adicionar_item(AZAH_TRANSMISSAO)
        heroi.item_equipado = AZAH_TRANSMISSAO
        narrar("Item recebido e equipado: Azah Transmissao.")
        return True

    if resultado == "desistiu":
        finalizar_por_desistencia()
        return False

    narrar("Worm arrasta Hot Dog para baixo da terra.")
    narrar("A transmissao falha, Glozium avanca e o mundo e destruido. Fim de jogo!")
    return False


def ato_quatro(heroi):
    """Executa a Torre de Contas a Receber e o combate contra Sandubinha Reverse."""
    divisor()
    narrar("ATO 4 - Torre de Contas a Receber")
    narrar("Hot Dog chega ao primeiro andar da torre.")
    narrar("Salsichinha sente uma energia magica mortifera vindo do topo.")
    narrar("Sem duvidas, Glozium esta la.")
    narrar("A parede se abre, revelando o penultimo monstro da jornada.")
    falar("Sandubinha Reverse", "Tudo que voce usar contra mim sera devolvido contra voce.")
    falar("Hot Dog", "Entao vou terminar isso antes que voce aprenda demais.")

    monstro = Personagem(
        "Sandubinha Reverse",
        vida_maxima=VIDA_SANDUBINHA_REVERSE,
        quantidade_dados=DADOS_SANDUBINHA_REVERSE,
    )
    # Ativa a mecanica de copiar o ultimo item usado pelo heroi.
    monstro.copia_item = True
    resultado = iniciar_batalha(heroi, monstro)

    if resultado == "vitoria":
        narrar("Sandubinha Reverse desaparece nas rachaduras da torre.")
        heroi.adicionar_item(COLAR_ESTATUA_SAGRADA)
        narrar("Item recebido: Colar da Estatua Sagrada.")
        narrar("Hot Dog esta diante do caminho para o topo.")
        return True

    if resultado == "desistiu":
        finalizar_por_desistencia()
        return False

    narrar("Sandubinha Reverse derrota Hot Dog e abre caminho para Glozium.")
    narrar("Fim de jogo!")
    return False


def possui_itens_para_forja(heroi):
    """Verifica se todos os itens obrigatorios de fase foram coletados."""
    return all(heroi.possui_item(item) for item in ITENS_DA_FORJA)


def perguntar_forja_espada(heroi):
    """Permite forjar a Espada ZG antes da batalha final."""
    divisor()
    narrar("Hot Dog sente que Glozium esta no topo da Torre de Contas a Receber.")

    if not possui_itens_para_forja(heroi):
        narrar("Hot Dog ainda nao possui todos os itens necessarios para forjar a Espada ZG.")
        return

    narrar("Hot Dog possui todos os itens das fases.")
    print("\n1 - Voltar a Hospitalis e forjar a Espada ZG")
    print("2 - Enfrentar Glozium com a espada simples")
    opcao = pedir_opcao("Escolha: ", ["1", "2"])

    if opcao == "1":
        # A Espada ZG altera o final e evita o desafio das gargulas captchas.
        heroi.tem_espada_zg = True
        # A forja consome todos os itens do inventario, incluindo a espada inicial.
        heroi.itens = []
        heroi.item_equipado = None
        heroi.adicionar_item(ESPADA_ZG)
        heroi.espada_equipada = ESPADA_ZG
        narrar("Os ferreiros de Zerum Glozium unem os artefatos e forjam a Espada ZG.")
    else:
        narrar("Hot Dog decide enfrentar Glozium sem a Espada ZG.")


def desafio_gargulas(heroi):
    """Executa o par ou impar das gargulas quando o heroi nao tem a Espada ZG."""
    if heroi.tem_espada_zg:
        narrar("Com a Espada ZG, Hot Dog evita os andares e entra direto na sala final.")
        return

    divisor()
    narrar("Glozium melhorou a seguranca da torre com gargulas captchas.")
    narrar("Elas atacam Hot Dog durante a escalada.")
    print("\n1 - Par")
    print("2 - Impar")
    escolha = pedir_opcao("Escolha par ou impar: ", ["1", "2"])
    numero = random.randint(1, VIDA_GARGULAS_CAPTCHAS)
    resultado_par = numero % 2 == 0
    heroi_escolheu_par = escolha == "1"
    narrar(f"As gargulas sorteiam o numero {numero}.")

    if resultado_par == heroi_escolheu_par:
        narrar("As captchas sao quebradas pela aura do heroi.")
        return

    # Perder o desafio remove Salsichinha do grupo e ativa um evento em Glozium.
    narrar("As gargulas vencem o desafio e levam Salsichinha.")
    heroi.salsichinha_presente = False


def conversa_glozium():
    """Mostra ou pula o dialogo inicial da batalha final."""
    divisor()
    narrar("Hot Dog entra na sala do chefe e se depara com Glozium sentado no trono.")
    print("\n1 - Ouvir a conversa")
    print("2 - Pular conversa")
    opcao = pedir_opcao("Escolha: ", ["1", "2"])

    if opcao == "2":
        narrar("Hot Dog ergue a espada e se prepara para a batalha final.")
        return

    falar("Glozium", "Novamente um rato invadiu meu recinto; desta vez ira servir de alimento para meus escravos.")
    falar("Hot Dog", "Voce e como meu pai descreveu. Nao cansa de ser derrotado por geracoes?")
    falar("Glozium", "Ha ha ha ha! Que petulante.")
    falar("Glozium", "Chegou a epoca, mas mandaram outro pobre coitado; pessima ideia.")
    falar("Hot Dog", "Vou te destruir, Glozium, e garantir sua aniquilacao total e permanente.")
    narrar("Hot Dog lanca sua espada girando no ar, ferindo o monstro antes que ela retorne a sua mao.")
    falar("Hot Dog", "Nao subestime alguem com cabeca de cachorro quente.")
    falar("Glozium", "Interessante. Aceito seu pedido de batalha. Me derrote e voce podera ver sua mae.")


def criar_evento_salsichinha():
    """Cria o evento que ocorre em Glozium se Salsichinha foi capturado."""
    evento_ja_aconteceu = {"valor": False}

    def evento(heroi, monstro):
        """Dispara quando Glozium chega a 80 de vida ou menos."""
        if evento_ja_aconteceu["valor"]:
            return False
        if heroi.salsichinha_presente:
            return False
        if monstro.vida_atual > 80:
            return False

        evento_ja_aconteceu["valor"] = True
        divisor()
        falar("Glozium", "Venham ate mim, gargulas captchas, e tragam o presentinho.")
        falar("Glozium", "Melhor nao se mover, heroi. Desista de tudo, entregue a espada e seu companheiro vivera.")
        print("\n1 - Continuar a batalha")
        print("2 - Desistir e sair com Salsichinha")
        opcao = pedir_opcao("Escolha: ", ["1", "2"])

        if opcao == "2":
            # O jogador salva o mascote, mas abandona a missao.
            heroi.desistiu_para_salvar_salsichinha = True
            heroi.vida_atual = 0
            narrar("Glozium liberta heroi e mascote, que sobrevivem, mas desonrados.")
            narrar("Glozium destroi o mundo. Fim de jogo.")
            return True

        # Continuar sacrifica Salsichinha e fortalece Hot Dog para o restante da luta.
        narrar("Glozium mata Salsichinha diante dos olhos de Hot Dog.")
        narrar("Hot Dog entra em furia incontrolavel, revelando seu verdadeiro poder.")
        heroi.multiplicador_dano = 3
        heroi.vida_maxima += 50
        heroi.vida_atual += 50
        narrar("Poder de ataque aumentado em 3x. Vida aumentada em 50 pontos.")
        return False

    return evento


def final_vitoria(heroi):
    """Escolhe o final de vitoria conforme Espada ZG e destino de Salsichinha."""
    narrar("Hot Dog golpeia Glozium no peito. O monstro sorri em agonia.")
    falar("Glozium", "Voce conseguiu... vou cumprir minha promessa. Aqui esta sua mae.")
    narrar("O corpo de Glozium se desfigura, revelando ser a mae de Hot Dog possuida pelos poderes sombrios.")
    falar("Hot Dog", "Nao pode ser... mae? O que foi que eu fiz?")
    narrar("Hot Dog segura a mae nos bracos com a espada ainda em seu peito.")
    falar("Mae", "Voce apenas cumpriu seu dever, filho...")

    if heroi.tem_espada_zg:
        narrar("A Espada ZG manifesta seu poder milagroso acumulado durante todo o ciclo hospitales.")
        narrar("Esse poder se funde a mae de Hot Dog, curando-a por completo.")
        narrar("O heroi derrotou Glozium e a paz retornou ao mundo.")
        narrar("Final A: Hot Dog vive feliz com sua familia. Muito obrigado, heroi!")
        return

    if heroi.salsichinha_presente:
        narrar("Sem a Espada ZG, a mae de Hot Dog nao pode ser salva.")
        narrar("Salsichinha observa em silencio enquanto o heroi se despede dela.")
        narrar("Hot Dog se joga da torre. Glozium foi detido por mais um ano.")
        narrar("Final C: Glozium foi derrotado, mas o custo ainda foi terrivel.")
        return

    narrar("Sem a Espada ZG, a mae de Hot Dog falece.")
    narrar("O silencio preenche a sala. Glozium foi detido por mais um ano, mas a que custo?")
    narrar("Com a mae e Salsichinha perdidos, Hot Dog caminha ate a janela e se joga da torre.")
    narrar("Final B: Glozium foi derrotado ao custo mais alto possivel.")


def ato_final(heroi):
    """Executa preparacao, dialogo e batalha final contra Glozium."""
    perguntar_forja_espada(heroi)
    desafio_gargulas(heroi)
    conversa_glozium()

    glozium = Personagem("Glozium", vida_maxima=VIDA_GLOZIUM, quantidade_dados=DADOS_GLOZIUM)
    heroi.desistiu_para_salvar_salsichinha = False
    resultado = iniciar_batalha(
        heroi,
        glozium,
        aumenta_vida_apos_vitoria=False,
        evento_durante_batalha=criar_evento_salsichinha(),
    )

    if getattr(heroi, "desistiu_para_salvar_salsichinha", False):
        return

    if resultado == "vitoria":
        final_vitoria(heroi)
        return

    if resultado == "desistiu":
        finalizar_por_desistencia()
        return

    falar("Glozium", "Finalmente! Um heroi que apenas aumentou meus poderes.")
    narrar("O mundo foi destruido por Glozium, uma fatalidade terrivel. Fim de jogo!")

import random

from configuracoes import BONUS_VIDA_APOS_VITORIA
from interface import divisor, mensagem_batalha, narrar, pedir_opcao
from itens import (
    AZAH_TRANSMISSAO,
    BOMBA_MAGICA,
    COLAR_ESTATUA_SAGRADA,
    ESPADA_ZG,
    FATURAMENTUS,
    GUIA_ATENDIMENTO,
    eh_espada,
    eh_item_comum,
)


def sortear_numeros(quantidade, valor_maximo):
    """Sorteia os numeros usados no ataque de um turno."""
    return [random.randint(1, valor_maximo) for _ in range(quantidade)]


def calcular_dano(numeros_sorteados, numero_secreto_alvo):
    """Calcula dano pela frequencia do numero secreto nos numeros sorteados."""
    frequencia = numeros_sorteados.count(numero_secreto_alvo)
    return numero_secreto_alvo * frequencia


def mostrar_status_batalha(heroi, monstro):
    """Mostra vida, estado especial do Worm e item atualmente equipado."""
    print(f"Vida do heroi: {heroi.vida_atual}/{heroi.vida_maxima}")
    print(f"Vida do monstro: {monstro.vida_atual}/{monstro.vida_maxima}")

    if getattr(monstro, "eh_worm", False):
        estado = "fora da terra" if monstro.desenterrado else "enterrado"
        print(f"Estado do Worm: {estado}")

    print(f"Espada equipada: {heroi.espada_equipada}")
    if heroi.item_equipado:
        print(f"Item equipado: {heroi.item_equipado}")
    else:
        print("Item equipado: nenhum")


def descricao_equipado(heroi, item):
    """Retorna marcador visual do item equipado no inventario."""
    if item == heroi.espada_equipada or item == heroi.item_equipado:
        return " (equipado)"
    return ""


def mostrar_menu_itens(heroi):
    """Permite equipar ou desequipar itens sem consumir o turno do heroi."""
    while True:
        divisor()
        print("ITENS DO HEROI")
        for indice, item in enumerate(heroi.itens, start=1):
            marcador = descricao_equipado(heroi, item)
            print(f"{indice} - {item}{marcador}")
        print("0 - Voltar para as acoes")

        opcoes_validas = ["0"] + [str(numero) for numero in range(1, len(heroi.itens) + 1)]
        opcao = pedir_opcao("Escolha um item para equipar/desequipar: ", opcoes_validas)

        if opcao == "0":
            return

        item_escolhido = heroi.itens[int(opcao) - 1]

        if eh_espada(item_escolhido):
            if heroi.espada_equipada == item_escolhido:
                mensagem_batalha(f"{item_escolhido} ja esta equipada.")
                continue

            heroi.espada_equipada = item_escolhido
            if item_escolhido == ESPADA_ZG:
                heroi.item_equipado = None
                mensagem_batalha("Espada ZG equipada. Nenhum outro item pode ficar equipado junto dela.")
            else:
                mensagem_batalha(f"{item_escolhido} foi equipada.")
            continue

        if eh_item_comum(item_escolhido):
            if heroi.espada_equipada == ESPADA_ZG:
                mensagem_batalha("A Espada ZG nao pode ser usada junto com outro item.")
                continue

            if heroi.item_equipado == item_escolhido:
                heroi.item_equipado = None
                mensagem_batalha(f"{item_escolhido} foi desequipado.")
            else:
                heroi.item_equipado = item_escolhido
                mensagem_batalha(f"{item_escolhido} foi equipado.")
            continue

        if heroi.item_equipado == item_escolhido:
            heroi.item_equipado = None
            mensagem_batalha(f"{item_escolhido} foi desequipado.")
        else:
            heroi.item_equipado = item_escolhido
            mensagem_batalha(f"{item_escolhido} foi equipado.")


def escolher_acao_heroi(heroi, monstro):
    """Monta o menu de acoes conforme itens e estado atual do heroi."""
    while True:
        print("\n1 - Atacar")
        print("2 - Itens")

        proxima_opcao = 3
        opcao_bomba = None
        opcao_salsichinha = None
        opcao_desistir = None

        if heroi.item_equipado == BOMBA_MAGICA:
            # A opcao de bomba so aparece quando ela esta equipada.
            opcao_bomba = str(proxima_opcao)
            print(f"{opcao_bomba} - Usar Bomba Magica")
            proxima_opcao += 1

        if heroi.salsichinha_presente:
            # Se Salsichinha foi levado por Glozium, o ataque combinado some.
            opcao_salsichinha = str(proxima_opcao)
            print(f"{opcao_salsichinha} - Ataque combinado com Salsichinha")
            proxima_opcao += 1

        opcao_desistir = str(proxima_opcao)
        print(f"{opcao_desistir} - Desistir da missao")

        opcoes_validas = [str(numero) for numero in range(1, proxima_opcao + 1)]
        opcao = pedir_opcao("Escolha uma acao: ", opcoes_validas)

        if opcao == "2":
            # Abrir o inventario nao passa o turno.
            mostrar_menu_itens(heroi)
            divisor()
            print(f"Turno de {heroi.nome}")
            mostrar_status_batalha(heroi, monstro)
            continue

        if opcao == "1":
            return "atacar"
        if opcao == opcao_bomba:
            return "bomba"
        if opcao == opcao_salsichinha:
            return "salsichinha"
        if opcao == opcao_desistir:
            return "desistir"


def quantidade_dados_heroi(heroi):
    """Define quantos numeros o heroi sorteia com base no item equipado."""
    if heroi.espada_equipada == ESPADA_ZG:
        return 40
    if heroi.item_equipado == GUIA_ATENDIMENTO:
        return 2
    if heroi.item_equipado == FATURAMENTUS:
        return 4
    if heroi.item_equipado == AZAH_TRANSMISSAO:
        return 10
    if heroi.item_equipado == COLAR_ESTATUA_SAGRADA:
        return 10
    return heroi.quantidade_dados


def aplicar_consequencias_item(heroi, acertou, numeros_sorteados):
    """Aplica penalidades dos itens quando o ataque do heroi falha."""
    if acertou:
        return

    if heroi.item_equipado == FATURAMENTUS:
        heroi.penalidade_faturamentus += 2
        heroi.erros_faturamentus += 1
        mensagem_batalha(
            "Faturamentus falhou. O dano extra acumulado para proximos acertos do monstro "
            f"agora e {heroi.penalidade_faturamentus}."
        )

        if heroi.erros_faturamentus >= 3:
            heroi.vida_atual -= 2
            mensagem_batalha("Faturamentus ja falhou 3 vezes nesta batalha. Hot Dog perde 2 de vida.")

    if heroi.item_equipado == AZAH_TRANSMISSAO and numeros_sorteados:
        heroi.penalidade_azah += numeros_sorteados[-1]
        mensagem_batalha(
            "Azah Transmissao falhou. O dano extra acumulado para proximos acertos do monstro "
            f"agora e {heroi.penalidade_azah}."
        )


def atacar_monstro(heroi, monstro, ataque_com_salsichinha=False):
    """Executa o ataque do heroi contra o monstro atual."""
    heroi.ultimo_item_usado = None if ataque_com_salsichinha else heroi.item_equipado

    if getattr(monstro, "eh_worm", False) and not monstro.desenterrado:
        # Worm so pode receber dano depois de ser retirado da terra.
        mensagem_batalha("Worm esta debaixo da terra. Primeiro use a Bomba Magica para desenterra-lo.")
        return False

    quantidade_dados = quantidade_dados_heroi(heroi)
    bonus_dano = 1 if ataque_com_salsichinha else 0

    if heroi.item_equipado == COLAR_ESTATUA_SAGRADA:
        heroi.vida_atual -= 3
        mensagem_batalha("O Colar da Estatua Sagrada consome 3 de vida de Hot Dog.")
        if not heroi.esta_vivo():
            return True

    if ataque_com_salsichinha:
        mensagem_batalha("Salsichinha avanca junto com Hot Dog no ataque combinado!")

    numeros_sorteados = sortear_numeros(quantidade_dados, monstro.vida_maxima)
    dano = calcular_dano(numeros_sorteados, monstro.numero_secreto)
    acertou = dano > 0

    mensagem_batalha(f"Numeros sorteados: {numeros_sorteados}")

    if acertou:
        dano = (dano + bonus_dano) * heroi.multiplicador_dano
        monstro.vida_atual -= dano
        mensagem_batalha(f"Acerto! {monstro.nome} perdeu {dano} de vida.")
    else:
        mensagem_batalha("O ataque nao encontrou o numero secreto do monstro.")

    aplicar_consequencias_item(heroi, acertou, numeros_sorteados)
    return True


def usar_bomba(heroi, monstro):
    """Aplica a regra da Bomba Magica contra Worm ou contra monstros comuns."""
    heroi.ultimo_item_usado = "Bomba Magica"

    quantidade_tentativas = max(1, int(monstro.vida_maxima * 0.8))

    if getattr(monstro, "eh_worm", False) and not monstro.desenterrado:
        # Contra Worm enterrado, a bomba tenta acertar sua posicao dinamica.
        numeros_sorteados = sortear_numeros(quantidade_tentativas, monstro.vida_maxima)
        acertou = monstro.posicao_atual in numeros_sorteados
        mensagem_batalha(f"Numeros sorteados pela bomba: {numeros_sorteados}")
        mensagem_batalha(f"Posicao atual do Worm: {monstro.posicao_atual}.")

        if acertou:
            monstro.desenterrado = True
            mensagem_batalha("A bomba explode no ponto certo. Worm saiu da terra!")
        else:
            registrar_erro_bomba(heroi)
            mensagem_batalha("A bomba errou a posicao. Worm continua enterrado.")
        return

    numeros_sorteados = sortear_numeros(quantidade_tentativas, monstro.vida_maxima)
    acertou = monstro.numero_secreto in numeros_sorteados
    mensagem_batalha(f"Numeros sorteados pela bomba: {numeros_sorteados}")

    if acertou:
        monstro.atordoado = True
        mensagem_batalha(f"A Bomba Magica atordoa {monstro.nome}. Ele perdera o proximo turno.")
        return

    registrar_erro_bomba(heroi)
    mensagem_batalha("A Bomba Magica errou o alvo.")


def registrar_erro_bomba(heroi):
    """Acumula erros da bomba e aplica dano a partir da terceira falha."""
    heroi.erros_bomba += 1
    if heroi.erros_bomba >= 3:
        heroi.vida_atual -= 2
        mensagem_batalha("A Bomba Magica ja falhou 3 vezes nesta batalha. Hot Dog perde 2 de vida.")


def atualizar_posicao_worm(monstro):
    """Move o Worm para outra posicao enquanto ele ainda estiver enterrado."""
    if getattr(monstro, "eh_worm", False) and not monstro.desenterrado:
        monstro.posicao_atual = random.randint(1, monstro.vida_maxima)
        mensagem_batalha(f"Worm se move por baixo da terra para uma nova posicao entre 1 e {monstro.vida_maxima}.")


def turno_heroi(heroi, monstro):
    """Controla uma rodada completa de decisao do heroi."""
    divisor()
    print(f"Turno de {heroi.nome}")
    mostrar_status_batalha(heroi, monstro)

    acao = escolher_acao_heroi(heroi, monstro)

    if acao == "desistir":
        return "desistiu"

    if acao == "bomba":
        usar_bomba(heroi, monstro)
        return "continuar"

    if acao == "salsichinha":
        atacar_monstro(heroi, monstro, ataque_com_salsichinha=True)
        return "continuar"

    atacar_monstro(heroi, monstro)
    return "continuar"


def turno_monstro(heroi, monstro):
    """Controla o ataque do monstro e efeitos especiais do turno inimigo."""
    if not monstro.esta_vivo():
        return

    if getattr(monstro, "atordoado", False):
        # A bomba faz o monstro perder exatamente um turno.
        monstro.atordoado = False
        mensagem_batalha(f"{monstro.nome} esta atordoado e perdeu o turno.")
        atualizar_posicao_worm(monstro)
        return

    divisor()
    mensagem_batalha(f"Turno de {monstro.nome}")

    quantidade_dados = monstro.quantidade_dados
    bonus_dano = 0

    if getattr(monstro, "copia_item", False) and heroi.ultimo_item_usado:
        # Sandubinha Reverse copia o ultimo item usado pelo heroi.
        mensagem_batalha(f"{monstro.nome} copia o ultimo item usado: {heroi.ultimo_item_usado}.")

        if heroi.ultimo_item_usado == GUIA_ATENDIMENTO:
            quantidade_dados = 2
        elif heroi.ultimo_item_usado == FATURAMENTUS:
            quantidade_dados = 4
            bonus_dano = 2
        elif heroi.ultimo_item_usado == AZAH_TRANSMISSAO:
            quantidade_dados = 10
        elif heroi.ultimo_item_usado == COLAR_ESTATUA_SAGRADA:
            quantidade_dados = 10
        elif heroi.ultimo_item_usado == BOMBA_MAGICA:
            mensagem_batalha("A copia da Bomba Magica falha contra Hot Dog, mas atrapalha sua defesa.")
            bonus_dano = 2

    numeros_sorteados = sortear_numeros(quantidade_dados, heroi.vida_maxima)
    dano = calcular_dano(numeros_sorteados, heroi.numero_secreto)

    mensagem_batalha(f"Numeros sorteados pelo monstro: {numeros_sorteados}")

    if dano > 0:
        dano += bonus_dano
        dano += heroi.penalidade_faturamentus
        dano += heroi.penalidade_azah
        heroi.penalidade_faturamentus = 0
        heroi.penalidade_azah = 0
        heroi.vida_atual -= dano
        mensagem_batalha(f"{monstro.nome} acertou o numero secreto! Hot Dog perdeu {dano} de vida.")
    else:
        mensagem_batalha(f"{monstro.nome} errou o ataque.")

    atualizar_posicao_worm(monstro)


def iniciar_batalha(heroi, monstro, aumenta_vida_apos_vitoria=True, evento_durante_batalha=None):
    """Executa o loop principal de batalha ate vitoria, derrota ou desistencia."""
    heroi.sortear_numero_secreto()
    heroi.reiniciar_consequencias_batalha()
    monstro.reiniciar_para_batalha()
    if getattr(monstro, "eh_worm", False):
        # Worm comeca enterrado e recebe uma posicao dinamica inicial.
        monstro.desenterrado = False
        monstro.posicao_atual = random.randint(1, monstro.vida_maxima)

    monstro.atordoado = False

    divisor()
    narrar(f"Batalha iniciada: {heroi.nome} vs {monstro.nome}")
    narrar("Numeros secretos foram sorteados e ficarao fixos ate o fim da luta.")

    while heroi.esta_vivo() and monstro.esta_vivo():
        resultado = turno_heroi(heroi, monstro)

        if resultado == "desistiu":
            heroi.reiniciar_consequencias_batalha()
            return "desistiu"

        if not monstro.esta_vivo():
            break

        if evento_durante_batalha and evento_durante_batalha(heroi, monstro):
            # Eventos especiais podem encerrar a luta, como desistir para salvar Salsichinha.
            if not heroi.esta_vivo():
                heroi.reiniciar_consequencias_batalha()
                return "desistiu"

        turno_monstro(heroi, monstro)

    if heroi.esta_vivo():
        if aumenta_vida_apos_vitoria:
            heroi.vida_maxima += BONUS_VIDA_APOS_VITORIA
            heroi.vida_atual = heroi.vida_maxima
            narrar(f"{heroi.nome} venceu a batalha!")
            narrar(f"Vida maxima aumentada em {BONUS_VIDA_APOS_VITORIA}. Nova vida maxima: {heroi.vida_maxima}.")
        heroi.reiniciar_consequencias_batalha()
        return "vitoria"

    heroi.reiniciar_consequencias_batalha()
    return "derrota"

"""Definicoes e regras auxiliares dos itens do jogo."""

ESPADA_SIMPLES = "Espada simples"
ESPADA_ZG = "Espada ZG"
GUIA_ATENDIMENTO = "Guia de Atendimento"
FATURAMENTUS = "Faturamentus"
BOMBA_MAGICA = "Bomba Magica"
AZAH_TRANSMISSAO = "Azah Transmissao"
COLAR_ESTATUA_SAGRADA = "Colar da Estatua Sagrada"

ITENS_DA_FORJA = [
    GUIA_ATENDIMENTO,
    FATURAMENTUS,
    BOMBA_MAGICA,
    AZAH_TRANSMISSAO,
    COLAR_ESTATUA_SAGRADA,
]

ESPADAS = [ESPADA_SIMPLES, ESPADA_ZG]
ITENS_EQUIPAVEIS = [
    GUIA_ATENDIMENTO,
    FATURAMENTUS,
    BOMBA_MAGICA,
    AZAH_TRANSMISSAO,
    COLAR_ESTATUA_SAGRADA,
]


def eh_espada(item):
    """Indica se o item ocupa o espaco de espada equipada."""
    return item in ESPADAS


def eh_item_comum(item):
    """Indica se o item pode ser equipado junto com a espada simples."""
    return item in ITENS_EQUIPAVEIS

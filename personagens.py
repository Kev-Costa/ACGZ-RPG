import random

from itens import ESPADA_SIMPLES


class Personagem:
    """Representa qualquer participante de batalha: heroi ou monstro."""

    def __init__(self, nome, vida_maxima, quantidade_dados=1):
        # Dados basicos de batalha.
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.quantidade_dados = quantidade_dados
        self.numero_secreto = 1

        # Estado usado principalmente pelo heroi ao longo da jornada.
        self.itens = [ESPADA_SIMPLES]
        self.espada_equipada = ESPADA_SIMPLES
        self.item_equipado = None
        self.salsichinha_presente = True
        self.tem_espada_zg = False
        self.multiplicador_dano = 1

        # Penalidades temporarias causadas por itens durante uma batalha.
        self.penalidade_azah = 0
        self.penalidade_faturamentus = 0
        self.erros_faturamentus = 0
        self.erros_bomba = 0
        self.ultimo_item_usado = None

    def reiniciar_para_batalha(self):
        """Restaura dados temporarios usados no inicio de cada batalha."""
        self.vida_atual = self.vida_maxima
        self.sortear_numero_secreto()
        self.reiniciar_consequencias_batalha()

    def reiniciar_consequencias_batalha(self):
        """Limpa consequencias acumuladas que so valem dentro da batalha atual."""
        self.penalidade_azah = 0
        self.penalidade_faturamentus = 0
        self.erros_faturamentus = 0
        self.erros_bomba = 0
        self.ultimo_item_usado = None

    def sortear_numero_secreto(self):
        """Sorteia o numero secreto fixo que vale ate o fim da batalha."""
        self.numero_secreto = random.randint(1, self.vida_maxima)

    def esta_vivo(self):
        """Retorna True enquanto a vida atual for maior que zero."""
        return self.vida_atual > 0

    def adicionar_item(self, item):
        """Adiciona um item ao inventario, evitando duplicatas."""
        if item not in self.itens:
            self.itens.append(item)

    def possui_item(self, item):
        """Verifica se o personagem possui determinado item."""
        return item in self.itens

    def remover_item(self, item):
        """Remove um item do inventario, caso ele exista."""
        if item in self.itens:
            self.itens.remove(item)

        if self.item_equipado == item:
            self.item_equipado = None

        if self.espada_equipada == item:
            self.espada_equipada = ESPADA_SIMPLES

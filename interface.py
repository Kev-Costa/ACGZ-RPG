import time

from configuracoes import PAUSA_BATALHA, PAUSA_DIALOGO, PAUSA_NARRACAO


def narrar(texto, pausa=PAUSA_NARRACAO):
    """Exibe textos de narracao com uma pausa para facilitar a leitura."""
    print(texto)
    time.sleep(pausa)


def falar(personagem, texto):
    """Exibe falas no formato 'Personagem: fala'."""
    print(f"{personagem}: {texto}")
    time.sleep(PAUSA_DIALOGO)


def mensagem_batalha(texto):
    """Exibe mensagens curtas de batalha com pausa menor."""
    print(texto)
    time.sleep(PAUSA_BATALHA)


def divisor():
    """Separa visualmente menus, atos e turnos no terminal."""
    print("\n" + "=" * 60)


def pedir_opcao(mensagem, opcoes_validas):
    """Repete a pergunta ate o usuario digitar uma opcao permitida."""
    opcoes_validas = [opcao.lower() for opcao in opcoes_validas]

    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in opcoes_validas:
            return resposta
        print("Opcao invalida. Tente novamente.")

from configuracoes import VIDA_INICIAL_HEROI
from historia import ato_dois, ato_final, ato_quatro, ato_tres, ato_um
from interface import divisor, narrar, pedir_opcao
from personagens import Personagem


def jogar():
    """Cria uma nova partida e executa os atos na ordem da historia."""
    heroi = Personagem("Hot Dog", vida_maxima=VIDA_INICIAL_HEROI, quantidade_dados=1)

    narrar("Desafio da historia epica de Sir Hot Dog")
    narrar("Seu objetivo e atravessar a jornada, reunir os artefatos e enfrentar Glozium.")

    # Cada ato retorna True quando o jogador pode avancar.
    # Se retornar False, a partida terminou por derrota ou desistencia.
    if not ato_um(heroi):
        return

    if not ato_dois(heroi):
        return

    if not ato_tres(heroi):
        return

    if not ato_quatro(heroi):
        return

    ato_final(heroi)

    divisor()
    narrar("Fim da jornada de Hot Dog.")


def main():
    """Mostra o menu principal e permite iniciar novas partidas."""
    while True:
        divisor()
        print("1 - Novo jogo")
        print("2 - Sair")
        opcao = pedir_opcao("Escolha uma opcao: ", ["1", "2"])

        if opcao == "2":
            print("Ate a proxima!")
            break

        jogar()

        jogar_novamente = pedir_opcao("\nDeseja jogar novamente? (s/n): ", ["s", "n"])
        if jogar_novamente == "n":
            print("Ate a proxima!")
            break


if __name__ == "__main__":
    main()

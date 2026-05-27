# ACZG-RPG 2 - Jornada de Sir Hot Dog

Projeto desenvolvido em Python para o desafio **ACZG-RPG 2**, com foco em logica de programacao, interpretacao de requisitos, controle de fluxo, estruturas condicionais, repeticao, funcoes, organizacao de codigo e interacao via terminal.

O jogo adapta a aventura de Sir Hot Dog em uma experiencia textual interativa. O jogador avanca por atos da historia, enfrenta monstros, coleta itens obrigatorios e toma decisoes que podem alterar o final da jornada.

## Objetivo do Projeto

O objetivo e implementar uma historia interativa em terminal, respeitando os requisitos principais do enunciado:

- interacao com o usuario;
- falas exibidas uma por vez;
- possibilidade de desistir da missao;
- possibilidade de jogar novamente;
- mecanica de batalha por turnos;
- uso de numeros aleatorios;
- numero secreto fixo durante cada batalha;
- vida atual e vida maxima;
- evolucao do personagem;
- itens que modificam a dinamica da batalha;
- finais diferentes conforme as decisoes tomadas.

## Como Executar

E necessario ter Python instalado.

```bash
python main.py
```

## Estrutura do Projeto

```text
main.py            Menu principal e fluxo geral da partida
historia.py        Atos, narrativa, enigma, eventos e finais
combate.py         Turnos, ataques, itens, dano e regras de batalha
personagens.py     Classe Personagem e estado do heroi/monstros
itens.py           Nomes e listas dos itens usados pelo jogo
interface.py       Funcoes auxiliares de texto, pausa, menus e entrada
configuracoes.py   Valores fixos de vida, dados e tempo de exibicao
```

## Atos Implementados

1. **Floresta do Atendimentus**
   - Introduz a jornada.
   - Batalha contra Anti-authorizatus.
   - Recompensa: Guia de Atendimento.

2. **Cavernas de Faturamentus**
   - Possui enigma com consequencias.
   - Batalha contra Glozium Administratus.
   - Recompensa: Faturamentus.

3. **Vila da Transmissao**
   - Introduz a Bomba Magica.
   - Batalha contra Worm, que fica enterrado e precisa ser desenterrado.
   - Recompensa: Azah Transmissao.

4. **Torre de Contas a Receber**
   - Batalha contra Sandubinha Reverse.
   - O monstro copia o ultimo item usado pelo heroi, exceto ataque do Salsichinha.
   - Recompensa: Colar da Estatua Sagrada

5. **Batalha Final**
   - Preparacao para enfrentar Glozium.
   - Possibilidade de forjar a Espada ZG.
   - Desafio das gargulas captchas caso o heroi enfrente Glozium sem a Espada ZG.
   - Dialogo inicial com Glozium pode ser ouvido ou pulado.
   - Finais alternativos conforme escolhas e resultado da batalha.

## Mecanica de Batalha

Cada personagem possui:

- vida maxima;
- vida atual;
- quantidade de numeros sorteados por turno;
- numero secreto.

No inicio de cada batalha, o numero secreto do heroi e o numero secreto do monstro sao sorteados. Eles permanecem fixos ate o fim da luta.

Em cada turno, o atacante sorteia uma quantidade de numeros. Se o numero secreto do alvo aparecer entre os numeros sorteados, ocorre dano.

Formula usada:

```text
dano = numero_secreto_do_alvo * quantidade_de_aparicoes
```

Exemplo:

```text
numero secreto do alvo = 7
numeros sorteados = [3, 7, 1, 7]
dano = 7 * 2 = 14
```

## Itens

O jogo implementa apenas os itens necessarios para a historia principal e para a forja da Espada ZG.

### Espada simples

Item inicial do heroi.

### Guia de Atendimento

Permite sortear 2 numeros no ataque.

### Faturamentus

Permite sortear 4 numeros no ataque.

Se errar, acumula +2 de dano para proximos acertos do monstro. Apos 3 falhas na mesma batalha, o heroi tambem perde 2 de vida ao usar o item.

### Bomba Magica

Obrigatoria contra Worm.

- Contra Worm enterrado: sorteia 80% da vida maxima do monstro em tentativas para acertar a posicao dinamica dele.
- Contra Worm fora da terra: atordoa o monstro.
- Contra outros monstros: tambem atordoa e faz o inimigo perder o proximo turno.
- A partir da terceira falha na mesma batalha, causa 2 de dano ao heroi quando usada.

### Azah Transmissao

Permite sortear 10 numeros no ataque.

Se errar, acumula dano extra baseado no ultimo numero sorteado para proximos acertos do monstro.

### Colar da Estatua Sagrada

Obtido apos derrotar Sandubinha Reverse.

Permite sortear 10 numeros no ataque.

Consequencia: sempre que for usado, subtrai 3 de vida do heroi.

### Espada ZG

Pode ser forjada antes da batalha final se o heroi tiver todos os itens obrigatorios das fases.

Ela altera o caminho ate Glozium e permite o melhor final.

Ao ser forjada em Hospitalis, todos os itens usados no processo saem do inventario, incluindo a espada inicial. Na batalha final, o heroi fica apenas com a Espada ZG.

A Espada ZG permite sortear 40 numeros por ataque e nao possui consequencia de uso.

## Finais Alternativos

O jogo possui diferentes finais:

- **Final A**: Hot Dog vence Glozium com a Espada ZG.
- **Final B**: Hot Dog vence sem a Espada ZG e Salsichinha morre.
- **Final C**: Hot Dog vence sem a Espada ZG, mas Salsichinha sobrevive.
- **Final D**: o heroi salva o mascote, mas Glozium destroi o mundo.
- **Derrota final**: Glozium vence e destroi o mundo.
- **Desistencia da missao**: o jogador abandona a jornada.

## Valores dos Monstros

Os valores fixos ficam em `configuracoes.py` para facilitar leitura, balanceamento e testes.

```text
Anti-authorizatus       vida 4   | dados 1
Glozium Administratus   vida 6   | dados 2
Worm                    vida 12  | dados 3
Sandubinha Reverse      vida 30  | dados 8
Gargulas captchas       vida 10  | dados 0
Glozium                 vida 100 | dados 10
```

## Observacoes de Implementacao

- O projeto foi separado por responsabilidade para facilitar leitura e manutencao.
- O menu de itens nao consome turno.
- A espada equipada e o item equipado sao estados separados.
- A Espada simples pode ser usada junto com um item.
- A Espada ZG e exclusiva e nao pode ser usada junto com outro item.
- O item equipado permanece salvo entre atos e batalhas, exceto se for consumido na forja.
- A Bomba Magica possui comportamento especial contra Worm.
- As consequencias acumuladas dos itens sao resetadas ao final de cada batalha.
- A escolha de forjar ou nao a Espada ZG influencia diretamente os eventos finais.
- O codigo utiliza apenas recursos padrao do Python, sem bibliotecas externas.

## Possiveis Ajustes Para Testes

Durante apresentacoes ou testes, os valores de `configuracoes.py` podem ser reduzidos temporariamente para acelerar as batalhas.

Tambem e possivel reduzir as pausas:

```python
PAUSA_NARRACAO = 0.1
PAUSA_DIALOGO = 0.1
PAUSA_BATALHA = 0.1
```

Esses ajustes sao uteis apenas para demonstracao e nao fazem parte das regras principais do jogo.

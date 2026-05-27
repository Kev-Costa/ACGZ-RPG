# Documentacao Para Apresentacao - ACZG-RPG 2

Este documento serve como guia para explicar o projeto durante a apresentacao tecnica.

## 1. Ideia Geral Do Projeto

O projeto e um RPG textual em Python executado no terminal. O jogador controla Hot Dog, passa por atos da historia, enfrenta monstros, coleta itens obrigatorios e toma decisoes que mudam o final.

O foco principal nao e grafico, mas sim demonstrar logica de programacao:

- menus e interacao com usuario;
- estruturas condicionais;
- repeticoes;
- funcoes;
- classes;
- listas;
- numeros aleatorios;
- controle de estado do personagem;
- separacao do codigo por responsabilidade.

## 2. Como Executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

O arquivo `main.py` e o ponto de entrada do programa.

## 3. Estrutura Dos Arquivos

### main.py

Controla o inicio do jogo.

Principais responsabilidades:

- mostrar menu inicial;
- criar o heroi;
- chamar os atos na ordem correta;
- perguntar se o jogador quer jogar novamente.

Funcoes importantes:

- `jogar()`: cria uma nova partida e executa os atos.
- `main()`: mostra o menu principal em loop.

### configuracoes.py

Guarda valores fixos do jogo.

Exemplos:

- vida inicial do heroi;
- vida dos monstros;
- quantidade de dados dos monstros;
- tempo de pausa dos textos.

Isso facilita testes e balanceamento sem mexer na logica principal.

### personagens.py

Contem a classe `Personagem`.

Essa classe representa tanto o heroi quanto os monstros.

Principais atributos:

- `nome`: nome do personagem;
- `vida_maxima`: vida total;
- `vida_atual`: vida durante a batalha;
- `quantidade_dados`: quantos numeros sorteia por turno;
- `numero_secreto`: numero fixo sorteado no inicio da batalha;
- `itens`: inventario;
- `espada_equipada`: espada atual;
- `item_equipado`: item comum atual;
- `salsichinha_presente`: controla se o ataque combinado esta disponivel.

Principais metodos:

- `sortear_numero_secreto()`: sorteia o numero secreto da batalha.
- `esta_vivo()`: verifica se a vida e maior que zero.
- `adicionar_item()`: adiciona item ao inventario.
- `remover_item()`: remove item do inventario.
- `reiniciar_consequencias_batalha()`: limpa efeitos temporarios apos cada batalha.

### itens.py

Centraliza os nomes dos itens.

Isso evita escrever strings repetidas em varios lugares, como:

```python
"Guia de Atendimento"
"Bomba Magica"
"Espada ZG"
```

Tambem separa:

- espadas;
- itens comuns;
- itens usados na forja.

### interface.py

Cuida da exibicao e entrada de dados.

Funcoes principais:

- `narrar()`: mostra textos narrativos com pausa.
- `falar()`: mostra falas de personagens.
- `mensagem_batalha()`: mostra mensagens curtas de batalha.
- `divisor()`: separa visualmente partes do terminal.
- `pedir_opcao()`: garante que o usuario escolha uma opcao valida.

### combate.py

E o arquivo mais importante da logica de batalha.

Responsabilidades:

- controlar turnos;
- sortear numeros;
- calcular dano;
- aplicar efeitos de itens;
- controlar Worm;
- controlar atordoamento;
- controlar consequencias acumuladas dentro da batalha.

Funcoes principais:

- `sortear_numeros()`: gera numeros aleatorios.
- `calcular_dano()`: calcula dano usando frequencia do numero secreto.
- `mostrar_menu_itens()`: permite equipar itens sem consumir turno.
- `quantidade_dados_heroi()`: define quantos numeros o heroi sorteia.
- `atacar_monstro()`: executa ataque do heroi.
- `usar_bomba()`: aplica regra da bomba.
- `turno_heroi()`: controla a decisao do jogador.
- `turno_monstro()`: controla ataque inimigo.
- `iniciar_batalha()`: loop principal da batalha.

### historia.py

Controla a narrativa e as escolhas de historia.

Responsabilidades:

- executar os atos;
- criar monstros de cada fase;
- entregar itens;
- controlar enigma;
- controlar forja da Espada ZG;
- controlar gargulas;
- controlar dialogo de Glozium;
- controlar finais alternativos.

Funcoes principais:

- `ato_um()`
- `ato_dois()`
- `ato_tres()`
- `ato_quatro()`
- `ato_final()`
- `perguntar_forja_espada()`
- `desafio_gargulas()`
- `criar_evento_salsichinha()`
- `final_vitoria()`

## 4. Mecanica De Batalha

No inicio de cada batalha:

1. O heroi sorteia um numero secreto.
2. O monstro sorteia outro numero secreto.
3. Esses numeros ficam fixos ate o fim da batalha.

Durante o ataque, o atacante sorteia numeros.

Se o numero secreto do alvo aparecer, ocorre dano.

Formula:

```text
dano = numero_secreto * quantidade_de_aparicoes
```

Exemplo:

```text
numero secreto = 7
numeros sorteados = [3, 7, 1, 7]
dano = 7 * 2 = 14
```

## 5. Itens E Efeitos

### Espada simples

Item inicial.

### Guia de Atendimento

Faz o heroi sortear 2 numeros.

### Faturamentus

Faz o heroi sortear 4 numeros.

Se errar, acumula penalidade de dano para o proximo acerto do monstro.

### Bomba Magica

Serve para atordoar monstros.

Contra Worm, e obrigatoria para tira-lo da terra.

A bomba sorteia tentativas equivalentes a 80% da vida maxima do monstro.

### Azah Transmissao

Faz o heroi sortear 10 numeros.

Se errar, acumula penalidade com base no ultimo numero sorteado.

### Colar da Estatua Sagrada

Faz o heroi sortear 10 numeros.

Consequencia: perde 3 de vida sempre que usado.

### Espada ZG

E criada na forja.

Quando forjada:

- todos os itens somem do inventario;
- a espada simples tambem e consumida;
- o heroi fica apenas com a Espada ZG.

Efeito:

- sorteia 40 numeros;
- nao tem consequencia negativa;
- permite o melhor final.

## 6. Worm

Worm tem uma regra especial.

Ele comeca enterrado e nao pode receber dano.

Para atacar Worm:

1. Equipar a Bomba Magica.
2. Usar a bomba.
3. Se a bomba acertar a posicao dinamica, Worm sai da terra.
4. Depois disso, pode ser atacado normalmente.

Enquanto esta enterrado, sua posicao muda a cada rodada.

## 7. Batalha Final

Antes de Glozium:

1. O jogador pode forjar a Espada ZG se tiver todos os itens.
2. Se forjar, pula as gargulas.
3. Se nao forjar, enfrenta o desafio de par ou impar das gargulas.
4. Se perder para as gargulas, Salsichinha e capturado.
5. O jogador pode pular ou ouvir o dialogo inicial de Glozium.

Durante Glozium:

- se Salsichinha foi capturado, quando Glozium chega a 80 ou menos de vida, ocorre uma escolha;
- o jogador pode continuar ou desistir para salvar Salsichinha;
- se continuar, Salsichinha morre e Hot Dog fica mais forte.

## 8. Finais

### Final A

Vence Glozium com Espada ZG.

E o melhor final.

### Final B

Vence Glozium sem Espada ZG e com Salsichinha morto.

### Final C

Vence Glozium sem Espada ZG, mas com Salsichinha vivo.

### Final de derrota

Glozium vence.

### Final de desistencia

Jogador abandona a missao.

### Final salvando Salsichinha

Jogador salva Salsichinha, mas abandona a missao e Glozium destroi o mundo.

## 9. Perguntas Provaveis Dos Avaliadores

### Por que voce escolheu Python?

Porque o desafio avalia principalmente logica de programacao. Python permite escrever menos codigo estrutural e focar mais nas regras, menus, batalhas e decisoes.

### Por que separou o projeto em varios arquivos?

Para organizar responsabilidades. Cada arquivo cuida de uma parte: historia, combate, personagens, itens, interface e configuracoes.

### Por que existe um arquivo de configuracoes?

Porque vidas, dados e pausas sao valores fixos de regra. Separar esses valores facilita testes e ajustes sem mexer na logica principal.

### Como funciona o dano?

Cada alvo tem um numero secreto. O atacante sorteia numeros. O dano e o numero secreto multiplicado pela quantidade de vezes que ele apareceu.

### Como voce garantiu que o numero secreto nao muda durante a batalha?

Ele e sorteado no inicio da batalha, dentro de `iniciar_batalha()`, e so muda quando uma nova batalha comeca.

### Por que o menu de itens nao consome turno?

Porque a regra que decidi aplicar foi que o jogador pudesse abrir a lista de itens e escolher o item antes de decidir a acao principal.

### Como voce controlou os finais diferentes?

Com estados no heroi, como:

- `tem_espada_zg`;
- `salsichinha_presente`;
- `desistiu_para_salvar_salsichinha`.

Esses estados sao verificados no final da batalha contra Glozium.

### Como funciona a forja?

Se o heroi tem todos os itens obrigatorios, ele pode forjar a Espada ZG. Ao forjar, os itens usados somem do inventario e fica apenas a Espada ZG.

### Como funciona o Worm?

Worm usa uma flag chamada `eh_worm`. Quando essa flag existe, o combate aplica regras especiais: ele comeca enterrado, tem posicao dinamica e precisa da bomba para sair da terra.

### O que voce faria se tivesse mais tempo?

Possiveis melhorias:

- modo de teste para iniciar direto em qualquer ato;
- testes automatizados;
- salvar progresso;
- melhorar balanceamento;
- interface visual simples;
- logs de batalha mais detalhados.

## 10. Pontos Fortes Para Citar

- O projeto cumpre a historia principal.
- O codigo esta separado por responsabilidade.
- O jogo possui decisoes que alteram finais.
- A batalha usa loops, condicionais, listas e randomizacao.
- Os itens alteram mecanicas de combate.
- O inventario e os estados do heroi persistem entre atos.
- O codigo usa apenas Python padrao.


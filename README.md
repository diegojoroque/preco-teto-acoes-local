# Preço Teto Ações Local

Aplicação web local desenvolvida em Python + Flask + JavaScript + CSS para consultar cotações de ações da B3, obter estimativas de EPS por meio do yfinance e calcular indicadores como PPA, preço-teto e dividend yield (DY).

A aplicação é executada localmente e disponibiliza uma interface web simples para visualização e ordenação dos resultados.

---

## Aviso importante — Dados, finalidade e responsabilidade

Esta aplicação foi desenvolvida para **uso próprio do desenvolvedor**, com finalidade de estudo, análise e acompanhamento pessoal de informações relacionadas ao mercado de ações.

Os dados apresentados pela aplicação são obtidos a partir de **fontes e serviços de terceiros**, incluindo, mas não se limitando ao `yfinance` e a outras fontes públicas ou serviços utilizados para obtenção de informações financeiras. A disponibilidade, precisão, atualização, integridade e estrutura desses dados dependem dos respectivos provedores e podem sofrer alterações sem aviso prévio.

Os indicadores e resultados apresentados pela aplicação, incluindo cotação, EPS, payout, PPA, preço-teto e dividend yield (DY), são calculados a partir dos dados obtidos das fontes consultadas e das fórmulas implementadas no código. Portanto, os resultados podem apresentar divergências em relação a outras fontes, metodologias ou cálculos.

A aplicação **não constitui recomendação de investimento, aconselhamento financeiro, indicação de compra ou venda de ativos, nem garantia de rentabilidade**. As informações apresentadas devem ser utilizadas exclusivamente como material auxiliar para análise.

O desenvolvedor **não se responsabiliza por erros, inconsistências, divergências, atrasos, indisponibilidade ou alterações nos dados fornecidos por terceiros**, tampouco por quaisquer decisões ou prejuízos decorrentes da utilização das informações ou dos cálculos apresentados pela aplicação.

A aplicação não foi desenvolvida com a finalidade de prestar serviços financeiros ou fornecer informações de investimento ao público. Seu desenvolvimento e utilização destinam-se ao **uso pessoal do próprio desenvolvedor**.

Qualquer pessoa que utilize, copie, modifique ou faça uso das informações ou do código deste projeto deverá realizar sua própria verificação dos dados e assumir integralmente a responsabilidade por suas decisões e pela utilização da aplicação.

> **Em resumo:** os dados são provenientes de fontes de terceiros, a aplicação foi desenvolvida para uso próprio do desenvolvedor e os resultados apresentados possuem caráter meramente informativo e auxiliar, não havendo garantia quanto à sua precisão, completude ou atualização.

---

## 1. Estrutura do projeto

    preco-teto-acoes-local/
    ├── app.py
    ├── LICENSE
    ├── README.md
    ├── static/
    │   └── style.css
    └── templates/
        └── index.html

### app.py

Arquivo principal da aplicação.

Responsável por:

- Inicializar o Flask.
- Consultar dados financeiros através do yfinance.
- Obter a cotação atual das ações.
- Obter o EPS estimado.
- Calcular o payout médio.
- Calcular o PPA.
- Calcular o preço-teto.
- Calcular o DY.
- Disponibilizar os dados através de uma API.
- Executar as atualizações em uma thread separada.
- Abrir automaticamente o navegador.

### templates/index.html

Interface da aplicação.

Responsável por:

- Exibir a tabela de ações.
- Exibir cotação, preço-teto, DY, PPA, EPS e payout.
- Aplicar cores às linhas de acordo com o DY.
- Permitir atualização dos dados.
- Permitir ordenação alfabética.
- Permitir ordenação por DY crescente ou decrescente.
- Exibir a data e hora da última atualização.

### static/style.css

Folha de estilos da aplicação.

Responsável por:

- Layout da página.
- Formatação da tabela.
- Tamanho das colunas.
- Formatação dos botões.
- Cores das faixas de DY.
- Legenda das cores.
- Rodapé/status.

---

## 2. Requisitos

Para executar a aplicação, é necessário ter instalado:

- Python 3.9 ou superior.
- Pip.
- Acesso à internet para as consultas realizadas pelo yfinance.
- Um navegador web.

É recomendado utilizar um ambiente virtual (`venv`).

---

## 3. Instalação

### 3.1. Abrir o terminal

Entre na pasta do projeto:

    cd preco-teto-acoes-local

No Windows, por exemplo:

    cd "C:\caminho\para\preco-teto-acoes-local"

---

## 4. Criar ambiente virtual

### Windows

Execute:

    python -m venv .venv

Ative o ambiente:

    .venv\Scripts\Activate.ps1

Se estiver utilizando o Prompt de Comando (`cmd`):

    .venv\Scripts\activate

### Linux/macOS

Crie o ambiente:

    python3 -m venv .venv

Ative:

    source .venv/bin/activate

Quando o ambiente estiver ativo, normalmente aparecerá algo semelhante a:

    (.venv)

no início da linha do terminal.

---

## 5. Instalar as dependências

Com o ambiente virtual ativado:

    pip install flask yfinance

As principais bibliotecas utilizadas são:

| Biblioteca | Função |
|---|---|
| Flask | Servidor web e API |
| yfinance | Consulta de dados financeiros |
| threading | Execução da atualização em segundo plano |
| webbrowser | Abertura automática do navegador |
| time | Controle de espera antes de abrir o navegador |
| datetime | Registro da data e hora da atualização |

As bibliotecas `threading`, `webbrowser`, `time` e `datetime` fazem parte da biblioteca padrão do Python e não precisam ser instaladas pelo pip.

---

## 6. Gerar requirements.txt

É recomendado registrar as dependências do projeto.

Com o ambiente virtual ativado:

    pip freeze > requirements.txt

A estrutura passará a ser:

    preco-teto-acoes-local/
    ├── app.py
    ├── requirements.txt
    ├── static/
    │   └── style.css
    └── templates/
        └── index.html

Em outro computador, as dependências poderão ser instaladas com:

    pip install -r requirements.txt

---

## 7. Executar a aplicação

Com o ambiente virtual ativado, execute:

    python app.py

No Linux/macOS, caso seja necessário:

    python3 app.py

A aplicação fará inicialmente uma consulta aos dados configurados.

No terminal deverá aparecer algo semelhante a:

    ==========================================
                  PREÇO TETO
    ==========================================

    Consultando dados iniciais...

    Iniciando atualização...

    Consultando AXIA3...
    Consultando BBAS3...
    Consultando BBSE3...
    ...

Depois que o Flask for iniciado, a aplicação ficará disponível em:

    http://127.0.0.1:5000

O próprio programa também tenta abrir automaticamente o navegador nesse endereço.

---

## 8. Execução resumida

Depois que o projeto já estiver configurado, o processo normal será:

### Windows

    cd "C:\caminho\para\preco-teto-acoes-local"
    .venv\Scripts\Activate.ps1
    python app.py

### Linux/macOS

    cd preco-teto-acoes-local
    source .venv/bin/activate
    python3 app.py

Depois, acessar:

    http://127.0.0.1:5000

---

## 9. Funcionamento da aplicação

A aplicação possui três partes principais:

    Python / Flask
           │
           │ consulta
           ▼
        yfinance
           │
           │ dados financeiros
           ▼
    Cálculos dos indicadores
           │
           ▼
       API Flask
           │
           ▼
       JavaScript
           │
           ▼
       Tabela HTML

---

## 10. Configuração das ações

As ações são configuradas no arquivo `app.py`.

### Prefixos e payouts

A variável:

    tickerPrefix = {
        ...
    }

define as ações e os valores utilizados para calcular o payout médio.

Exemplo:

    "BBSE": [86, 58.1, 64.8, 97.4, 86.1, 106.7],

O payout médio é calculado por:

    payout = sum(payouts) / len(payouts)

Portanto, para adicionar ou alterar uma empresa, os valores dessa configuração precisam ser modificados.

---

## 11. Sufixos dos tickers

A variável:

    priceSuffix = {
        ...
    }

determina quais códigos de negociação serão consultados.

Por exemplo:

    "ITSA": ["3", "4"],

faz com que sejam consultados:

    ITSA3
    ITSA4

Enquanto:

    "BBAS": ["3"],

faz com que seja consultado:

    BBAS3

---

## 12. Configuração do EPS

A variável:

    epsTicker = {
        ...
    }

define qual ticker será utilizado para obter o EPS e qual divisor deverá ser aplicado.

Exemplo:

    "TAEE3": ("TAEE11", 3),
    "TAEE4": ("TAEE11", 3)

Nesse caso, o EPS obtido para TAEE11 é dividido por 3.

Outro exemplo:

    "ITSA3": ("ITSA4", 1),
    "ITSA4": ("ITSA4", 1)

Nesse caso, o EPS utilizado é o de ITSA4, sem divisão adicional.

---

## 13. Cálculos realizados

Depois de obter a cotação e o EPS, a aplicação calcula o payout médio.

Em seguida:

### PPA

O PPA é calculado por:

    ppa = eps * (payout / 100)

Ou seja:

    PPA = EPS × payout

considerando o payout em formato decimal.

### Preço-teto

O preço-teto é calculado por:

    precoTeto = ppa / 0.06

Portanto:

    Preço-teto = PPA / 6%

O percentual de 6% está atualmente fixado no código.

### Dividend Yield

O DY é calculado por:

    dy = ppa / cotacao * 100

Portanto:

    DY = PPA / Cotação × 100

---

## 14. Cores da tabela

A interface utiliza cinco faixas de DY.

| DY | Cor |
|---|---|
| < 6% | Vermelho |
| 6% a < 7% | Amarelo |
| 7% a < 8% | Verde claro |
| 8% a < 9% | Verde médio |
| ≥ 9% | Verde escuro |

Se o DY não estiver disponível, a linha permanece neutra.

Essas regras são implementadas no JavaScript do arquivo `index.html`.

---

## 15. Interface

A tabela apresenta as seguintes colunas:

| Coluna | Descrição |
|---|---|
| Ticker | Código de negociação |
| Price(R$) | Cotação atual |
| MB(R$) | Preço-teto calculado |
| DY(%) | Dividend Yield calculado |
| DPA(R$) | PPA calculado |
| EPS(R$) | EPS obtido |
| PO(%) | Payout médio |

---

## 16. Ordenação

A interface possui três opções de ordenação.

### AZ ↑

Restaura a ordem original definida pelas configurações do `app.py`.

### DY ↑

Ordena o DY do menor para o maior.

### DY ↓

Ordena o DY do maior para o menor.

Valores sem DY disponível são tratados separadamente para permanecerem no final da ordenação correspondente.

---

## 17. Atualização dos dados

Ao clicar em:

    Atualizar

o navegador envia uma requisição:

    POST /api/atualizar

O Flask inicia uma thread:

    thread = threading.Thread(
        target=atualizar_dados
    )

Isso permite que a consulta seja executada em segundo plano.

Enquanto a atualização ocorre, a interface mostra:

    Atualizando...

e:

    Consultando dados...

O JavaScript verifica periodicamente o status da atualização através da API.

---

## 18. APIs disponíveis

A aplicação possui três rotas principais.

### Página principal

    GET /

Retorna a página HTML.

### Consulta dos dados

    GET /api/dados

Retorna um JSON semelhante a:

    {
        "resultados": [],
        "atualizando": false,
        "ultima_atualizacao": "18/09/2026 às 16:30:00"
    }

### Solicitação de atualização

    POST /api/atualizar

Solicita uma nova consulta aos dados.

Se já houver uma atualização em andamento:

    {
        "status": "atualizando"
    }

Caso contrário:

    {
        "status": "iniciado"
    }

---

## 19. Fluxo de inicialização

Ao executar:

    python app.py

ocorre a seguinte sequência:

    1. Python inicia
           ↓
    2. Flask é configurado
           ↓
    3. atualizar_dados()
           ↓
    4. consultar_dados()
           ↓
    5. yfinance consulta as ações
           ↓
    6. EPS é obtido
           ↓
    7. Payout médio é calculado
           ↓
    8. PPA é calculado
           ↓
    9. Preço-teto é calculado
           ↓
    10. DY é calculado
           ↓
    11. Resultados são armazenados
           ↓
    12. Navegador é aberto
           ↓
    13. Flask inicia na porta 5000

---

## 20. Encerrando a aplicação

Para encerrar a aplicação, volte ao terminal onde o Flask está executando e pressione:

    Ctrl + C

O servidor será encerrado.

Caso o ambiente virtual esteja ativo, pode ser desativado com:

    deactivate

---

## 21. Solução de problemas

### `python` não é reconhecido

No Windows, tente:

    py --version

Se funcionar, utilize:

    py app.py

Para criar o ambiente:

    py -m venv .venv

### Erro `No module named flask`

Instale o Flask:

    pip install flask

### Erro `No module named yfinance`

Instale o yfinance:

    pip install yfinance

Ou reinstale todas as dependências:

    pip install -r requirements.txt

### A página não abre

Verifique se o terminal mostra que o Flask está executando.

Tente abrir manualmente:

    http://127.0.0.1:5000

Também é possível verificar se a porta 5000 está sendo utilizada por outro programa.

### A cotação não aparece

A aplicação depende dos dados fornecidos pelo yfinance.

Verifique:

- conexão com a internet;
- código do ticker;
- disponibilidade do ativo;
- funcionamento do serviço consultado;
- eventuais alterações na estrutura de dados retornada pelo yfinance.

A aplicação trata algumas falhas retornando `None`, o que faz o campo correspondente ficar vazio na interface.

---

## 22. Observações sobre os dados

Os dados financeiros são obtidos externamente através do yfinance.

A disponibilidade e a estrutura desses dados podem mudar independentemente da aplicação.

Além disso, o código atual utiliza:

    acao.fast_info["last_price"]

para obter a cotação e:

    .get_earnings_estimate()

para obter o EPS estimado.

Caso o yfinance altere essas interfaces, poderá ser necessário atualizar o código.

---

## 23. Observações sobre o servidor

O Flask está configurado para executar somente localmente:

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )

Isso significa que a aplicação não foi configurada para ser acessada diretamente por outros computadores da rede.

O endereço:

    127.0.0.1

representa o próprio computador onde a aplicação está sendo executada.

---

## 24. Segurança

Esta aplicação foi projetada para uso local.

Não há autenticação de usuários, banco de dados ou controle de acesso implementado.

Por isso, caso futuramente o servidor seja disponibilizado em uma rede ou na internet, será necessário revisar a arquitetura e adicionar mecanismos apropriados de segurança.

---

## 25. Comandos rápidos

### Primeira instalação

    cd preco-teto-acoes-local
    python -m venv .venv

### Windows

    .venv\Scripts\Activate.ps1

### Linux/macOS

    source .venv/bin/activate

### Instalação

    pip install flask yfinance

### Gerar dependências

    pip freeze > requirements.txt

### Executar

    python app.py

### Abrir

    http://127.0.0.1:5000

### Encerrar

    Ctrl + C

### Desativar ambiente

    deactivate

---

## 26. Resumo

O Preço Teto Ações Local é uma aplicação web local composta por:

    Python + Flask
           +
       yfinance
           +
          HTML
           +
       JavaScript
           +
           CSS

Seu fluxo principal é:

    Configuração dos ativos
            ↓
    Consulta ao yfinance
            ↓
       Cotação + EPS
            ↓
       Payout médio
            ↓
           PPA
            ↓
       Preço-teto
            ↓
            DY
            ↓
         API Flask
            ↓
    Tabela no navegador

A aplicação não necessita de banco de dados para funcionar, pois os resultados são mantidos em memória durante a execução do processo Python.

Para iniciar a aplicação após a instalação, basta executar:

    python app.py

e acessar:

    http://127.0.0.1:5000

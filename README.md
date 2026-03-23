# Dash Funter

Painel standalone para analise de carteira comercial fora do Grafana.

O projeto foi montado para cruzar duas exportacoes CSV diretamente no navegador, sem banco, sem backend e sem dependencia do Grafana:

- base principal de contratos
- base detalhada de itens/servicos por contrato

O foco do painel e consolidar uma visao operacional e executiva da carteira, com filtros, vencimentos, status, servicos e detalhe do contrato.

---

## Objetivo

Transformar o dashboard originalmente exportado do Grafana em uma dashboard local, leve e independente, capaz de:

- carregar dois CSVs
- cruzar os dados por numero do contrato
- consolidar status, situacao, servicos e valores
- filtrar a carteira por criterios operacionais
- exibir detalhe do contrato
- exportar a visao filtrada

---

## Fontes de dados

### 1. Base principal de contratos

Arquivo atual:

- `contratos-20260311121947.csv`

Responsabilidade:

- traz o cadastro principal dos contratos
- traz cliente, vendedor, datas, tipo, status, situacao, valor e localidade
- serve como base principal do painel

Campos relevantes usados no merge e na exibicao:

- `Codigo do Contrato`
- `Nº Contrato`
- `Cod. Cliente`
- `Cliente`
- `Tipo`
- `Dt. Cadastro`
- `Dt. Term.`
- `Vendedor 1`
- `Valor`
- `Status`
- `Situacao`
- `Cidade do Cliente`
- `Bairro do Cliente`

### 2. Base detalhada de itens por contrato

Arquivo atual:

- `itens_contratos-20260311130114.csv`

Responsabilidade:

- traz os servicos e itens vinculados a cada contrato
- traz valor unitario, valor total, status e situacao do contrato na base detalhada
- enriquece a base principal

Campos relevantes usados:

- `Nº Contrato`
- `Cliente`
- `Descricao`
- `Servico`
- `Unidades`
- `Valor Unitario`
- `Valor Total`
- `Situacao do Contrato`
- `Status do Contrato`
- `Cidade do Cliente`
- `Bairro do Cliente`

---

## Estrategia de consolidacao

O merge e feito integralmente no front-end, no arquivo `app.js`.

### Chave principal de cruzamento

O cruzamento usa:

- `Nº Contrato` normalizado

Normalizacao aplicada:

- remove caracteres nao numericos
- remove zeros a esquerda

Exemplo:

- `0003036` vira `3036`
- `3036` continua `3036`

Isso permite bater o contrato entre os dois CSVs mesmo quando um vier com formato diferente.

### Regra de consolidacao

Para cada contrato da base principal:

1. localizar os itens do mesmo contrato na base detalhada
2. consolidar servicos associados
3. consolidar valor total por itens
4. priorizar `Status do Contrato` e `Situacao do Contrato` da base detalhada quando existirem
5. manter a base principal como fallback quando nao houver item correspondente

### Regra de valor

O valor exibido no painel segue esta prioridade:

1. soma dos `Valor Total` dos itens detalhados
2. se nao houver itens detalhados, usa o `Valor` da base principal

### Regra de carteira ativa

A carteira ativa considera prioritariamente:

1. `Situacao do Contrato` da base detalhada
2. se nao houver, `Situacao` da base principal

Regra atual:

- se a situacao for `Cancelado`, o contrato nao entra como ativo

---

## Arquivos do projeto

- `index.html`: estrutura da dashboard
- `styles.css`: identidade visual e layout
- `app.js`: leitura dos CSVs, merge, filtros, renderizacao e exportacao
- `contratos-20260311121947.csv`: base principal atual
- `itens_contratos-20260311130114.csv`: base detalhada atual
- `[FUNTER] - CONSULTA BASE DE CARTEIRA - V2.0-1773239813240.json`: export original do Grafana

---

## Funcionalidades atuais

### Painel principal

O painel exibe:

- clientes unicos
- contratos ativos
- valor da carteira
- ticket medio
- vendedor lider
- status dominante
- proximo vencimento

### Blocos analiticos

- carteira por vendedor
- distribuicao por status
- top servicos
- vencimentos proximos
- clientes agregados
- contratos filtrados

### Detalhe do contrato

Ao clicar em uma linha da tabela de contratos, o painel exibe:

- cliente
- vendedor
- status e situacao
- valor consolidado
- data de cadastro
- data de termino
- cidade e bairro
- quantidade de itens vinculados
- lista de servicos associados
- tabela detalhada com:
  - servico
  - unidades
  - valor unitario
  - valor total
  - situacao
  - status

### Exportacao

- `Exportar filtros`: baixa a visao filtrada em CSV
- `Gerar PDF`: usa a impressao do navegador

---

## Filtros disponiveis

O painel atualmente filtra por:

- vendedor
- status
- situacao
- servico
- cidade
- busca textual
- cadastro de
- cadastro ate
- termino de
- termino ate

### Busca textual

A busca textual considera os principais campos consolidados:

- cliente
- codigo do contrato
- descricao
- cidade
- bairro
- tipo
- servicos
- status
- situacao

### Filtros de data

Os filtros de data atuam sobre a base principal:

- `Dt. Cadastro`
- `Dt. Term.`

---

## Visual e usabilidade

A dashboard foi ajustada para uma linguagem mais proxima da identidade da NetTurbo:

- paleta em verde e cinza
- topo institucional
- layout corporativo limpo
- cards executivos
- destaque visual para vencimentos
- truncamento de campos longos com tooltip no hover

### Campos longos

Campos como:

- nome do cliente
- vendedor
- servico
- tipo
- cidade/bairro

sao truncados visualmente para nao quebrar o layout, mas preservam o valor completo no atributo `title`.

---

## Regras de vencimento

O bloco de vencimentos proximos mostra:

- contrato
- cliente
- quantos dias faltam para vencer
- data de termino
- valor

Status visual:

- vermelho: vencido
- amarelo: vence em ate 30 dias
- verde: prazo mais folgado

---

## Como usar

### Forma mais simples

1. Abra `index.html` no navegador.
2. Se a base nao carregar automaticamente, clique em `Carregar contratos` e selecione `contratos-20260311121947.csv`.
3. Clique em `Carregar itens` e selecione `itens_contratos-20260311130114.csv`.
4. O painel cruza as duas bases no navegador.
5. Aplique os filtros desejados.
6. Clique numa linha de contrato para abrir o detalhe.
7. Exporte o resultado quando necessario.

### Com servidor local

Se quiser que os CSVs padrao sejam carregados automaticamente ao abrir a pagina:

- Python: `python -m http.server`
- VS Code Live Server

Depois, abra:

- `http://localhost:8000/`

---

## Limitacoes atuais

- o painel depende de exportacoes CSV atualizadas manualmente
- nao existe persistencia de configuracoes ou filtros
- o merge depende da consistencia do numero do contrato
- se um contrato nao existir na base detalhada, o painel usa apenas a base principal
- metricas originalmente dependentes de outras tabelas do banco/Grafana nao foram reproduzidas literalmente

---

## Decisoes tecnicas

### O que foi escolhido

- manter tudo no front-end
- evitar backend e banco local
- usar o CSV como fonte unica
- cruzar os arquivos no navegador
- priorizar simplicidade operacional

### O que isso evita

- deploy de API
- manutencao de banco auxiliar
- dependencia do Grafana
- dependencia de credenciais externas para consulta

---

## Proximos passos recomendados

1. Adicionar ordenacao clicavel nas colunas das tabelas.
2. Adicionar paginacao na tabela de contratos.
3. Criar filtros rapidos de vencimento:
   - vencidos
   - vence em 30 dias
   - vence em 60 dias
4. Criar busca direta por numero do contrato.
5. Criar uma versao executiva e outra operacional da dashboard.

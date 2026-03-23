# Dash Funter v2 - Documentação Técnica

## Visão Geral

Dashboard standalone para análise da carteira comercial, desenvolvido como alternativa independente ao Grafana. Roda inteiramente no navegador sem necessidade de banco de dados, backend ou dependência de sistemas externos.

**Versão:** 2.0  
**Tecnologia:** HTML/CSS/JavaScript puro  
**Dependências externas:** Leaflet (mapas), OpenStreetMap (tiles)  
**Formato de dados:** CSV  
**Autor:** NetTurbo Telecom  

---

## Arquitetura

### Estrutura de Arquivos

```
04.1 - DASH FUNTER/
├── index_v2.html          # Estrutura HTML principal
├── app_v2.js              # Lógica JavaScript (parse, merge, filtros, render)
├── styles.css             # Estilos visuais
├── contratos.csv          # Base principal de contratos
├── itens_contratos.csv    # Base detalhada de itens por contrato
├── conexoes.csv           # Base de conexões/endereços
├── [FUNTER] - CONSULTA BASE DE CARTEIRA - V2.0.json  # Export original do Grafana
├── README.md              # Documentação original
└── ponto_de_recuperacao.md # Checkpoint de desenvolvimento
```

### Fluxo de Dados

```
CSV Contratos ─────┐
                  ├──► Merge (app_v2.js) ──► Filtros ──► Renderização
CSV Itens ────────┤         │
                  │         ▼
CSV Conexões ─────┘    Normalização
                           │
                           ▼
                    Indexação por Nº Contrato
```

---

## Bases de Dados

### 1. Base de Contratos (contratos.csv)

**Responsabilidade:** Cadastro principal dos contratos

| Campo | Descrição |
|-------|-----------|
| Código do Contrato | Identificador único do contrato |
| Nº Contrato | Número do contrato (chave de cruzamento) |
| Cod. Cliente | Código do cliente |
| Cliente | Nome do cliente |
| Tipo | Tipo de contrato |
| Dt. Cadastro | Data de cadastro |
| Dt. Térm. | Data de término |
| Vendedor 1 | Nome do vendedor responsável |
| Valor | Valor do contrato |
| Status | Status atual |
| Situação | Situação atual |
| Cidade do Cliente | Cidade da instalação |
| Bairro do Cliente | Bairro da instalação |

### 2. Base de Itens (itens_contratos.csv)

**Responsabilidade:** Detalhamento dos serviços por contrato

| Campo | Descrição |
|-------|-----------|
| Nº Contrato | Número do contrato (chave de cruzamento) |
| Cliente | Nome do cliente |
| Descrição | Descrição do item |
| Serviço | Nome do serviço |
| Unidades | Quantidade de unidades |
| Valor Unitário | Valor unitário |
| Valor Total | Valor total do item |
| Situação do Contrato | Situação na base detalhada |
| Status do Contrato | Status na base detalhada |
| Cidade do Cliente | Cidade |
| Bairro do Cliente | Bairro |

### 3. Base de Conexões (conexoes.csv)

**Responsabilidade:** Endereços de instalação e dados de rede

| Campo | Descrição |
|-------|-----------|
| Código do Contrato | Identificador do contrato |
| Código da Conexão | Identificador da conexão |
| Descrição do Contrato | Descrição |
| Código do Serviço | Código do serviço |
| Serviço | Nome do serviço |
| Usuário | Usuário de acesso |
| MAC | Endereço MAC do equipamento |
| IP | Endereço IP |
| Concentrador | Equipamento concentrador |
| Ponto de Acesso | Ponto de acesso |
| Tipo de Equipamento | Tipo do equipamento |
| Rua | Logradouro |
| Número | Número do endereço |
| Complemento | Complemento |
| CEP | CEP |
| Bairro | Bairro |
| Cidade | Cidade |
| Estado | Estado |
| Latitude | Coordenada latitude |
| Longitude | Coordenada longitude |
| Tipo de Conexão | Tipo da conexão |
| Ativo | Se está ativo (Sim/Não) |

---

## Cruzamento de Dados

### Chave de Junção

O cruzamento usa o **Nº Contrato** normalizado como chave:

```
Normalização aplicada:
1. Remove caracteres não numéricos
2. Remove zeros à esquerda

Exemplo:
- "0003036" → "3036"
- "3036" → "3036"
```

### Regras de Consolidação

| Campo | Regra |
|-------|-------|
| **Valor** | Soma dos `Valor Total` dos itens; se não houver itens, usa `Valor` da base principal |
| **Status** | Prioriza da base de itens; fallback para base principal |
| **Situação** | Prioriza da base de itens; fallback para base principal |
| **Serviços** | Consolida todos os serviços dos itens vinculados |
| **Endereço** | Tenta base de conexões; fallback para base principal |
| **Cidade/Bairro** | Prioriza base de conexões; fallback para base principal |

---

## Funcionalidades

### Painel de Métricas (Cards Superiores)

- **Clientes únicos** - Contagem distinta de clientes na base filtrada
- **Contratos ativos** - Contratos com situação diferente de "Cancelado"
- **Valor da carteira** - Soma dos valores dos contratos ativos
- **Ticket médio** - Valor médio por contrato
- **Conexões ativas** - Total de conexões vinculadas

### Cards Executivos

- **Vendedor líder** - Vendedor com maior valor na carteira + participação %
- **Status dominante** - Status mais frequente na base + contagem
- **Próximo vencimento** - Contrato com menor data de término

### Blocos Analíticos

| Bloco | Descrição |
|-------|-----------|
| Carteira por vendedor | Ranking de vendedores por valor |
| Distribuição por status | Contagem por status (Aprovado, Em aprovação, Cancelado) |
| Top serviços | Serviços mais frequentes na base |
| Cidades mais atendidas | Ranking de cidades por quantidade de contratos |
| Vencimentos próximos | Próximos 12 contratos a vencer |
| Mapa de conexões | Visualização geográfica dos pontos |

### Tabelas

| Tabela | Conteúdo |
|--------|----------|
| Clientes | Top 50 clientes por valor total, com quantidade de contratos e conexões |
| Contratos | Top 80 contratos ordenados por valor, com seleção para detalhe |

### Detalhe do Contrato

Ao clicar em um contrato, exibe:

- Informações básicas (cliente, vendedor, status, situação)
- Valor consolidado
- Datas (cadastro, término)
- Endereço de instalação com link para Google Maps
- Lista de serviços vinculados
- Tabela de itens detalhados
- Tabela de conexões vinculadas

---

## Filtros Disponíveis

| Filtro | Tipo | Atuação |
|--------|------|---------|
| Vendedor | Select | Campo `Vendedor 1` normalizado |
| Status | Select | Campo `Status` ou `Status do Contrato` |
| Situação | Select | Campo `Situação` ou `Situação do Contrato` |
| Serviço | Select | Serviços dos itens vinculados |
| Cidade | Select | Campo `Cidade do Cliente` |
| Bairro | Select | Campo `Bairro do Cliente` |
| Busca | Texto | Busca em múltiplos campos |
| Cadastro de/até | Data | Campo `Dt. Cadastro` |
| Término de/até | Data | Campo `Dt. Térm.` |

### Busca Textual

A busca considera os campos:
- Cliente
- Código do contrato
- Descrição
- Cidade
- Bairro
- Tipo
- Serviços
- Status
- Situação
- Rua (das conexões)

### Normalização na Busca

Todos os filtros de texto são normalizados (case-insensitive, sem acentos) para garantir correspondência independente da grafia.

---

## Exportação

### Exportar Filtros (CSV)

Gera arquivo CSV com os dados filtrados contendo:
- Código do Contrato
- Código do Cliente
- Cliente
- Serviço
- Tipo
- Situação
- Status
- Vendedor
- Cidade
- Bairro
- Endereço
- CEP
- Data de Cadastro
- Data de Término
- Valor
- Quantidade de Itens
- Quantidade de Conexões

### Gerar PDF

Utiliza a função de impressão do navegador para gerar PDF.

---

## Mapa

### Tecnologia
- **Biblioteca:** Leaflet.js
- **Tiles:** OpenStreetMap

### Funcionalidades
- Exibe pontos geolocalizados das conexões
- Cores indicativas: verde (ativo), amarelo (inativo)
- Popup com informações do cliente, contrato, endereço e IP
- Auto-zoom para Fitting os pontos visíveis

### Campos Necessários
Para o mapa funcionar, a base de conexões precisa conter:
- `Latitude` - valor numérico
- `Longitude` - valor numérico

---

## Visual e Design

### Paleta de Cores

| Cor | Uso |
|-----|-----|
| Verde NetTurbo (#2e8b57) | Destaques, valores positivos |
| Verde claro (#66FF66) | Títulos hero |
| Laranja (#FF4500) | Accent no logo |
| Cinza escuro (#1a1a2e) | Background principal |
| Cinza médio (#2d2d44) | Cards e painéis |

### Tipografia
- **Fontes:** Arial, sans-serif (sistema)
- **Hierarquia:** H1 > H2 > strong > body

### Badges de Status

| Status | Classe CSS |
|--------|------------|
| Em aprovação | `em-aprovacao` |
| Aprovado | `aprovado` |
| Cancelado | `cancelado` |

### Badges de Vencimento

| Condição | Cor |
|----------|-----|
| Vencido | Vermelho |
| Até 30 dias | Amarelo |
| Mais de 30 dias | Verde |

---

## Configuração

### Arquivo app_v2.js - Constantes

```javascript
const DEFAULT_CONTRACTS_CSV = 'contratos-20260311121947.csv';
const DEFAULT_ITEMS_CSV = 'itens_contratos-20260311130114.csv';
const DEFAULT_CONNECTIONS_CSV = 'Março_2026/conexoes-20260320111419.csv';
```

Para alterar os CSVs carregados automaticamente, modifique estas constantes.

---

## Como Testar Localmente

### Opção 1: Servidor Python (Recomendado)

```bash
cd "C:\Users\alan.moreira\Documents\00 - 2026\04.1 - DASH FUNTER"
python -m http.server 8000
```

Abrir: `http://localhost:8000/index_v2.html`

### Opção 2: VS Code Live Server

1. Instalar extensão "Live Server" no VS Code
2. Clicar com botão direito em `index_v2.html`
3. Selecionar "Open with Live Server"

### Opção 3: Direto no Navegador

1. Duplo clique em `index_v2.html`
2. Carregar CSVs manualmente pelo botão "Carregar"

---

## Como Distribuir para Terceiros

### Opção 1: Pasta Compactada

1. Compactar pasta inteira em `.zip`
2. Enviar para destinatário
3. Destinatário descompacta e abre `index_v2.html`

### Opção 2: Hospedagem Online

Plataformas gratuitas:
- **GitHub Pages** - Upload no GitHub
- **Netlify Drop** - Arrastar pasta
- **Vercel** - Deploy rápido

### Opção 3: Intranet/SharePoint

1. Hospedar arquivos em servidor interno
2. Compartilhar link interno

---

## Limitações Conhecidas

1. Dependência de exportações CSV manuais
2. Sem persistência de filtros ou configurações
3. Merge depende de consistência no número do contrato
4. Contratos sem correspondência na base de itens usam apenas dados principais
5. Mapa requer coordenadas geográficas válidas na base de conexões

---

## Melhorias Futuras Recomendadas

1. Paginação nas tabelas de clientes e contratos
2. Ordenação clicável nas colunas
3. Filtros rápidos de vencimento (vencidos, 30 dias, 60 dias)
4. Busca direta por número do contrato
5. Persistência de filtros no localStorage
6. Gráficos adicionais (histograma de valores, timeline de vencimentos)
7. Versão mobile responsiva
8. Tema claro/escuro

---

## Estrutura do Código (app_v2.js)

### Estado Global (`state`)

```javascript
state = {
  rawContracts: [],      // Dados brutos dos contratos
  rawItems: [],         // Dados brutos dos itens
  rawConnections: [],   // Dados brutos das conexões
  rows: [],             // Dados normalizados e mesclados
  filteredRows: [],     // Dados após aplicação de filtros
  selectedContractKey: null, // Contrato selecionado para detalhe
  datasets: { ... },    // Nomes dos arquivos carregados
  filters: { ... }      // Estado atual dos filtros
}
```

### Principais Funções

| Função | Responsabilidade |
|--------|-----------------|
| `parseCsv()` | Parser de CSV com suporte a campos entre aspas |
| `parseCurrency()` | Converte string monetária em número |
| `parseDate()` | Converte string de data DD/MM/AAAA em Date |
| `normalizeText()` | Remove acentos e normaliza para comparação |
| `normalizeContractKey()` | Normaliza número do contrato |
| `normalizeContractRow()` | Normaliza linha da base de contratos |
| `normalizeItemRow()` | Normaliza linha da base de itens |
| `normalizeConnectionRow()` | Normaliza linha da base de conexões |
| `buildItemsIndex()` | Cria índice Map de itens por contrato |
| `buildConnectionsIndex()` | Cria índice Map de conexões por contrato |
| `consolidateRows()` | Faz o merge das três bases |
| `applyFilters()` | Aplica todos os filtros ativos |
| `render()` | Coordena toda a renderização |
| `renderSummary()` | Atualiza cards de métricas |
| `renderRanking()` | Renderiza rankings com barras de progresso |
| `renderDistribution()` | Renderiza distribuição por status |
| `renderExpiring()` | Renderiza tabela de vencimentos |
| `renderClients()` | Renderiza tabela de clientes |
| `renderContracts()` | Renderiza tabela de contratos |
| `renderContractDetail()` | Renderiza painel de detalhe |
| `renderMap()` | Renderiza mapa com Leaflet |
| `exportFilteredRows()` | Gera CSV dos dados filtrados |
| `updateFiltersFromData()` | Popula selects com opções únicas |

---

## Contato e Suporte

Para dúvidas ou problemas com o Dash Funter v2, contactar a equipe de desenvolvimento da NetTurbo Telecom.

---

*Documentação gerada em 20/03/2026*

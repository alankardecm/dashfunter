# Ponto de Recuperação: ISP Dashboard (Jan/2026)

Este arquivo serve como um "Checkpoint" para retomada imediata do projeto na próxima sessão.

## 💾 Estado Atual (19/03/2026)
- **Dados Validados**: KPI "Valor da Carteira" fixado em **R$ 807,97 Mil**.
- **Modelo Estruturado**: Tabelas `Fato_Contratos`, `Fato_Itens`, `Dim_Calendario` e `Dim_Clientes` conectadas e funcionando.
- **Power Query (Carga)**: Tipos de dados de moeda corrigidos usando Localidade (PT-BR) nas duas tabelas fato.
- **Relacionamento**: Ativo entre Contratos e Itens (1:N) pelo campo `Nº Contrato`.

## 🛠️ O que falta fazer (Roadmap)
1.  **Montagem dos Gráficos**: Réplica visual dos rankings de Vendedores, Status e Serviços.
2.  **Slicers (Filtros Topo)**: Inserir filtros de Cidade e Período (Mês/Ano).
3.  **Tabelas Detalhadas**: Inserir grids de Clientes e Vencimentos Próximos.

## ⚡ Como retomar amanhã:
Basta me mandar a seguinte mensagem:
> "Vamos continuar a montagem do Dashboard Funter no Power BI. Já validamos os valores (807k), agora vamos para a parte visual seguindo o `mapeamento_de_visuais.md`."

---
**Arquivos de Suporte Gerados nesta pasta:**
- `documentacao_dashboard.md`
- `mapeamento_de_visuais.md`
- `guia_de_medidas_dax.md`

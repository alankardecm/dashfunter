# Deploy Online - Dash Funter v2

## Opção 1: Netlify Drop (Mais Rápido)

### Passo a Passo:
1. Acesse: https://app.netlify.com/drop
2. Arraste esta pasta ("dash-funter-online") para a área de drop
3. Aguarde o upload
4. Receba o link permanente para compartilhar

**Vantagens:**
- Grátis
- Sem cadastro
- Link permanente
- Upload em segundos

---

## Opção 2: Vercel

### Passo a Passo:
1. Acesse: https://vercel.com
2. Faça login (GitHub/Google)
3. Clique em "Add New" > "Project"
4. Selecione "Deploy from Local"
5. Arraste esta pasta
6. Deploy automático

**Vantagens:**
- CDN global rápido
- SSL automático
- Custom domains

---

## Opção 3: GitHub Pages

### Passo a Passo:
1. Crie repositório no GitHub
2. Faça upload dos arquivos
3. Vá em Settings > Pages
4. Selecione branch "main"
5. Deploy automático

---

## Arquivos Necessários Online

Esta pasta contém:
- `index_v2.html` - Página principal
- `app_v2.js` - Lógica da aplicação
- `styles.css` - Estilos visuais
- `assets/` - Logo da NetTurbo
- `*.csv` - Bases de dados (carrega automaticamente)

---

## Atualizando os Dados

Para atualizar os dados da dashboard:
1. Substitua os arquivos CSV na pasta
2. O deploy já está pronto, basta re-upload se necessário

**CSV padrão atual:**
- contratos-20260311121947.csv
- itens_contratos-20260311130114.csv
- conexoes-20260320111419.csv

---

## Se Não Carregar Automaticamente

Se os CSVs não carregarem, pode ser CORS. Nesse caso:
1. Abra o console (F12) e verifique erros
2. Se houver erro de CORS, use o Netlify Drop (que permite CORS)

---

## Suporte

NetTurbo Telecom - Dash Funter v2
Gerado em: 20/03/2026

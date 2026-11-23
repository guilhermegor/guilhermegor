[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md)

# Guilherme Rodrigues

**Mercado financeiro × matemática × engenharia de software.** Construo ferramentas open source confiáveis e escaláveis para os problemas que as instituições financeiras realmente têm, com visão front-to-back, da mesa de operações à administração fiduciária.

Feitas para tesourarias de bancos, corretoras, administradores fiduciários e gestoras: precificação, risco, compliance, controladoria e reporte regulatório.

<sub>CFA Level I · ANBIMA CGA · São Paulo, BR</sub>

## Para onde isso vai

1. **Fundação** (agora): bibliotecas open source para dados públicos, layouts de arquivos regulatórios e a matemática de precificação, risco e tributos. Tudo o que está abaixo.
2. **APIs e pipelines de dados**: serviços `hub-*` sobre essas bibliotecas para dados de mercado, precificação, posições, estatísticas, risco, rulebooks e documentos de fundos.
3. **Produtos**: ferramentas front-to-back para instituições financeiras, do pré-trade à contabilidade.

## Como está organizado

<sub>Cada repositório pertence a uma família, e o prefixo do nome diz qual. Cada família tem uma única função.</sub>

| Família | O que faz |
|---|---|
| **Open data** | `opendata-*`: SDKs não oficiais para os dados que reguladores, bolsas e institutos de estatística publicam. Tipados, com cache e proveniência. |
| **Layouts** | `layouts-*`: os formatos de arquivo que as instituições trocam entre si. Ler, montar, validar e gravar o arquivo, sem chamadas de rede ou banco: buscá-lo e enviá-lo fica com `integrations-*`. |
| **Pure** | `pure*`: matemática, precificação, risco, tributos e atribuição de performance. Só cálculo, sem I/O. Um número calculado fica aqui mesmo quando a regra por trás dele muda com o tempo. |
| **Rulebooks** | `rulebooks-*`: normas como dado, vigentes em uma data. Uma linha por dispositivo (ato, artigo, parágrafo), com o texto literal, a fonte e o hash do documento original para auditoria, para o compliance de fundos. Devolvem a norma, nunca um resultado calculado: aplicar a norma é `pure*`. |
| **Integrations** | `integrations-*`: clientes para as plataformas que as equipes de operações já usam. |
| **Hubs** | `hub-*`: serviços que são donos dos dados de um tema e os expõem por uma API. Código aberto; dados e configuração ficam fora do repositório. |
| **Ferramentas de engenharia** | Scaffolding, ambiente de desenvolvimento e checagens de release por trás de cada repositório daqui. |

## Publicados

<sub>Públicos e publicados hoje.</sub>

| Repositório | O que faz |
|---|---|
| **Open data** | |
| [opendata-cvm](https://github.com/guilhermegor/opendata-cvm) | Dados de emissores e fundos da CVM, incluindo o informe mensal de FIDC |
| [opendata-b3](https://github.com/guilhermegor/opendata-b3) | Arquivos públicos da B3 |
| [opendata-bcb](https://github.com/guilhermegor/opendata-bcb) | Dados do Banco Central do Brasil (SGS, Olinda/PTAX, Focus, boletins de cotações, cadastro de bancos), com cache e proveniência |
| [opendata-calendars](https://github.com/guilhermegor/opendata-calendars) | Calendários de feriados buscados direto de quem os publica (B3, ANBIMA, FEBRABAN, NASDAQ, feriados federais dos EUA), com cache e proveniência |
| [opendata-rfb](https://github.com/guilhermegor/opendata-rfb) | Dados públicos da Receita Federal |
| **Layouts** | |
| [layouts-cvm](https://github.com/guilhermegor/layouts-cvm) | Montar e validar os arquivos de fundos enviados à CVM |
| **Pure** | |
| [purecalendars](https://github.com/guilhermegor/purecalendars) | Calendários de dias úteis do Brasil e dos EUA, calculados offline (antigo `wwdates`). A busca de feriados na web fica no `opendata-calendars` |
| [purepii-br](https://github.com/guilhermegor/purepii-br) | Validar, aplicar e remover a máscara de documentos brasileiros (CPF, CNPJ, RG, CNH e outros). Antigo `pure-docs-br` |
| [pure-schema-regimes](https://github.com/guilhermegor/pure-schema-regimes) | Adaptadores de schema para séries cujas colunas mudam no meio do caminho |
| **Ferramentas de engenharia** | |
| [blueprintx](https://github.com/guilhermegor/blueprintx) | O scaffolding por trás de cada repositório daqui |
| [timeglass](https://github.com/guilhermegor/timeglass) | Uso e cobrança de assinaturas de IA entre fornecedores |
| [dotfiles-linux-dev](https://github.com/guilhermegor/dotfiles-linux-dev) | Máquina de desenvolvimento reprodutível |

## Roadmap

<sub>Planejados, ainda não públicos. Mesmas famílias de cima.</sub>

### Open data

- **Reguladores e entidades de mercado brasileiros:** opendata-funddocs-cvm · opendata-treasury-br · opendata-anbima-public · opendata-anbima-data · opendata-debenturescombr
- **Preços, taxas, ratings e commodities:** opendata-global-rates · opendata-world-government-bonds · opendata-trading-economics · opendata-spglobal · opendata-yahii · opendata-mais-retorno · opendata-cepea · opendata-coincap · opendata-coinmarket
- **Macro e fiscal:** opendata-ibge · opendata-fred-us · opendata-fiscal-data-treasury-us
- **Reguladores dos EUA:** opendata-finra-us
- **Outros:** opendata-who-int

### Layouts

- **Enviados a reguladores e ao fisco:** layouts-bcb · layouts-nfse
- **Padrões de mercado entre instituições:** layouts-anbima · layouts-febraban

### Pure

- **Matemática e dados:** puremaths · puredsa · puretidy
- **Precificação e risco:** purepricing · purepricing-br · purerisk
- **Performance de fundos:** pureattribution · purefees
- **Tributos:** puretaxes-br

### Rulebooks

rulebooks-funds-br · rulebooks-funds-us

### Integrations

integrations-b3 · integrations-nfse · integrations-pipefy · integrations-typeform

### Hubs

- **Insumos coletados (persistidos como recebidos: dados de mercado, posições, regulamentos e prospectos de fundos):** hub-marketdata · hub-positions · hub-funddocs
- **Calculados (preços e gregas, parâmetros de mercado, medidas de risco):** hub-pricing · hub-statistics · hub-risk
- **Regras (todos os pacotes `rulebooks-*`, versionados e consultáveis):** hub-rulebooks

### Ferramentas de engenharia

determinism · publishprobe

## Stack

- **Linguagens:** Python · TypeScript · JavaScript · SQL · HTML · CSS · VBA
- **Runtimes:** Node.js
- **Frameworks:** FastAPI · NestJS · React

## Contato

[LinkedIn](https://www.linkedin.com/in/guilhermegor/)

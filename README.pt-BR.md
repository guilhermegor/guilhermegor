[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md)

# Guilherme Rodrigues

**Mercado financeiro × matemática × engenharia de software.** Construo ferramentas open source confiáveis e escaláveis para os problemas que as instituições financeiras realmente têm, com visão front-to-back, da mesa de operações à administração fiduciária.

Feitas para tesourarias de bancos, corretoras, administradores fiduciários e gestoras: precificação, risco, compliance, controladoria e reporte regulatório.

<sub>CFA Level I · ANBIMA CGA · São Paulo, BR</sub>

## Para onde isso vai

1. **Fundação** (agora): bibliotecas open source para dados públicos, layouts de arquivos regulatórios e a matemática de precificação e risco. Tudo o que está abaixo.
2. **APIs e pipelines de dados**: serviços sobre essas bibliotecas para posições, dados de mercado, documentos regulatórios, precificação e risco de carteira.
3. **Produtos**: ferramentas front-to-back para instituições financeiras, do pré-trade à contabilidade.

## Como está organizado

<sub>Cada biblioteca pertence a uma família, e o prefixo do nome diz qual. Cada família tem uma única função.</sub>

| Família | O que faz |
|---|---|
| **Open data** | `opendata-*`: SDKs não oficiais para os dados que reguladores, bolsas e institutos de estatística publicam. Tipados, com cache e proveniência. |
| **Layouts** | `layouts-*`: os formatos de arquivo que as instituições trocam entre si. Ler, montar e validar, sem I/O. |
| **Pure** | `pure*`: matemática, precificação, risco e atribuição de performance. Só cálculo, sem I/O. |
| **Rulebooks** | `rulebooks-*`: as regras de fundos vigentes em uma data. |
| **Integrations** | `integrations-*`: clientes para as plataformas que as equipes de operações já usam. |
| **Ferramentas de engenharia** | Scaffolding, ambiente de desenvolvimento e checagens de release por trás de cada repositório daqui. |

## Publicados

<sub>Públicos e publicados hoje.</sub>

| Repositório | O que faz |
|---|---|
| **Open data** | |
| [opendata-cvm](https://github.com/guilhermegor/opendata-cvm) | Dados de emissores e fundos da CVM, incluindo o informe mensal de FIDC |
| [opendata-b3](https://github.com/guilhermegor/opendata-b3) | Arquivos públicos da B3 |
| [opendata-rfb](https://github.com/guilhermegor/opendata-rfb) | Dados públicos da Receita Federal |
| **Layouts** | |
| [layouts-cvm](https://github.com/guilhermegor/layouts-cvm) | Montar e validar os arquivos de fundos enviados à CVM |
| **Pure** | |
| [wwdates](https://github.com/guilhermegor/wwdates) | Calendários de dias úteis no mundo todo |
| **Ferramentas de engenharia** | |
| [blueprintx](https://github.com/guilhermegor/blueprintx) | O scaffolding por trás de cada repositório daqui |
| [timeglass](https://github.com/guilhermegor/timeglass) | Uso e cobrança de assinaturas de IA entre fornecedores |
| [dotfiles-linux-dev](https://github.com/guilhermegor/dotfiles-linux-dev) | Máquina de desenvolvimento reprodutível |

## Roadmap

<sub>Planejados, ainda não públicos. Mesmas famílias de cima.</sub>

### Open data

- **Reguladores e entidades de mercado brasileiros:** opendata-funddocs-cvm · opendata-bcb · opendata-treasury-br · opendata-anbima-pub · opendata-anbima-data · opendata-debenturescombr
- **Preços, taxas, ratings e commodities:** opendata-global-rates · opendata-world-government-bonds · opendata-trading-economics · opendata-spglobal · opendata-yahii · opendata-mais-retorno · opendata-cepea · opendata-coincap · opendata-coinmarket
- **Macro e fiscal · reguladores dos EUA · outros:** opendata-ibge · opendata-fred-us · opendata-fiscal-data-treasury-us · opendata-finra-us · opendata-who-int

### Layouts

- **Enviados a reguladores:** layouts-bcb
- **Padrões de mercado entre instituições:** layouts-anbima · layouts-febraban

### Pure

puremath · purepricing · purepricing-br · purerisk · pureattribution · purefees · puretidy · puredsa

### Rulebooks

rulebooks-funds-br · rulebooks-funds-us

### Integrations

integrations-b3 · integrations-pipefy · integrations-typeform

### Ferramentas de engenharia

determinism · publishprobe

## Stack

- **Linguagens:** Python · TypeScript · JavaScript · SQL · HTML · CSS · VBA
- **Runtimes:** CPython · Node.js
- **Frameworks:** FastAPI · NestJS · React

## Contato

[LinkedIn](https://www.linkedin.com/in/guilhermegor/)

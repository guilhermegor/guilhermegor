[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md)

# Guilherme Rodrigues

**Financial markets × mathematics × software engineering.** I build reliable, scalable open-source tooling for the problems financial institutions actually have, with a front-to-back view, from trading desks to fund administration.

Built for bank treasuries, brokers, fund administrators and asset managers: pricing, risk, compliance, controllership and regulatory reporting.

<sub>CFA Level I · ANBIMA CGA · São Paulo, BR</sub>

## Where this is going

1. **Foundation** (now): open-source libraries for public data, regulatory file formats, and pricing and risk math. Everything below.
2. **APIs and data pipelines**: services over those libraries for positions, market data, regulatory documents, pricing and portfolio risk.
3. **Products**: front-to-back tooling for financial institutions, from pre-trade to accounting.

## How it's organized

<sub>Every library belongs to one family, and the prefix of its name says which. Each family has one job.</sub>

| Family | What it does |
|---|---|
| **Open data** | `opendata-*`: unofficial SDKs for data that regulators, exchanges and statistics agencies publish. Typed, cached, with provenance. |
| **Layouts** | `layouts-*`: the file formats institutions exchange. Read, build and validate, with no I/O. |
| **Pure** | `pure*`: math, pricing, risk and performance attribution. Computation only, no I/O. |
| **Rulebooks** | `rulebooks-*`: fund rules as in force on a given date. |
| **Integrations** | `integrations-*`: clients for the platforms operations teams already use. |
| **Engineering tooling** | Scaffolding, dev environment and release checks behind every repo here. |

## Shipped

<sub>Public and published today.</sub>

| Repository | What it does |
|---|---|
| **Open data** | |
| [opendata-cvm](https://github.com/guilhermegor/opendata-cvm) | CVM issuer and fund data, FIDC monthly reports included |
| [opendata-b3](https://github.com/guilhermegor/opendata-b3) | B3 public files |
| [opendata-rfb](https://github.com/guilhermegor/opendata-rfb) | Receita Federal public data |
| **Layouts** | |
| [layouts-cvm](https://github.com/guilhermegor/layouts-cvm) | Build and validate the fund files sent to the CVM |
| **Pure** | |
| [wwdates](https://github.com/guilhermegor/wwdates) | Global business-day calendars |
| **Engineering tooling** | |
| [blueprintx](https://github.com/guilhermegor/blueprintx) | Project scaffolding behind every repo here |
| [timeglass](https://github.com/guilhermegor/timeglass) | AI subscription usage and billing across vendors |
| [dotfiles-linux-dev](https://github.com/guilhermegor/dotfiles-linux-dev) | Reproducible dev machine |

## Roadmap

<sub>Planned, not public yet. Same families as above.</sub>

### Open data

- **Brazilian regulators & market bodies:** opendata-funddocs-cvm · opendata-bcb · opendata-treasury-br · opendata-anbima-pub · opendata-anbima-data · opendata-debenturescombr
- **Prices, rates, ratings & commodities:** opendata-global-rates · opendata-world-government-bonds · opendata-trading-economics · opendata-spglobal · opendata-yahii · opendata-mais-retorno · opendata-cepea · opendata-coincap · opendata-coinmarket
- **Macro & fiscal · US regulators · other:** opendata-ibge · opendata-fred-us · opendata-fiscal-data-treasury-us · opendata-finra-us · opendata-who-int

### Layouts

- **Filed with regulators:** layouts-bcb
- **Market standards between institutions:** layouts-anbima · layouts-febraban

### Pure

puremath · purepricing · purepricing-br · purerisk · pureattribution · purefees · puretidy · puredsa

### Rulebooks

rulebooks-funds-br · rulebooks-funds-us

### Integrations

integrations-b3 · integrations-pipefy · integrations-typeform

### Engineering tooling

determinism · publishprobe

## Stack

- **Languages:** Python · TypeScript · JavaScript · SQL · HTML · CSS · VBA
- **Runtimes:** CPython · Node.js
- **Frameworks:** FastAPI · NestJS · React

## Connect

[LinkedIn](https://www.linkedin.com/in/guilhermegor/)

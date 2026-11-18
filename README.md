[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md)

# Guilherme Rodrigues

**Financial markets × mathematics × software engineering.** I build reliable, scalable open-source tooling for the problems financial institutions actually have, with a front-to-back view, from trading desks to fund administration.

Built for bank treasuries, brokers, fund administrators and asset managers: pricing, risk, compliance, controllership and regulatory reporting.

<sub>CFA Level I · ANBIMA CGA · São Paulo, BR</sub>

## Where this is going

1. **Foundation** (now): open-source libraries for public data, regulatory file formats, and the math behind pricing, risk and taxes. Everything below.
2. **APIs and data pipelines**: `hub-*` services over those libraries for market data, pricing, positions, statistics, risk, rulebooks and fund documents.
3. **Products**: front-to-back tooling for financial institutions, from pre-trade to accounting.

## How it's organized

<sub>Every repository belongs to one family, and the prefix of its name says which. Each family has one job.</sub>

| Family | What it does |
|---|---|
| **Open data** | `opendata-*`: unofficial SDKs for data that regulators, exchanges and statistics agencies publish. Typed, cached, with provenance. |
| **Layouts** | `layouts-*`: the file formats institutions exchange. Read, build, validate and write the file, with no network or database calls: fetching and sending it belong to `integrations-*`. |
| **Pure** | `pure*`: math, pricing, risk, taxes and performance attribution. Computation only, no I/O. A computed number belongs here even when the rule behind it changes over time. |
| **Rulebooks** | `rulebooks-*`: regulations as data, as in force on a given date. One row per provision (act, article, paragraph), with its verbatim text, source and the original document's hash for audit, for fund compliance. They return the rule, never a computed result: applying the rule is `pure*`. |
| **Integrations** | `integrations-*`: clients for the platforms operations teams already use. |
| **Hubs** | `hub-*`: services that own the data for one theme and expose it through an API. Open-source code; data and configuration stay out of the repo. |
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
| [wwdates](https://github.com/guilhermegor/wwdates) | Global business-day calendars. Being renamed to `purecalendars`; fetching holidays from the web moves to `opendata-calendars` |
| [pure-docs-br](https://github.com/guilhermegor/pure-docs-br) | Validate, mask and unmask Brazilian document numbers (CPF, alphanumeric CNPJ). Being renamed to `purepii-br` |
| [pure-schema-regimes](https://github.com/guilhermegor/pure-schema-regimes) | Schema adapters for series whose columns change mid-series |
| **Engineering tooling** | |
| [blueprintx](https://github.com/guilhermegor/blueprintx) | Project scaffolding behind every repo here |
| [timeglass](https://github.com/guilhermegor/timeglass) | AI subscription usage and billing across vendors |
| [dotfiles-linux-dev](https://github.com/guilhermegor/dotfiles-linux-dev) | Reproducible dev machine |

## Roadmap

<sub>Planned, not public yet. Same families as above.</sub>

### Open data

- **Brazilian regulators & market bodies:** opendata-funddocs-cvm · opendata-bcb · opendata-treasury-br · opendata-anbima-public · opendata-anbima-data · opendata-debenturescombr
- **Prices, rates, ratings & commodities:** opendata-global-rates · opendata-world-government-bonds · opendata-trading-economics · opendata-spglobal · opendata-yahii · opendata-mais-retorno · opendata-cepea · opendata-coincap · opendata-coinmarket
- **Macro & fiscal · US regulators · other:** opendata-ibge · opendata-fred-us · opendata-fiscal-data-treasury-us · opendata-finra-us · opendata-who-int · opendata-calendars

### Layouts

- **Filed with regulators and tax authorities:** layouts-bcb · layouts-nfse
- **Market standards between institutions:** layouts-anbima · layouts-febraban

### Pure

puremaths · purepricing · purepricing-br · purerisk · pureattribution · purefees · puretaxes-br · puretidy · puredsa

### Rulebooks

rulebooks-funds-br · rulebooks-funds-us

### Integrations

integrations-b3 · integrations-nfse · integrations-pipefy · integrations-typeform

### Hubs

hub-marketdata · hub-pricing · hub-positions · hub-statistics · hub-risk · hub-rulebooks · hub-funddocs

### Engineering tooling

determinism · publishprobe

## Stack

- **Languages:** Python · TypeScript · JavaScript · SQL · HTML · CSS · VBA
- **Runtimes:** Node.js
- **Frameworks:** FastAPI · NestJS · React

## Connect

[LinkedIn](https://www.linkedin.com/in/guilhermegor/)

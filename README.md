# Golden Breeze

<p align="center">
  <strong>English</strong> · <a href="README.uk.md">Українська</a> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

![Golden Breeze — Multi-Agent Trading Platform](assets/brand/golden-breeze-banner-en.svg)

**Multi-Agent Trading Platform: collaborative work of specialized AI agents across the trading workflow — from market analysis and trading decisions to execution, position management, and risk control under user governance.**

Golden Breeze is built for collaborative work of specialized AI agents in trading. From a single Control Desk, the user governs agents, their tasks, and access to connected trading accounts: from market analysis, decision-making, position management, and risk control to research, strategy engineering, isolated verification, and the versioned strategy catalog.

[**Download for Windows (v0.14.0-alpha)**](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/GoldenBreeze-FirstInstall-0.14.0-alpha.exe) · [**Web Showcase (EN)**](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) · [Веб-витрина (RU)](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/) · [Release v0.14.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.14.0-alpha) · [Status & Roadmap](docs/en/roadmap.md) · [First Start Guide](docs/en/first-start.md) · [Partners & Sponsors](#partners-and-sponsors)

> **Alpha · v0.14.0-alpha (published November 11, 2026; status & roadmap snapshot as of November 12, 2026).** The primary installer package `GoldenBreeze-FirstInstall-0.14.0-alpha.exe` (`stable` channel, Windows x64) is published in Releases and delivers the capabilities of the `0.13.0-alpha`–`0.14.0-alpha` cycles. On the dedicated Windows x64 acceptance rig, clean installation, `0.13.0-alpha → 0.14.0-alpha` auto-update with data preservation and rollback verification, FTMO MT5 connection, Agent Studio configuration publish/activation, and a full demo trade cycle on `XAUUSD` with risk checks and `trailing-stop` management have been verified on an `FTMO-Demo` account (live trading acceptance on a `Real` account is not claimed).

---

## Product Web Showcase (GitHub Pages)

A bilingual responsive static product showcase is published from `main:/docs`:
- **English Web Showcase:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/)
- **Russian Web Showcase:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/)
- Overview of the multi-agent trading platform architecture, 5-step trading workflow, and an interactive Control Desk workspace preview with demonstration data;
- Interactive capability status matrix (`In Release v0.14`, `Delivered in 0.13–0.14 / Demo Acceptance Verified`, `Planned`, `Deferred`);
- Direct `FirstInstall` download links, one-click `SHA-256` copy, and PowerShell verification commands;
- User documentation in English: [Status & Roadmap (`docs/en/roadmap.md`)](docs/en/roadmap.md) · [Installation & First Start (`docs/en/first-start.md`)](docs/en/first-start.md);
- Canonical repository maintenance & Pages notes (in Russian): [`docs/github-pages.md` (RU)](docs/github-pages.md) · [`docs/CONTENT-MAINTENANCE.md` (RU)](docs/CONTENT-MAINTENANCE.md).

---

## Available in Release v0.14.0-alpha (`stable` channel)

- **Trading Agent Control Desk & Agent Studio.** Agent profiles, assignment of trading instrument, account, risk boundaries, and strategy version, strict parameter comparison when applying a Studio draft, recording of "Behavior Review" results (including `+sourcefree` versions), immediate market study over closed broker bars even when the market is closed, a **"Market State"** block aligned to the official FTMO schedule, pre-start readiness verification, and desktop window scaling (`25%–500%`) with responsive narrow-window layout (`<= 700px`). Starting and stopping a trading session are distinct explicit user actions; during an active session, the agent manages positions within defined risk limits.
- **Accounts, Prop Firms & MetaTrader 5 (MT5) Trading Integration.** Supports both `Demo` and `Real` accounts via **MT5**, neutral prop-firm and account cards (with GoatFunded explicitly marked as "Support in development"), a unified sign-in window mechanism, **"Connect now"** toggle and automatic adapter selection by platform family (`MT5`/`MT4`), automatic symbol addition to MT5 "Market Watch" and background broker clock verification, dedicated MT5 terminal auto-provisioning with non-activating window placement and automatic termination on disconnect/exit, and verification of account identity/type, auto-trading permissions, and risk boundaries.
- **Agent Chat, Knowledge Library, Strategy Generation & Model Selection.** The "Agent Chat" workspace for trading and research tasks runs the main agent via both **Claude CLI** and **Codex CLI (ChatGPT sign-in without an API key)** with formatted Markdown responses, conversation management and per-chat draft isolation, selection of AI model and reasoning level (`thinking effort`) with requested vs. actual model display, multimodal attachments (`PNG`/`JPG`, text/tables, `PDF`, `DOCX`, and isolated frame extraction from short video clips), a built-in **Knowledge Library** with source/page citations, live **web search**, a **child researcher subagent** in code, and direct in-chat Python strategy generation with isolated synthetic-bar verification and **"Add to catalog"** registration for Agent Studio.
- **`FirstInstall` Installer & Direct Auto-Update (`stable`).** The installer bundles its own Windows x64 runtime and does not require a separate Python installation. Updates are delivered on button click from a dedicated HTTPS update server with **Ed25519** cryptographic manifest signature verification, installed build revision stamp check (`gb-build-stamp.json`), child process tree termination (Job Object), preservation of agent profiles and accounts, verified recovery rollback, and short anonymized update failure reports.
- **Trilingual Interface (`RU` · `UA` · `EN`).** Switching between Russian, Ukrainian, and English works across the Control Desk, Agent Studio, chat, memory, prop-firm cards, and update notifications, including completed `RU`/`UA`/`EN` localization of the **"FTMO Conditions"** card, **"Terminal Reconciliation"** block, account registration messages, and human-readable readiness statuses in the Control Desk.

> **Interactive Control Desk Preview:** the [English Web Showcase](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) features an interactive demonstration layout of the Control Desk workspace with trading agent profile cards (`XAUUSD` / `EURUSD`), price chart, account and risk panel, decision log, and protective stop management (demonstration data).

---

## Delivered in Cycle 0.13–0.14-alpha & Live Acceptance Status (v0.14.0-alpha, snapshot as of November 12, 2026)

Installation, auto-update, and automated CI tests confirm build delivery, whereas live functional acceptance is tracked with explicit environment and account-type boundaries. Included in the published `v0.14.0-alpha` (`stable`) installer and verified on the dedicated Windows x64 acceptance rig:

1. **Knowledge Library, Multimodal Attachments, Web Search & Child Researcher Agent in Chat:**
   - Attaching screenshots and charts, text and tabular files, `PDF` (with text layer), `DOCX`, and short video clips (up to 10 MB and 10 minutes — extracting frames in an isolated process without audio recognition) to chat messages;
   - Full operation of the main agent via both **Claude CLI** and **Codex CLI (ChatGPT sign-in without an API key)** with formatted Markdown responses (live main chat dialogue via `claude_cli` verified in the desktop UI during `v0.14.0-alpha` acceptance);
   - Built-in **Knowledge Library** (storing books, documents, and notes, searching and reading with source and page/section citations), live **web search** recording URLs and access timestamps, and delegation of research tasks to a **child researcher subagent** (implemented in code with access strictly limited to the Knowledge Library and web search and no access to trading accounts; separate live rig verification of researcher delegation remains a follow-up item).
2. **In-Chat Strategy Code Generation, Isolated Verification & Studio Catalog Registration:**
   - The main agent writes and refines Python strategy code directly in chat; the application validates the code against a construct whitelist and executes it in an isolated memory-limited process on synthetic bars (verifying executability and core invariants rather than running a deep historical backtest);
   - The chat response renders a strategy card with code preview and an **"Add to catalog"** button, making the registered version immediately selectable in Agent Studio without manual file copying.
3. **Closed-Market Analysis, Broker Timezones, Control Desk & MT5 Terminal Lifecycle:**
   - Immediate analysis of closed bars via **"Study Market"** when the market is closed without waiting for a live tick, history persistence across regular daily and weekend session breaks, a **"Market State"** block following the official FTMO schedule, and weekly bar dating aligned to verified server timezone (including DST transitions); bars without verified UTC are never passed into the trading pipeline;
   - Automatic addition of the trading symbol to MT5 "Market Watch" while awaiting history synchronization, background verification of broker server time upon account connection and agent selection, and explicit explanations of waiting reasons in Control Desk readiness checks;
   - **"Connect now"** toggle and automatic adapter selection by platform family (`MT5`/`MT4`) when adding an account, dedicated MT5 terminal auto-provisioning (`[Experts]` Algo Trading enabled and standard operator workspace seeded) with non-activating window placement and automatic termination upon application exit or account disconnect, verification of the installed build revision stamp, `RU`/`UA`/`EN` localization of the **"FTMO Conditions"** card and **"Terminal Reconciliation"** block, replacement of internal codes with human-readable statuses in the Control Desk, and strict parameter comparison when applying a Studio draft.
4. **Diagnostic Demo Route in Broker Mode & Completed Live Acceptance on FTMO MT5 Demo:**
   - For the diagnostic verification path (manually enabling execution in Diagnostics, diagnostic run, and acceptance `BUY`/`SELL` trades), Studio agents are supported in broker mode with fresh dual verification of the account's demo status from the MT5 terminal upon activation and before every order submission (this diagnostic test route operates strictly on demo accounts and rejects real accounts with `account_not_demo`, while general platform support for both `Demo` and `Real` accounts remains intact);
   - On the dedicated Windows x64 acceptance rig, live end-to-end verification of `v0.14.0-alpha` passed for:
     - **Clean installation, update & rollback:** cold install of `GoldenBreeze-FirstInstall-0.14.0-alpha.exe`, clean process-tree shutdown (`0` residual processes), live update `0.13.0-alpha → 0.14.0-alpha` preserving database, strategies, and FTMO session, and live recovery rollback verification (`rolled_back`);
     - **FTMO connection, risk gate & Agent Studio:** live `FTMO-Demo` MT5 connection, `prop-policy` v2 verification, negative risk gate rejection (`HTTP 422` when agent limits are weaker than program rules), and Studio configuration creation, validation, `v1` publication, and activation (**"Apply configuration"**);
     - **Full demo trade cycle on `XAUUSD` (`M5`):** `Acceptance Gateway Cycle` (`BUY 0.01 XAUUSD` with `PropGuard`, `exit_cost_reserve`, server `SL`/`TP` confirmation, position close, deal reconciliation, and zero residual position check `0/0`), `ExecutionDiagnosticLoop` (`5/5` scenarios passed, including live server `trailing-stop` modification via `TRADE_ACTION_SLTP`), ordinary strategy signal (`+sourcefree`) + LLM pass (`DRY_RUN_ACCEPTED`), and clean session stop (`0` open positions, `0` active orders).
   - Separate follow-up verification of child researcher delegation on the rig and remaining manual Figma screen comparisons continue independently.

Completed live trading acceptance on a real account (`Real`) is not claimed.

---

## Where We Are Heading (Planned & Deferred)

- **Planned — Multiple Trading Executors & Portfolio Management:** scaling multi-agent trading — parallel coordination of specialized trading agents across multiple instruments and sessions, capital allocation, enforcement of portfolio-wide prop-firm risk rules, end-to-end drawdown control, and market regime analytics.
- **Planned — Platform Catalog & Dedicated TradeLocker Integration:** expanding the unified registry of prop-firm and platform adapters; in the current release, **MetaTrader 5 (MT5)** is the active trading connector and **FTMO** is the currently supported prop-firm integration, while **TradeLocker** integration is scheduled as a dedicated planned milestone.
- **Planned — Saved Trading Agent Workflows:** repeatable multi-step routines for readiness checks, market study, enforcement of verified prop-firm rules, and scheduled risk control.
- **Design Stage — Licensing & Access Tiers:** architectural design of access keys and closed beta testing modes (`Free` / `Pro` / `Tester`), device binding, and capability tier separation without mixing licensing with trading execution permissions (plans, pricing, and commercial sales terms are not yet approved).
- **Deferred Without Blocking the Current Path:** an expanded Studio with a standalone built-in code editor for manual programming and a custom deep historical backtesting engine with dataset management, as well as purchasing a paid Windows **Authenticode** publisher certificate and a dedicated custom domain (deferred until the product reaches profitability).

[Detailed Status & Roadmap (`docs/en/roadmap.md`) →](docs/en/roadmap.md)

---

## Download & Get Started (Windows x64)

Current pre-release: **[Golden Breeze v0.14.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.14.0-alpha)** (for `alpha` pre-releases, use the direct tag link or the [Releases](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases) page, because GitHub's `/releases/latest` endpoint excludes pre-releases).

- **Download for Windows (FirstInstall):** [`GoldenBreeze-FirstInstall-0.14.0-alpha.exe`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/GoldenBreeze-FirstInstall-0.14.0-alpha.exe) (`406,722,870` bytes / `387.9 MiB`)
- **Checksum file:** [`GoldenBreeze-FirstInstall-0.14.0-alpha.exe.sha256`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/GoldenBreeze-FirstInstall-0.14.0-alpha.exe.sha256)
- **SHA-256 value:** `f166f00d4bbfd5e299c7f52e9ba3b51c3c208ea1d9f3b93dbc039806e113d69e`
- **Update manifest & signature:** [`build-manifest.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/build-manifest.json) · [`first-install.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/first-install.json) · [`first-install.json.sig`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/first-install.json.sig)

Verify `SHA-256` in Windows PowerShell before running (confirms exact byte-for-byte match between the downloaded file and the trusted release artifact):

```powershell
Get-FileHash .\GoldenBreeze-FirstInstall-0.14.0-alpha.exe -Algorithm SHA256
```

- **Source code** archives automatically generated by GitHub contain only the files of this showcase repository and are not the application installer.
- The `.exe` binary is not signed with a paid Windows **Authenticode** certificate, so Windows SmartScreen may request manual confirmation on first install (after verifying `SHA-256`, click *"More info" → "Run anyway"*).
- After initial installation, `stable` channel updates are delivered over HTTPS with **Ed25519** cryptographic manifest signature verification via the **"Update now"** button without requiring GitHub access.
- Installing and launching the application never starts trading or opens orders automatically: a trading session is started explicitly by the user from the Control Desk.

[Detailed Installation & First Start Guide (`docs/en/first-start.md`) →](docs/en/first-start.md)

---

## Partners and Sponsors

We collaborate around concrete deliverables of the multi-agent trading platform:
- **Trading Integrations & Market Data:** connectors to trading platforms (including the planned TradeLocker integration), broker and prop-firm integrations, and market data feeds;
- **Independent Acceptance & Pilot Testing:** verifying trading agent workflows on Windows x64 systems, validating prop-firm risk rules, and evaluating Control Desk usability;
- **Targeted Sponsorship of Roadmap Modules:** accelerating multi-agent portfolio coordination and risk control, new trading adapters, the Knowledge Library with specialized subagents, and in-chat strategy engineering;
- **Educational & Methodological Materials:** documentation on configuring trading agents, risk governance, and market regime analysis.

Support is tied to agreed deliverables and verifiable product outcomes.

[Discuss partnership or sponsorship in GitHub Issues →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

---

## Feedback

[Ask a question or report an issue in GitHub Issues →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

Please include the exact application version (`0.14.0-alpha`), expected behavior, and actual behavior. Attach screenshots without passwords, API keys, or account numbers.

*Historical analysis results or performance on a demo account do not promise similar outcomes on a real account. Golden Breeze does not guarantee profitability.*

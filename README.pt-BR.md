# Golden Breeze

<p align="center">
  <a href="README.md">English</a> · <a href="README.uk.md">Українська</a> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a> · <strong>Português (Brasil)</strong> · <a href="README.zh-CN.md">简体中文</a>
</p>

![Golden Breeze — Plataforma de trading multiagente](assets/brand/golden-breeze-banner-en.svg)

**Plataforma de trading multiagente: trabalho colaborativo de agentes de IA especializados ao longo de todo o fluxo operacional de negociação — desde a análise de mercado e decisões operacionais até a execução, gestão de posições e controle de risco sob governança do usuário.**

O Golden Breeze foi desenvolvido para o trabalho colaborativo de agentes de IA especializados em trading. A partir de um único Painel de Controle (Control Desk), o usuário governa os agentes, suas tarefas e o acesso às contas de negociação conectadas: da análise de mercado, tomada de decisões, gestão de posições e controle de risco à pesquisa, engenharia de estratégias, verificação isolada e catálogo versionado de estratégias.

[**Baixar para Windows (v0.12.0-alpha)**](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe) · [**Vitrine Web (EN)**](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) · [Vitrine Web (RU)](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/) · [Lançamento v0.12.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.12.0-alpha) · [Status e Roadmap (em inglês)](docs/en/roadmap.md) · [Guia de Primeiro Início (em inglês)](docs/en/first-start.md) · [Parceiros e patrocinadores](#parceiros-e-patrocinadores)

> **Alpha · v0.12.0-alpha (publicado em 17 de outubro de 2026; panorama de status e roadmap em 28 de outubro de 2026).** O pacote de instalação principal `GoldenBreeze-FirstInstall-0.12.0-alpha.exe` (canal `stable`, Windows x64) está publicado em Releases. A publicação do instalador confirma a entrega da compilação, enquanto as funcionalidades dos ciclos `0.13.0-alpha`–`0.14.0-alpha` estão integradas à ramificação principal de desenvolvimento e passam por homologação funcional em tempo real de ponta a ponta em uma bancada dedicada de testes Windows x64 antes do próximo lançamento público.

---

## Vitrine Web do Produto (GitHub Pages)

Uma vitrine web estática, responsiva e bilíngue do produto está publicada a partir de `main:/docs`:
- **Vitrine Web em inglês:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/)
- **Vitrine Web em russo:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/)
- Visão geral da arquitetura da plataforma de trading multiagente, fluxo operacional de trading em 5 etapas e prévia interativa do ambiente de trabalho do Painel de Controle (Control Desk) com dados de demonstração;
- Matriz interativa de status de capacidades (`Na versão v0.12`, `Implementado em 0.13–0.14 / Em homologação`, `Planejado`, `Adiado`);
- Links diretos para download do `FirstInstall`, cópia em um clique do `SHA-256` e comandos de verificação em PowerShell;
- Documentação do usuário em inglês: [Status e Roadmap (`docs/en/roadmap.md`, em inglês)](docs/en/roadmap.md) · [Instalação e Primeiro Início (`docs/en/first-start.md`, em inglês)](docs/en/first-start.md);
- Notas canônicas de manutenção do repositório e do Pages (em russo): [`docs/github-pages.md` (RU)](docs/github-pages.md) · [`docs/CONTENT-MAINTENANCE.md` (RU)](docs/CONTENT-MAINTENANCE.md).

---

## Disponível na versão v0.12.0-alpha (canal stable)

- **Painel de Controle de agentes de trading (Control Desk) e Estúdio de Agentes (Agent Studio).** Perfis de agentes, atribuição de instrumento operacional, conta, limites de risco e versão da estratégia, registro dos resultados de "Revisão de Comportamento" (incluindo versões com status `+sourcefree`), estudo de mercado sobre barras fechadas da corretora e verificação de prontidão pré-início. O início e a interrupção de uma sessão de trading são ações explícitas e distintas do usuário; durante uma sessão ativa, o agente gerencia posições dentro dos limites de risco definidos.
- **Contas, empresas proprietárias (prop firms) e integração operacional com MetaTrader 5 (MT5).** Suporte a contas demo (`Demo`) e reais (`Real`) via **MT5**, cartões neutros de prop firms e de contas, mecanismo unificado de janela de login, verificação de identidade e tipo de conta, permissões de negociação automatizada e limites de risco.
- **Chat do agente, contexto e seleção de modelos.** O espaço de trabalho "Chat do agente" para tarefas operacionais e de pesquisa oferece criação, renomeação, agrupamento, arquivamento e restauração de conversas, isolamento de rascunhos por chat, seleção de modelo de IA e nível de raciocínio (`thinking effort`) conforme as capacidades do provedor de IA conectado, além de exibição do modelo solicitado versus modelo real nos detalhes de execução (na versão publicada `v0.12.0-alpha`, o chat principal do agente opera via **Claude CLI**, enquanto o login com **Codex CLI / ChatGPT** em Configurações já é suportado e se torna um mecanismo completo de chat principal no ciclo `0.13–0.14-alpha`).
- **Instalador `FirstInstall` e atualização automática direta (`stable`).** O instalador inclui seu próprio runtime para Windows x64 e não exige uma instalação separada do Python. As atualizações são entregues com um clique de botão a partir de um servidor HTTPS dedicado com verificação criptográfica de assinatura de manifesto **Ed25519**, encerramento de árvore de processos filhos (Job Object), preservação de perfis de agentes e de contas, além de relatórios curtos e anonimizados de falhas de atualização.
- **Interface trilíngue (`RU` · `UA` · `EN`).** A alternância entre russo, ucraniano e inglês funciona no Painel de Controle, no Estúdio de Agentes, no chat, na memória, nos cartões de prop firms e nas notificações de atualização (na compilação publicada `v0.12.0-alpha`, algumas mensagens de registro de conta em Configurações e alguns rótulos no cartão de conta FTMO e na tela de verificação inicial ainda apareciam em russo; sua localização e a substituição de códigos brutos de status foram concluídas no ciclo `0.13–0.14-alpha`).

> **Prévia interativa do Painel de Controle:** a [Vitrine Web em inglês](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) apresenta um modelo interativo de demonstração do espaço de trabalho do Painel de Controle com cartões de perfil de agentes de trading (`XAUUSD` / `EURUSD`), gráfico de preços, painel de conta e risco, registro de decisões e gerenciamento de stop de proteção (dados de demonstração).

---

## Implementado após a v0.12.0-alpha e em processo de homologação (ciclo 0.13–0.14-alpha, panorama em 28 de outubro de 2026)

A instalação, a atualização automática e os testes automatizados de CI confirmam a entrega da compilação, enquanto a homologação funcional em tempo real é acompanhada separadamente. Integrado à ramificação principal de desenvolvimento após a `v0.12.0-alpha` e atualmente passando por verificação em etapas na bancada dedicada de testes Windows x64:

1. **Biblioteca de Conhecimento, anexos multimodais, busca web e subagente pesquisador secundário no Chat:**
   - Anexo de capturas de tela e gráficos, arquivos de texto e tabelas, `PDF` (com camada de texto), `DOCX` e clipes curtos de vídeo (até 10 MB e 10 minutos — com extração de quadros em processo isolado sem reconhecimento de áudio) às mensagens do chat;
   - Operação completa do agente principal tanto via **Claude CLI** quanto via **Codex CLI (login com ChatGPT sem chave de API)** com respostas formatadas em Markdown;
   - **Biblioteca de Conhecimento** integrada (armazenamento de livros, documentos e notas, busca e leitura com citações de fonte e página/seção), **busca web** ao vivo com registro de URLs e carimbos de data/hora de acesso, e delegação de tarefas de pesquisa a um **subagente pesquisador secundário** (implementado em código com acesso estritamente restrito à Biblioteca de Conhecimento e à busca web, sem acesso a contas de negociação; a validação de homologação ao vivo da delegação ao pesquisador na bancada de testes ainda está pendente).
2. **Geração de código de estratégia no chat, verificação isolada e registro no catálogo do Estúdio:**
   - O agente principal escreve e aprimora código de estratégia em Python diretamente no chat; a aplicação valida o código em relação a uma lista de permissões de estruturas (whitelist) e o executa em um processo isolado com limite de memória sobre barras sintéticas (verificando a capacidade de execução e os invariantes centrais, em vez de realizar um backtest histórico profundo);
   - A resposta do chat exibe um cartão de estratégia com pré-visualização do código e o botão **"Adicionar ao catálogo"**, tornando a versão registrada imediatamente selecionável no Estúdio de Agentes sem a necessidade de copiar arquivos manualmente.
3. **Análise com mercado fechado, fusos horários da corretora, Painel de Controle e ciclo de vida do terminal MT5:**
   - Análise imediata de barras fechadas pelo botão **"Estudar Mercado"** quando o mercado está fechado, sem aguardar um tick em tempo real; persistência de histórico através de intervalos de sessão diários e de finais de semana; bloco **"Estado do Mercado"** seguindo a programação oficial da FTMO e datação semanal de barras alinhada ao fuso horário verificado do servidor (incluindo transições de horário de verão/inverno); barras sem UTC verificado nunca são repassadas ao fluxo de negociação;
   - Adição automática do símbolo de negociação ao "Market Watch" (Observação de Mercado) do MT5 enquanto aguarda a sincronização do histórico, verificação em segundo plano da hora do servidor da corretora no momento da conexão da conta e seleção do agente, e explicações explícitas dos motivos de espera nas verificações de prontidão do Painel de Controle;
   - Seletor **"Conectar agora"** e seleção automática de adaptador por família de plataforma (`MT5`/`MT4`) ao adicionar uma conta, posicionamento de janela sem ativação de foco e encerramento automático do terminal MT5 dedicado ao sair da aplicação ou desconectar a conta, verificação do carimbo de revisão da compilação instalada, localização em `RU`/`UA`/`EN` do cartão **"Condições FTMO"** e do bloco **"Reconciliação com o Terminal"**, substituição de códigos internos por status legíveis no Painel de Controle e comparação estrita de parâmetros ao aplicar um rascunho do Estúdio.
4. **Rota demo de diagnóstico no modo broker e status atual da homologação em tempo real:**
   - Para o fluxo de verificação diagnóstica (habilitação manual da execução em Diagnósticos, execução diagnóstica e ordens de homologação `BUY`/`SELL`), foi adicionado suporte a agentes do Estúdio em modo broker com dupla verificação recente do status demo da conta a partir do terminal MT5 no momento da ativação e antes de cada envio de ordem (essa rota de teste diagnóstico opera estritamente em contas demo e rejeita contas reais, enquanto o suporte geral da plataforma a contas `Demo` e `Real` permanece inalterado);
   - A homologação funcional de ponta a ponta em tempo real em **111 verificações** na bancada de testes dedicada **ainda não está concluída** (na última execução registrada no candidato anterior de homologação, **84 de 111** verificações foram aprovadas, com **4** falhas, **10** etapas dependentes não executadas, **6** revisões manuais de layout no Figma necessárias e **7** verificações externas pendentes): no candidato anterior, a ativação manual da execução, a execução diagnóstica e o ciclo de ordens de verificação (`BUY`/`SELL`, `trailing-stop` e conciliação de posição residual zero) permaneceram pendentes; as correções para essas etapas já foram integradas à ramificação principal para o próximo candidato de bancada, enquanto a verificação em tempo real do subagente pesquisador secundário e a comparação manual de 6 telas com os padrões do Figma continuam pendentes.

A homologação concluída de negociação ao vivo em conta real (`Real`) não é reivindicada.

---

## Para onde estamos indo (Planejado e adiado)

- **Planejado — Múltiplos executores de negociação e gestão de portfólio:** escalabilidade do trading multiagente — coordenação paralela de agentes de negociação especializados em múltiplos instrumentos e sessões, alocação de capital, aplicação de regras de risco de prop firms no nível do portfólio, controle de drawdown de ponta a ponta e análise de regimes de mercado.
- **Planejado — Catálogo de plataformas e integração dedicada do TradeLocker:** expansão do registro unificado de adaptadores de plataformas e prop firms; na versão atual, o **MetaTrader 5 (MT5)** é o conector de negociação ativo e a **FTMO** é a integração de prop firm suportada no momento, enquanto a integração com o **TradeLocker** está agendada como um marco planejado dedicado.
- **Planejado — Fluxos de trabalho salvos de agentes de trading:** rotinas de múltiplas etapas repetíveis para verificações de prontidão, estudo de mercado, aplicação de regras verificadas de prop firms e controle agendado de risco.
- **Fase de projeto — Estrutura de licenciamento e níveis de acesso:** desenho arquitetônico de chaves de acesso e modos de teste beta fechado (`Free` / `Pro` / `Tester`), vinculação a dispositivos e separação de níveis de capacidade sem misturar licenciamento com permissões de execução de ordens (planos, preços e termos comerciais de venda ainda não foram aprovados).
- **Adiado sem bloquear o caminho atual:** um Estúdio ampliado com editor de código autônomo integrado para programação manual e um motor próprio de backtest histórico profundo com gerenciamento de conjuntos de dados, bem como a aquisição de um certificado pago de editor Windows **Authenticode** e um domínio personalizado dedicado (adiados até que o produto atinja a lucratividade).

[Status detalhado e Roadmap (`docs/en/roadmap.md`, em inglês) →](docs/en/roadmap.md)

---

## Baixar e começar a usar (Windows x64)

Pré-lançamento atual: **[Golden Breeze v0.12.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.12.0-alpha)** (para pré-lançamentos `alpha`, use o link direto da tag ou a página de [Releases](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases), pois o endpoint `/releases/latest` do GitHub desconsidera pré-lançamentos).

- **Download para Windows (FirstInstall):** [`GoldenBreeze-FirstInstall-0.12.0-alpha.exe`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe) (`383,300,782` bytes / `365.5 MiB`)
- **Arquivo de checksum:** [`GoldenBreeze-FirstInstall-0.12.0-alpha.exe.sha256`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe.sha256)
- **Valor SHA-256:** `d4546bc1fe718020f78315bbe98e4b232db044fb80bdb1061f1d2fe44ffd60a2`
- **Manifesto de atualização e assinatura:** [`build-manifest.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/build-manifest.json) · [`first-install.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/first-install.json) · [`first-install.json.sig`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/first-install.json.sig)

Verifique o `SHA-256` no Windows PowerShell antes de executar (confirma a correspondência exata byte a byte entre o arquivo baixado e o artefato confiável do lançamento):

```powershell
Get-FileHash .\GoldenBreeze-FirstInstall-0.12.0-alpha.exe -Algorithm SHA256
```

- Os arquivos de código-fonte (**Source code**) gerados automaticamente pelo GitHub contêm apenas os arquivos deste repositório de vitrine e não constituem o instalador do aplicativo.
- O arquivo executável `.exe` não é assinado com um certificado comercial Windows **Authenticode**; por isso, o Windows SmartScreen pode solicitar confirmação manual na primeira instalação (após verificar o `SHA-256`, clique em *"Mais informações" → "Executar assim mesmo"*).
- Após a instalação inicial, as atualizações do canal `stable` são entregues via HTTPS com verificação criptográfica de assinatura de manifesto **Ed25519** pelo botão **"Atualizar agora"**, sem necessidade de acesso ao GitHub.
- A instalação e a inicialização do aplicativo nunca iniciam negociações ou abrem ordens automaticamente: uma sessão de trading é iniciada explicitamente pelo usuário a partir do Painel de Controle.

[Guia detalhado de instalação e primeiro início (`docs/en/first-start.md`, em inglês) →](docs/en/first-start.md)

---

## Parceiros e patrocinadores

Colaboramos em torno de entregas concretas da plataforma de trading multiagente:
- **Integrações de negociação e dados de mercado:** conectores para plataformas de trading (incluindo a integração planejada do TradeLocker), integrações com corretoras e prop firms, e feeds de cotações de mercado;
- **Homologação independente e testes-piloto:** verificação do funcionamento dos agentes de trading em sistemas Windows x64, validação das regras de risco de prop firms e avaliação da usabilidade do Painel de Controle;
- **Patrocínio direcionado de módulos do roadmap:** aceleração da coordenação de múltiplos agentes em portfólios e controle de risco, novos adaptadores de negociação, Biblioteca de Conhecimento com subagentes especializados e engenharia de estratégias no chat;
- **Materiais educativos e metodológicos:** documentação sobre configuração de agentes de trading, governança de risco e análise de regimes de mercado.

O apoio está vinculado a entregas acordadas e resultados verificáveis no produto.

[Discutir parceria ou patrocínio no GitHub Issues →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

---

## Feedback

[Faça uma pergunta ou relate um problema no GitHub Issues →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

Por favor, inclua a versão exata do aplicativo (`0.12.0-alpha`), o comportamento esperado e o comportamento real. Anexe capturas de tela sem senhas, chaves de API ou números de conta.

*Resultados de análises históricas ou desempenho em conta demo não prometem resultados semelhantes em conta real. O Golden Breeze não garante lucratividade.*

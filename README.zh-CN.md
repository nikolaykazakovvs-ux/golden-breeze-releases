# Golden Breeze

<p align="center">
  <a href="README.md">English</a> · <a href="README.uk.md">Українська</a> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <strong>简体中文</strong>
</p>

![Golden Breeze — 多智能体交易平台](assets/brand/golden-breeze-banner-en.svg)

**多智能体交易平台：在用户治理与监管下，专业 AI 智能体跨越完整交易工作流协同作业——从市场分析、交易决策到订单执行、持仓管理及风险控制。**

Golden Breeze 专为交易领域中专业 AI 智能体的协同作业而打造。用户可通过统一的控制台（Control Desk）全面治理各个智能体、分配任务并管理已连接交易账户的访问权限：涵盖从市场分析、决策制定、持仓管理与风险控制，到深度研究、策略工程、隔离验证以及版本化策略目录的完整流程。

[**下载 Windows 版 (v0.12.0-alpha)**](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe) · [**网页展台 (英文)**](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) · [网页展台 (俄文)](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/) · [版本发布 v0.12.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.12.0-alpha) · [状态与路线图（英文）](docs/en/roadmap.md) · [快速上手指南（英文）](docs/en/first-start.md) · [合作伙伴与赞助商](#合作伙伴与赞助商)

> **Alpha · v0.12.0-alpha（发布于 2026 年 10 月 17 日；状态与路线图快照截至 2026 年 10 月 28 日）。** 主安装程序包 `GoldenBreeze-FirstInstall-0.12.0-alpha.exe`（`stable` 稳定通道，Windows x64）已在 Releases 中发布。发布安装包确认了软件构建版本的交付，而来自 `0.13.0-alpha`–`0.14.0-alpha` 开发周期的功能已合并至主开发分支，目前正在专用 Windows x64 验收测试机上进行端到端实时功能验收，为下一个公开发布版本做准备。

---

## 产品网页展台（GitHub Pages）

基于 `main:/docs` 构建的双语响应式静态产品网页展台已上线：
- **英文网页展台：** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/)
- **俄文网页展台：** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/)
- 介绍多智能体交易平台架构、5 步交易工作流逻辑，以及包含演示数据的交互式控制台（Control Desk）工作区预览；
- 交互式功能状态矩阵（“已在 v0.12 发布版提供”、“已在 0.13–0.14 实现 / 验收中”、“已计划”、“已延后”）；
- `FirstInstall` 安装包直接下载链接、`SHA-256` 一键复制及 PowerShell 校验命令；
- 英文用户文档：[状态与路线图（英文，`docs/en/roadmap.md`）](docs/en/roadmap.md) · [安装与首次启动（英文，`docs/en/first-start.md`）](docs/en/first-start.md)；
- 规范的代码库维护与 GitHub Pages 说明（俄文）：[`docs/github-pages.md`（俄文）](docs/github-pages.md) · [`docs/CONTENT-MAINTENANCE.md`（俄文）](docs/CONTENT-MAINTENANCE.md)。

---

## v0.12.0-alpha 发布版可用功能（`stable` 通道）

- **交易智能体控制台与智能体工作室（Control Desk & Agent Studio）。** 提供智能体配置文件、交易品种分配、账户与风险边界设定以及策略版本选择，记录“行为审查”（Behavior Review）结果（包括 `+sourcefree` 版本），基于经纪商已闭合 K 线进行市场分析，并在启动前执行就绪状态检查。交易时段的启动与停止为明确独立的用户操作；在活跃时段内，智能体严格在设定的风险限额内管理持仓。
- **账户、自营交易公司（Prop Firm）与 MetaTrader 5 (MT5) 交易接入。** 支持通过 **MT5** 连接模拟账户（`Demo`）与实盘账户（`Real`），提供中立的自营公司与账户卡片、统一登录弹窗机制、验证账户身份/类型、自动交易权限检查以及风险边界约束。
- **智能体对话、上下文与模型选择。** 用于交易与研究任务的“智能体对话”（Agent Chat）工作区支持创建、重命名、分组、归档及恢复对话，实现跨对话草稿隔离，根据已接入 AI 服务商的能力选择 AI 模型与思考深度（`thinking effort`），并在执行详情中显示所请求的模型与实际调用的模型（在已发布的 `v0.12.0-alpha` 中，主智能体对话通过 **Claude CLI** 运行，而“设置”中的 **Codex CLI / ChatGPT 登录** 已受支持，并在 `0.13–0.14-alpha` 周期中升级为完整的主对话引擎）。
- **`FirstInstall` 独立安装程序与直接自动更新（`stable`）。** 安装包内置独立的 Windows x64 运行环境，无需单独安装 Python。只需点击按钮即可从专用 HTTPS 更新服务器获取更新，更新包附带 **Ed25519** 加密清单签名校验、子进程树安全终止（Job Object）、保留智能体配置与账户数据，并在更新失败时生成简明匿名故障报告。
- **三语界面（`RU` · `UA` · `EN`）。** 支持在俄语、乌克兰语和英语之间无缝切换，覆盖控制台、智能体工作室、对话、记忆、自营公司卡片及更新通知（在已发布的 `v0.12.0-alpha` 版本中，“设置”中个别账户注册提示、FTMO 账户卡片和启动检查界面上的少量文本仍显示为俄语；这些界面的多语言本地化及将原始状态码替换为人性化提示已在 `0.13–0.14-alpha` 周期中完成）。

> **交互式控制台预览：** [英文网页展台](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) 提供了控制台工作区的交互式演示界面，包含交易智能体配置文件卡片（`XAUUSD` / `EURUSD`）、价格走势图、账户与风险面板、决策日志以及保护性止损管理（均为演示数据）。

---

## v0.12.0-alpha 之后已实现且正在验收的功能（0.13–0.14-alpha 周期，快照截至 2026 年 10 月 28 日）

安装包交付、自动更新和自动化 CI 测试用于确认构建版本的交付，而实时功能验收则进行独立跟踪。在 `v0.12.0-alpha` 之后已集成至主开发分支、目前正在专用 Windows x64 验收测试机上接受分阶段验证的功能包括：

1. **知识库、多模态附件、网络搜索与对话中的子研究员智能体：**
   - 支持在对话消息中附加屏幕截图与图表、文本与表格文件、带有文本层的 `PDF`、`DOCX` 以及短视频片段（不超过 10 MB 且时长在 10 分钟以内——在隔离进程中提取视频帧，不进行音频识别）；
   - 主智能体支持通过 **Claude CLI** 和 **Codex CLI（通过 ChatGPT 登录，无需 API Key）** 完整运行，并具备格式化 Markdown 渲染能力；
   - 内置**知识库**（存储书籍、文档和笔记，支持按来源和页码/章节引文进行检索与阅读）、记录 URL 和访问时间戳的实时**网络搜索**，以及将研究任务委派给**子研究员智能体**（代码中已实现，其访问权限严格受限于知识库和网络搜索，无权访问交易账户；在测试机上对研究员委派的实时验收测试尚待完成）。
2. **对话内策略代码生成、隔离验证与工作室目录注册：**
   - 主智能体可直接在对话中编写和优化 Python 策略代码；应用程序根据语法白名单校验代码，并在内存受限的隔离进程中基于合成 K 线执行验证（旨在验证代码可执行性与核心不变式，而非执行深度历史回测）；
   - 对话回复中渲染策略卡片，提供代码预览及**“添加到目录”**按钮，注册成功后即可在智能体工作室中直接选用该版本，无需手动复制文件。
3. **闭市分析、经纪商时区、控制台与 MT5 终端生命周期管理：**
   - 闭市期间通过**“研究市场”**按钮立即分析已闭合 K 线，无需等待实时 Tick 报价推送；历史数据在常规日内休市和周末休市期间保持持久化；遵循 FTMO 官方交易时间表的**“市场状态”**模块，以及按已验证的服务器时区对周 K 线进行日期对齐（包括夏令时/冬令时转换）；未经确认 UTC 时间戳的 K 线绝不会传入交易管线；
   - 等待历史数据同步期间自动将交易品种添加至 MT5“市场报价”窗口；在连接账户和选择智能体时后台预热验证经纪商服务器时间；在控制台就绪检查中对等待原因给出明确说明；
   - 添加账户时提供**“立即连接”**开关并根据平台系列（`MT5`/`MT4`）自动匹配适配器；窗口采用不激活焦点的放置方式；在退出程序或断开账户连接时自动安全终止专用 MT5 终端；校验已安装构建版本的修订版标识戳；完成**“FTMO 交易条件”**卡片和**“终端核对”**模块的 `RU`/`UA`/`EN` 本地化；在控制台中使用人类可读状态替代内部代码；并在工作室应用草稿时执行严格的参数对比。
4. **经纪商模式下的诊断 Demo 路由与当前实时验收状态：**
   - 针对诊断验证路径（在“诊断”中手动启用执行权限、诊断运行以及用于验收的 `BUY`/`SELL` 交易测试），增加了对经纪商模式下工作室智能体的支持，并在激活时及每次提交订单前，从 MT5 终端获取账户的 Demo 模拟状态进行双重实时验证（该诊断测试路径严格仅在模拟账户上运行并明确拒绝真实账户，而平台整体对 `Demo` 和 `Real` 账户的通用支持保持不变）；
   - 专用测试机上的 **111 项端到端实时验收检查尚未完全完成**（在上一版验收候选版本的最终记录运行中，**111 项检查中有 84 项通过**，**4** 项未通过，**10** 项因依赖关系未执行，**6** 项需要人工核对 Figma 界面布局，**7** 项等待外部环境检查）：在上一版本中，手动启用执行、诊断执行以及验证性订单闭环（`BUY`/`SELL`、`trailing-stop` 追踪止损以及核对无残留持仓）尚未关闭；针对这些步骤的修复已合并入主分支并准备好用于下一版测试机候选版本；子研究员智能体的实时验证以及 6 个界面与 Figma 设计基准的人工比对仍在等待执行。

平台未声明已完成真实账户（`Real`）上的实时交易验收。

---

## 未来演进方向（规划中与延后项目）

- **规划中 — 多交易执行器与投资组合管理：** 扩展多智能体交易能力——跨多个品种与交易时段并行协调专业交易智能体、资金分配、执行投资组合级自营公司风险规则、端到端回撤控制及市场状态分析。
- **规划中 — 平台目录与专有 TradeLocker 接入：** 扩充自营公司与交易平台适配器的统一注册表；在当前版本中，**MetaTrader 5 (MT5)** 是当前启用的交易连接器，**FTMO** 是当前支持的自营公司接入，而 **TradeLocker** 接入已列为独立的计划里程碑。
- **规划中 — 已保存的交易智能体工作流：** 用于就绪检查、市场研究、合规自营规则执行以及计划性风险控制的自动化多步可复用流程。
- **设计阶段 — 许可与访问层级体系：** 访问密钥与封闭公测模式（`Free` / `Pro` / `Tester`）的架构设计、设备绑定以及功能层级划分，且不与交易执行权限相混淆（具体方案、价格及商业销售条款尚未敲定）。
- **已延后（不阻碍当前开发路径）：** 带有用于手动编程的独立内置代码编辑器与支持数据集管理的自定义深度历史回测引擎的增强版工作室，以及购买付费 Windows **Authenticode** 发布者证书和独立自定义域名（延后至产品实现盈利之后）。

[查看详细状态与路线图（英文，`docs/en/roadmap.md`） →](docs/en/roadmap.md)

---

## 下载与快速入门（Windows x64）

当前预发布版本：**[Golden Breeze v0.12.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.12.0-alpha)**（对于 `alpha` 预发布版本，请使用直接标签链接或访问 [Releases](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases) 页面，因为 GitHub 的 `/releases/latest` 接口不包含预发布版本）。

- **Windows 版下载（FirstInstall）：** [`GoldenBreeze-FirstInstall-0.12.0-alpha.exe`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe)（`383,300,782` 字节 / `365.5 MiB`）
- **校验和文件：** [`GoldenBreeze-FirstInstall-0.12.0-alpha.exe.sha256`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe.sha256)
- **SHA-256 校验值：** `d4546bc1fe718020f78315bbe98e4b232db044fb80bdb1061f1d2fe44ffd60a2`
- **更新清单与签名：** [`build-manifest.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/build-manifest.json) · [`first-install.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/first-install.json) · [`first-install.json.sig`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/first-install.json.sig)

运行前请在 Windows PowerShell 中校验 `SHA-256`（确认下载的文件与受信任的发布构件逐字节完全一致）：

```powershell
Get-FileHash .\GoldenBreeze-FirstInstall-0.12.0-alpha.exe -Algorithm SHA256
```

- GitHub 自动生成的 **Source code** 源码归档仅包含当前展台仓库的文件，并非应用程序安装包。
- 该 `.exe` 二进制文件暂未签署付费 Windows **Authenticode** 证书，因此在首次安装时 Windows SmartScreen 可能会弹出手动确认提示（在核对 `SHA-256` 校验和无误后，点击*“更多信息” → “仍要运行”*）。
- 首次安装完成后，`stable` 通道更新将通过 HTTPS 进行传输，更新时利用 **Ed25519** 加密清单签名进行安全校验，只需点击**“立即更新”**按钮即可完成升级，无需访问 GitHub。
- 安装和启动应用程序绝不会自动开始交易或建仓：交易时段必须由用户在控制台显式手动启动。

[查看详细安装与首次启动指南（英文，`docs/en/first-start.md`） →](docs/en/first-start.md)

---

## 合作伙伴与赞助商

我们围绕多智能体交易平台的具体交付成果开展合作：
- **交易接入与市场数据：** 交易平台连接器（包括已规划的 TradeLocker 接入）、经纪商与自营交易公司接入以及市场行情数据源；
- **独立验收与试点测试：** 在 Windows x64 系统上验证交易智能体工作流、校验自营公司风险规则并评估控制台易用性；
- **路线图模块定向赞助：** 加速多智能体投资组合协调与风险控制、新型交易适配器、带有专用子智能体的知识库以及对话内策略工程模块的开发；
- **教育与方法论资料：** 交易智能体配置、风险治理与市场状态分析指南。

所有支持均与既定交付成果及可验证的产品成效相挂钩。

[在 GitHub Issues 中探讨合作或赞助事宜 →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

---

## 反馈交流

[在 GitHub Issues 中提问或反馈问题 →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

反馈时请注明确切的应用程序版本（`0.12.0-alpha`）、预期行为与实际表现。截图请确保已去除密码、API 密钥或账户号码等敏感信息。

*历史分析结果或模拟账户（Demo）表现并不代表真实账户（Real）能获得类似结果。Golden Breeze 不承诺或保证任何投资收益。*

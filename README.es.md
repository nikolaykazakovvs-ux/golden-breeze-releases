# Golden Breeze

<p align="center">
  <a href="README.md">English</a> · <a href="README.uk.md">Українська</a> · <a href="README.ru.md">Русский</a> · <strong>Español</strong> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

![Golden Breeze — Plataforma de trading multiagente](assets/brand/golden-breeze-banner-en.svg)

**Plataforma de trading multiagente: trabajo colaborativo de agentes de IA especializados a lo largo de todo el proceso operativo de trading — desde el análisis de mercado y las decisiones operativas hasta la ejecución, la gestión de posiciones y el control de riesgo bajo la supervisión del usuario.**

Golden Breeze está diseñada para el trabajo colaborativo de agentes de IA especializados en trading. Desde un único Panel de Control (Control Desk), el usuario supervisa los agentes, sus tareas y el acceso a las cuentas de trading conectadas: desde el análisis de mercado, la toma de decisiones, la gestión de posiciones y el control de riesgo hasta la investigación, el desarrollo de estrategias, la verificación aislada y el catálogo de versiones de estrategias.

[**Descargar para Windows (v0.14.0-alpha)**](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/GoldenBreeze-FirstInstall-0.14.0-alpha.exe) · [**Escaparate web (EN)**](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) · [Escaparate web (UA)](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/uk/) · [Escaparate web (RU)](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/) · [Lanzamiento v0.14.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.14.0-alpha) · [Estado y hoja de ruta (en inglés)](docs/en/roadmap.md) · [Guía de primer inicio (en inglés)](docs/en/first-start.md) · [Socios y patrocinadores](#socios-y-patrocinadores)

> **Alpha · v0.14.0-alpha (publicado el 11 de noviembre de 2026; balance de estado y hoja de ruta a 12 de noviembre de 2026).** El paquete de instalación principal `GoldenBreeze-FirstInstall-0.14.0-alpha.exe` (canal `stable`, Windows x64) está publicado en Releases e incorpora las capacidades de los ciclos `0.13.0-alpha`–`0.14.0-alpha`. Para el instalador publicado del canal `stable`, se han verificado en un entorno Windows en la nube la instalación limpia, la desinstalación NSIS y la actualización `0.13.0-alpha → 0.14.0-alpha` con conservación de los datos del usuario. En el banco de pruebas dedicado de Windows x64 (usando la compilación de aceptación de la misma revisión de código con `FTMO-Demo`), se han verificado la actualización conservando la sesión de FTMO, la recuperación a la compilación operativa `0.14` ante un paquete de prueba defectuoso, la conexión con FTMO MT5, la publicación y activación de configuraciones en el Estudio de Agentes, el pase de cálculo (`dry-run`) de la estrategia ordinaria y operaciones demo en vivo de `0.01 XAUUSD` con comprobaciones de riesgo y gestión de `trailing-stop` en escenarios de aceptación y diagnóstico (no se declara una aceptación completada de trading en vivo en cuenta real `Real`).

---

## Escaparate web del producto (GitHub Pages)

Se ha publicado un escaparate web estático, responsivo y trilingüe del producto desde `main:/docs`:
- **Escaparate web en inglés:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/)
- **Escaparate web en ucraniano:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/uk/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/uk/)
- **Escaparate web en ruso:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/)
- Visión general de la arquitectura de la plataforma de trading multiagente, el flujo operativo de trading en 5 pasos y una vista previa interactiva del espacio de trabajo del Panel de Control (Control Desk) con datos de demostración;
- Matriz interactiva de estado de capacidades (`En el lanzamiento v0.14` con insignias explícitas del circuito de verificación en cada tarjeta, `Planificado`, `Pospuesto`);
- Enlaces directos de descarga de `FirstInstall`, copia con un solo clic de `SHA-256` y comandos de verificación en PowerShell;
- Documentación de usuario en inglés: [Estado y hoja de ruta (`docs/en/roadmap.md`, en inglés)](docs/en/roadmap.md) · [Instalación y primer inicio (`docs/en/first-start.md`, en inglés)](docs/en/first-start.md);
- Notas canónicas de mantenimiento del repositorio y de Pages (en ruso): [`docs/github-pages.md` (RU)](docs/github-pages.md) · [`docs/CONTENT-MAINTENANCE.md` (RU)](docs/CONTENT-MAINTENANCE.md).

---

## Disponible en el lanzamiento v0.14.0-alpha (canal stable)

- **Panel de Control de agentes de trading (Control Desk) y Estudio de Agentes (Agent Studio).** Perfiles de agentes, asignación de instrumento operativo, cuenta, límites de riesgo y versión de estrategia, comparación estricta de parámetros al aplicar un borrador del Estudio, registro de resultados de "Revisión de comportamiento" (incluidas versiones con estado `+sourcefree`), análisis inmediato sobre barras cerradas del bróker incluso con el mercado cerrado, bloque **"Estado del mercado"** alineado con el calendario oficial de FTMO, verificación de preparación previa al inicio y escalado de ventana (`25%–500%`) con diseño compacto adaptable (`<= 700px`). El inicio y la detención de una sesión de trading son acciones explícitas e independientes del usuario; durante una sesión activa, el agente gestiona las posiciones dentro de los límites de riesgo definidos.
- **Cuentas, empresas de fondeo (prop firms) e integración operativa con MetaTrader 5 (MT5).** Admite cuentas demo (`Demo`) y reales (`Real`) a través de **MT5**, fichas neutrales de empresas de fondeo y cuentas (con GoatFunded explícitamente marcado como "Soporte en desarrollo"), mecanismo unificado de ventana de inicio de sesión, selector **"Conectar ahora"** y selección automática de adaptador por familia de plataforma (`MT5`/`MT4`), adición automática del instrumento a la "Observación del mercado" de MT5 y verificación en segundo plano de la hora del bróker, aprovisionamiento automático del terminal MT5 dedicado con colocación de ventana sin robo de foco y cierre automático al salir o desconectar, además de verificación de identidad y tipo de cuenta, permisos de trading automático y límites de riesgo.
- **Chat del agente, Biblioteca de conocimientos, generación de estrategias y selección de modelos.** El espacio de trabajo "Chat del agente" opera el agente principal tanto mediante **Claude CLI** como mediante **Codex CLI (inicio de sesión con ChatGPT sin clave API)** con respuestas formateadas en Markdown, gestión de conversaciones y aislamiento de borradores por chat, selección de modelo de IA y nivel de razonamiento (`thinking effort`) mostrando modelo solicitado frente a modelo real, archivos adjuntos multimodales (`PNG`/`JPG`, texto y tablas, `PDF`, `DOCX` y extracción aislada de fotogramas de vídeos cortos), **Biblioteca de conocimientos** integrada con citas de fuente y página, **búsqueda web** en vivo, **subagente investigador secundario** en código y generación directa de código de estrategias en Python desde el chat con verificación aislada en barras sintéticas y botón **"Añadir al catálogo"** para el Estudio de Agentes.
- **Instalador `FirstInstall` y actualización automática directa (`stable`).** El instalador incorpora su propio entorno de ejecución para Windows x64 y no requiere una instalación independiente de Python. Las actualizaciones se entregan al pulsar un botón desde un servidor HTTPS dedicado con verificación criptográfica de la firma del manifiesto **Ed25519**, comprobación del sello de revisión de la compilación instalada, finalización del árbol de procesos secundarios (Job Object), conservación de perfiles de agentes y cuentas, mecanismo de reversión (rollback) de recuperación e informes anónimos y breves de fallos de actualización.
- **Interfaz trilingüe (`RU` · `UA` · `EN`).** El cambio entre ruso, ucraniano e inglés funciona en el Panel de Control, el Estudio de Agentes, el chat, la memoria, las fichas de empresas de fondeo y las notificaciones de actualización, incluida la localización completa en `RU`/`UA`/`EN` de la ficha **"Condiciones de FTMO"**, el bloque **"Conciliación con el terminal"**, los mensajes de registro de cuenta y los estados legibles de preparación en el Panel de Control.

> **Vista previa interactiva del Panel de Control:** el [escaparate web en inglés](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) presenta un diseño interactivo de demostración del espacio de trabajo del Panel de Control con fichas de perfil de agentes de trading (`XAUUSD` / `EURUSD`), gráfico de precios, panel de cuenta y riesgo, registro de decisiones y gestión de stop de protección (datos de demostración).

---

## Entregado en el ciclo 0.13–0.14-alpha y estado de la aceptación en vivo (v0.14.0-alpha, balance a 12 de noviembre de 2026)

La entrega de capacidades en el instalador publicado `v0.14.0-alpha` (`stable`) se distingue de los escenarios específicos de verificación comprobados por entorno y tipo de cuenta:

1. **Biblioteca de conocimientos, archivos adjuntos multimodales, búsqueda web y subagente investigador secundario en el chat:**
   - Adjuntar a los mensajes de chat capturas de pantalla y gráficos, archivos de texto y tablas, `PDF` (con capa de texto), `DOCX` y fragmentos cortos de vídeo (hasta 10 MB y 10 minutos — extrayendo fotogramas en un proceso aislado sin reconocimiento de audio);
   - Funcionamiento completo del agente principal tanto mediante **Claude CLI** como a través de **Codex CLI (inicio de sesión con ChatGPT sin clave API)** con respuestas formateadas en Markdown (diálogo en vivo del chat principal mediante Claude CLI verificado en la interfaz de escritorio durante la aceptación de `v0.14.0-alpha`);
   - **Biblioteca de conocimientos** integrada (almacenamiento de libros, documentos y notas, búsqueda y lectura con citas de fuente y página/sección), **búsqueda web** en vivo con registro de URL y marcas de tiempo de acceso, y delegación de tareas de investigación en un **subagente investigador secundario** (implementado en código con acceso estrictamente limitado a la Biblioteca de conocimientos y a la búsqueda web, sin acceso a cuentas de trading; la verificación en vivo por separado de la delegación del investigador en el banco de pruebas continúa como tarea de seguimiento).
2. **Generación de código de estrategia desde el chat, verificación aislada y registro en el catálogo del Estudio:**
   - El agente principal escribe y perfecciona código de estrategia en Python directamente en el chat; la aplicación valida el código contra una lista blanca de estructuras y lo ejecuta en un proceso aislado con memoria limitada sobre barras sintéticas (comprobando la ejecutabilidad y los invariantes fundamentales en lugar de ejecutar un backtest histórico profundo);
   - La respuesta del chat muestra una ficha de estrategia con vista previa del código y el botón **"Añadir al catálogo"**, haciendo que la versión registrada esté disponible de inmediato para su selección en el Estudio de Agentes sin necesidad de copiar archivos manualmente.
3. **Análisis con mercado cerrado, zonas horarias del bróker, Panel de Control y ciclo de vida del terminal MT5:**
   - Análisis inmediato de barras cerradas mediante **"Analizar mercado"** cuando el mercado está cerrado, sin esperar un tick en vivo; persistencia del historial a través de los descansos habituales de sesión diarios y de fin de semana; bloque **"Estado del mercado"** conforme al calendario oficial de FTMO y fechado semanal de barras alineado con la zona horaria comprobada del servidor (incluidos los cambios de horario de verano/invierno); las barras sin UTC comprobado nunca se envían al circuito de trading;
   - Incorporación automática del instrumento a la "Observación del mercado" de MT5 mientras se espera la sincronización del historial, comprobación en segundo plano de la hora del servidor del bróker al conectar la cuenta y seleccionar el agente, y explicaciones explícitas de los motivos de espera en las comprobaciones de preparación del Panel de Control;
   - Selector **"Conectar ahora"** y selección automática de adaptador por familia de plataforma (`MT5`/`MT4`) al añadir una cuenta, aprovisionamiento automático del terminal MT5 dedicado (permiso de trading algorítmico habilitado automáticamente en los ajustes del terminal y espacio de trabajo estándar preparado) con disposición de ventana sin activación de foco y cierre automático al salir de la aplicación o desconectar la cuenta, verificación del sello de revisión de la compilación instalada, localización en `RU`/`UA`/`EN` de la ficha **"Condiciones de FTMO"** y del bloque **"Conciliación con el terminal"**, sustitución de códigos internos por estados legibles en el Panel de Control y comparación estricta de parámetros al aplicar un borrador del Estudio.
4. **Ruta demo de diagnóstico en modo bróker y límites de verificación (`stable` CI + banco de aceptación FTMO MT5 Demo):**
   - Para el circuito de verificación de diagnóstico (habilitación manual de la ejecución en Diagnóstico, ejecución de diagnóstico y operaciones de prueba de aceptación `BUY`/`SELL`), se admiten agentes del Estudio en modo bróker con una doble verificación reciente del estado demo de la cuenta desde el terminal MT5 en el momento de la activación y antes de cada envío de orden (esta ruta de prueba de diagnóstico opera estrictamente en cuentas demo y bloquea cuentas reales, mientras que el soporte general de la plataforma para conectar y operar tanto con cuentas `Demo` como `Real` de MT5 se mantiene intacto);
   - La verificación de `v0.14.0-alpha` por circuitos confirmó:
     - **Instalador publicado `stable` (Windows CI en la nube) y banco local de aceptación:** para el paquete publicado `GoldenBreeze-FirstInstall-0.14.0-alpha.exe` (`stable`), se verificaron en Windows en la nube la instalación limpia, la desinstalación NSIS y la actualización `0.13.0-alpha → 0.14.0-alpha` conservando los datos del usuario; en el banco local de aceptación Windows x64 (compilación de aceptación de la misma revisión de código), se verificaron el arranque en frío, el cierre limpio del árbol de procesos (`0` procesos residuales), la actualización `0.13.0-alpha → 0.14.0-alpha` conservando base de datos, estrategias y sesión de FTMO, y la reversión de recuperación mediante el botón de la ventana de recuperación desde un paquete de prueba defectuoso de vuelta a la compilación operativa `0.14` de aceptación (la reversión `0.14.0-alpha → 0.13.0-alpha` de la compilación publicada `stable` no se probó por separado);
     - **Conexión FTMO, barrera de riesgo y Estudio de Agentes:** conexión en vivo con `FTMO-Demo` en MT5, verificación del cumplimiento de reglas de la empresa de fondeo, bloqueo protector ante intentos de configurar límites del agente más débiles que las reglas del programa, y creación, validación, publicación `v1` y activación de configuración (**"Aplicar configuración"**) en el Estudio;
     - **Escenarios de trading en `XAUUSD` (`M5`):** pase de cálculo (`dry-run`) de la estrategia ordinaria (señal `+sourcefree` en barras `M5` cerradas, revisión de IA, cálculo de volumen y validación previa de parámetros de la orden sin enviar una orden comercial viva al mercado), además de operaciones demo reales (`BUY 0.01 XAUUSD` con comprobación de límites de riesgo y reserva de costes de salida, confirmación de `SL`/`TP` en servidor, cierre de posición, conciliación de operación y comprobación de posición residual cero `0/0`) y `5/5` escenarios de diagnóstico superados (dos de los cuales verificaron la modificación en vivo de `trailing-stop` en el servidor, con detención limpia de sesión a `0` posiciones abiertas y `0` órdenes activas) en escenarios de aceptación y diagnóstico sobre `FTMO-Demo`.
   - La verificación de seguimiento por separado de la delegación en el subagente investigador secundario en el banco de pruebas y las comparaciones manuales restantes con los patrones de Figma continúan de forma independiente.

La plataforma admite la conexión tanto de cuentas `Demo` como `Real` de MT5; no se declara una aceptación completada de trading en vivo en cuenta real (`Real`) para `v0.14.0-alpha`.

---

## Hacia dónde vamos (Planificado y pospuesto)

- **Planificado — Múltiples ejecutores de trading y gestión de carteras:** escalado del trading multiagente — coordinación en paralelo de agentes de trading especializados a través de múltiples instrumentos y sesiones, asignación de capital, aplicación de reglas de riesgo de empresas de fondeo a nivel de cartera, control integral de reducción de capital (drawdown) y analítica de regímenes de mercado.
- **Planificado — Catálogo de plataformas e integración dedicada de TradeLocker:** ampliación del registro unificado de adaptadores de plataformas y empresas de fondeo; en el lanzamiento actual, **MetaTrader 5 (MT5)** es el conector operativo activo y **FTMO** es la integración de empresa de fondeo admitida actualmente, mientras que la integración de **TradeLocker** está programada como un hito planificado independiente.
- **Planificado — Flujos de trabajo guardados de agentes de trading:** rutinas multietapa repetibles para comprobaciones de preparación, análisis de mercado, aplicación de reglas verificadas de empresas de fondeo y control programado de riesgo.
- **Fase de diseño — Esquema de licencias y niveles de acceso:** diseño arquitectónico de claves de acceso y modos de prueba beta cerrada (`Free` / `Pro` / `Tester`), vinculación de dispositivos y separación de niveles de funcionalidad sin mezclar la concesión de licencias con los permisos de ejecución operativa (los planes, precios y condiciones de comercialización aún no están aprobados).
- **Pospuesto sin bloquear el camino actual:** un Estudio ampliado con un editor de código independiente integrado para programación manual y un motor propio de backtesting histórico profundo con gestión de conjuntos de datos, así como la adquisición de un certificado de firma de código **Authenticode** de pago para Windows y un dominio personalizado dedicado (pospuestos hasta que el producto alcance rentabilidad).

[Estado detallado y hoja de ruta (`docs/en/roadmap.md`, en inglés) →](docs/en/roadmap.md)

---

## Descarga y primeros pasos (Windows x64)

Versión preliminar actual: **[Golden Breeze v0.14.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.14.0-alpha)** (para versiones preliminares `alpha`, utilice el enlace directo a la etiqueta o la página de [Releases](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases), ya que el endpoint `/releases/latest` de GitHub excluye las versiones preliminares).

- **Descarga para Windows (FirstInstall):** [`GoldenBreeze-FirstInstall-0.14.0-alpha.exe`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/GoldenBreeze-FirstInstall-0.14.0-alpha.exe) (`406,722,870` bytes / `387.9 MiB`)
- **Archivo de suma de comprobación:** [`GoldenBreeze-FirstInstall-0.14.0-alpha.exe.sha256`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/GoldenBreeze-FirstInstall-0.14.0-alpha.exe.sha256)
- **Valor SHA-256:** `f166f00d4bbfd5e299c7f52e9ba3b51c3c208ea1d9f3b93dbc039806e113d69e`
- **Manifiesto de actualización y firma:** [`build-manifest.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/build-manifest.json) · [`first-install.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/first-install.json) · [`first-install.json.sig`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.14.0-alpha/first-install.json.sig)

Comprobación de `SHA-256` en Windows PowerShell antes de ejecutar (confirma la coincidencia exacta byte a byte entre el archivo descargado y el artefacto confiable del lanzamiento):

```powershell
Get-FileHash .\GoldenBreeze-FirstInstall-0.14.0-alpha.exe -Algorithm SHA256
```

- Los archivos comprimidos de código fuente (**Source code**) generados automáticamente por GitHub contienen únicamente los archivos de este repositorio del escaparate y no constituyen el instalador de la aplicación.
- El archivo ejecutable `.exe` no está firmado con un certificado comercial Windows **Authenticode**, por lo que Windows SmartScreen podría solicitar confirmación manual durante la primera instalación (tras verificar el `SHA-256`, haga clic en *"Más información" → "Ejecutar de todas formas"*).
- Tras la instalación inicial, las actualizaciones del canal `stable` se entregan mediante HTTPS con verificación criptográfica de la firma del manifiesto **Ed25519** a través del botón **"Actualizar ahora"** sin necesidad de acceder a GitHub.
- La instalación y el inicio de la aplicación nunca inician operaciones ni abren órdenes de forma automática: la sesión de trading la inicia explícitamente el usuario desde el Panel de Control.

[Guía detallada de instalación y primer inicio (`docs/en/first-start.md`, en inglés) →](docs/en/first-start.md)

---

## Socios y patrocinadores

Colaboramos en torno a entregas concretas de la plataforma de trading multiagente:
- **Integraciones operativas y datos de mercado:** conectores para plataformas de trading (incluida la integración planificada de TradeLocker), integraciones con brókeres y empresas de fondeo, y fuentes de cotizaciones de mercado;
- **Aceptación independiente y pruebas piloto:** verificación del funcionamiento de los agentes de trading en sistemas Windows x64, validación de las reglas de riesgo de empresas de fondeo y evaluación de la usabilidad del Panel de Control;
- **Patrocinio específico de módulos de la hoja de ruta:** acelerar la coordinación de múltiples agentes en carteras y el control de riesgo, nuevos adaptadores de trading, la Biblioteca de conocimientos con subagentes especializados y el entorno de diseño de estrategias desde el chat;
- **Materiales educativos y metodológicos:** documentación sobre configuración de agentes de trading, gestión de riesgos y análisis de regímenes de mercado.

El apoyo se vincula a entregas acordadas y resultados verificables en el producto.

[Debatir sobre colaboraciones o patrocinio en GitHub Issues →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

---

## Comentarios y contacto

[Hacer una pregunta o informar de un problema en GitHub Issues →](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/issues)

Indique la versión exacta de la aplicación (`0.14.0-alpha`), el comportamiento esperado y el comportamiento real. Adjunte capturas de pantalla sin contraseñas, claves API ni números de cuenta.

*Los resultados del análisis histórico o el rendimiento en una cuenta demo no prometen resultados similares en una cuenta real. Golden Breeze no garantiza rentabilidad.*

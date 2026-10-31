# Golden Breeze

<p align="center">
  <a href="README.md">English</a> · <a href="README.uk.md">Українська</a> · <a href="README.ru.md">Русский</a> · <strong>Español</strong> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

![Golden Breeze — Plataforma de trading multiagente](assets/brand/golden-breeze-banner-en.svg)

**Plataforma de trading multiagente: trabajo colaborativo de agentes de IA especializados a lo largo de todo el proceso operativo de trading — desde el análisis de mercado y las decisiones operativas hasta la ejecución, la gestión de posiciones y el control de riesgo bajo la supervisión del usuario.**

Golden Breeze está diseñada para el trabajo colaborativo de agentes de IA especializados en trading. Desde un único Panel de Control (Control Desk), el usuario supervisa los agentes, sus tareas y el acceso a las cuentas de trading conectadas: desde el análisis de mercado, la toma de decisiones, la gestión de posiciones y el control de riesgo hasta la investigación, el desarrollo de estrategias, la verificación aislada y el catálogo de versiones de estrategias.

[**Descargar para Windows (v0.12.0-alpha)**](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe) · [**Escaparate web (EN)**](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) · [Escaparate web (RU)](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/) · [Lanzamiento v0.12.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.12.0-alpha) · [Estado y hoja de ruta (en inglés)](docs/en/roadmap.md) · [Guía de primer inicio (en inglés)](docs/en/first-start.md) · [Socios y patrocinadores](#socios-y-patrocinadores)

> **Alpha · v0.12.0-alpha (publicado el 17 de octubre de 2026; balance de estado y hoja de ruta a 28 de octubre de 2026).** El paquete de instalación principal `GoldenBreeze-FirstInstall-0.12.0-alpha.exe` (canal `stable`, Windows x64) está publicado en Releases. La publicación del instalador confirma la entrega de la compilación, mientras que las capacidades de los ciclos `0.13.0-alpha`–`0.14.0-alpha` están integradas en la rama principal de desarrollo y se encuentran superando la aceptación funcional en vivo de extremo a extremo en un banco de pruebas dedicado de Windows x64 antes del próximo lanzamiento público.

---

## Escaparate web del producto (GitHub Pages)

Se ha publicado un escaparate web estático, responsivo y bilingüe del producto desde `main:/docs`:
- **Escaparate web en inglés:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/)
- **Escaparate web en ruso:** [`https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/`](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/)
- Visión general de la arquitectura de la plataforma de trading multiagente, el flujo operativo de trading en 5 pasos y una vista previa interactiva del espacio de trabajo del Panel de Control (Control Desk) con datos de demostración;
- Matriz interactiva de estado de capacidades (`En el lanzamiento v0.12`, `Implementado en 0.13–0.14 / En aceptación`, `Planificado`, `Pospuesto`);
- Enlaces directos de descarga de `FirstInstall`, copia con un solo clic de `SHA-256` y comandos de verificación en PowerShell;
- Documentación de usuario en inglés: [Estado y hoja de ruta (`docs/en/roadmap.md`, en inglés)](docs/en/roadmap.md) · [Instalación y primer inicio (`docs/en/first-start.md`, en inglés)](docs/en/first-start.md);
- Notas canónicas de mantenimiento del repositorio y de Pages (en ruso): [`docs/github-pages.md` (RU)](docs/github-pages.md) · [`docs/CONTENT-MAINTENANCE.md` (RU)](docs/CONTENT-MAINTENANCE.md).

---

## Disponible en el lanzamiento v0.12.0-alpha (canal stable)

- **Panel de Control de agentes de trading (Control Desk) y Estudio de Agentes (Agent Studio).** Perfiles de agentes, asignación de instrumento operativo, cuenta, límites de riesgo y versión de estrategia, registro de resultados de "Revisión de comportamiento" (incluidas versiones con estado `+sourcefree`), análisis de mercado sobre barras cerradas del bróker y verificación de preparación previa al inicio. El inicio y la detención de una sesión de trading son acciones explícitas e independientes del usuario; durante una sesión activa, el agente gestiona las posiciones dentro de los límites de riesgo definidos.
- **Cuentas, empresas de fondeo (prop firms) e integración operativa con MetaTrader 5 (MT5).** Admite cuentas demo (`Demo`) y reales (`Real`) a través de **MT5**, fichas neutrales de empresas de fondeo y cuentas, mecanismo unificado de ventana de inicio de sesión, verificación de identidad y tipo de cuenta, permisos de trading automático y límites de riesgo.
- **Chat del agente, contexto y selección de modelos.** El espacio de trabajo "Chat del agente" para tareas operativas y de investigación ofrece creación, renombramiento, agrupación, archivado y restauración de conversaciones, aislamiento de borradores por chat, selección de modelo de IA y nivel de razonamiento (`thinking effort`) según las capacidades del proveedor de IA conectado, así como visualización del modelo solicitado frente al modelo real en los detalles de ejecución (en la versión publicada `v0.12.0-alpha`, el chat del agente principal opera mediante **Claude CLI**, mientras que el inicio de sesión con **Codex CLI / ChatGPT** en Ajustes ya está preparado y pasa a ser un motor de chat principal completo en el ciclo `0.13–0.14-alpha`).
- **Instalador `FirstInstall` y actualización automática directa (`stable`).** El instalador incorpora su propio entorno de ejecución para Windows x64 y no requiere una instalación independiente de Python. Las actualizaciones se entregan al pulsar un botón desde un servidor HTTPS dedicado con verificación criptográfica de la firma del manifiesto **Ed25519**, finalización del árbol de procesos secundarios (Job Object), conservación de perfiles de agentes y cuentas, e informes anónimos y breves de fallos de actualización.
- **Interfaz trilingüe (`RU` · `UA` · `EN`).** El cambio entre ruso, ucraniano e inglés funciona en el Panel de Control, el Estudio de Agentes, el chat, la memoria, las fichas de empresas de fondeo y las notificaciones de actualización (en la compilación publicada `v0.12.0-alpha`, algunos mensajes de registro de cuenta en Ajustes y unas pocas etiquetas en la ficha de cuenta FTMO y en la pantalla de verificación de inicio aún aparecían en ruso; su localización y la sustitución de códigos de estado sin procesar se completaron en el ciclo `0.13–0.14-alpha`).

> **Vista previa interactiva del Panel de Control:** el [escaparate web en inglés](https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/) presenta un diseño interactivo de demostración del espacio de trabajo del Panel de Control con fichas de perfil de agentes de trading (`XAUUSD` / `EURUSD`), gráfico de precios, panel de cuenta y riesgo, registro de decisiones y gestión de stop de protección (datos de demostración).

---

## Implementado después de v0.12.0-alpha y en proceso de aceptación (ciclo 0.13–0.14-alpha, balance a 28 de octubre de 2026)

La instalación, la actualización automática y las pruebas continuas de CI confirman la entrega de la compilación, mientras que la aceptación funcional en vivo se supervisa por separado. Integrado en la rama principal de desarrollo tras `v0.12.0-alpha` y actualmente en verificación por etapas en el banco de pruebas de aceptación dedicado de Windows x64:

1. **Biblioteca de conocimientos, archivos adjuntos multimodales, búsqueda web y subagente investigador secundario en el chat:**
   - Adjuntar a los mensajes de chat capturas de pantalla y gráficos, archivos de texto y tablas, `PDF` (con capa de texto), `DOCX` y fragmentos cortos de vídeo (hasta 10 MB y 10 minutos — extrayendo fotogramas en un proceso aislado sin reconocimiento de audio);
   - Funcionamiento completo del agente principal tanto mediante **Claude CLI** como a través de **Codex CLI (inicio de sesión con ChatGPT sin clave API)** con respuestas formateadas en Markdown;
   - **Biblioteca de conocimientos** integrada (almacenamiento de libros, documentos y notas, búsqueda y lectura con citas de fuente y página/sección), **búsqueda web** en vivo con registro de URL y marcas de tiempo de acceso, y delegación de tareas de investigación en un **subagente investigador secundario** (implementado en código con acceso estrictamente limitado a la Biblioteca de conocimientos y a la búsqueda web, sin acceso a cuentas de trading; la verificación de aceptación en vivo de la delegación del investigador en el banco de pruebas sigue pendiente).
2. **Generación de código de estrategia desde el chat, verificación aislada y registro en el catálogo del Estudio:**
   - El agente principal escribe y perfecciona código de estrategia en Python directamente en el chat; la aplicación valida el código contra una lista blanca de estructuras y lo ejecuta en un proceso aislado con memoria limitada sobre barras sintéticas (comprobando la ejecutabilidad y los invariantes fundamentales en lugar de ejecutar un backtest histórico profundo);
   - La respuesta del chat muestra una ficha de estrategia con vista previa del código y el botón **"Añadir al catálogo"**, haciendo que la versión registrada esté disponible de inmediato para su selección en el Estudio de Agentes sin necesidad de copiar archivos manualmente.
3. **Análisis con mercado cerrado, zonas horarias del bróker, Panel de Control y ciclo de vida del terminal MT5:**
   - Análisis inmediato de barras cerradas mediante **"Analizar mercado"** cuando el mercado está cerrado, sin esperar un tick en vivo; persistencia del historial a través de los descansos habituales de sesión diarios y de fin de semana; bloque **"Estado del mercado"** conforme al calendario oficial de FTMO y fechado semanal de barras alineado con la zona horaria comprobada del servidor (incluidos los cambios de horario de verano/invierno); las barras sin UTC comprobado nunca se envían al circuito de trading;
   - Incorporación automática del instrumento a la "Observación del mercado" de MT5 mientras se espera la sincronización del historial, comprobación en segundo plano de la hora del servidor del bróker al conectar la cuenta y seleccionar el agente, y explicaciones explícitas de los motivos de espera en las comprobaciones de preparación del Panel de Control;
   - Selector **"Conectar ahora"** y selección automática de adaptador por familia de plataforma (`MT5`/`MT4`) al añadir una cuenta, disposición de ventana sin activación de foco y cierre automático del terminal MT5 dedicado al salir de la aplicación o desconectar la cuenta, verificación del sello de revisión de la compilación instalada, localización en `RU`/`UA`/`EN` de la ficha **"Condiciones de FTMO"** y del bloque **"Conciliación con el terminal"**, sustitución de códigos internos por estados legibles en el Panel de Control y comparación estricta de parámetros al aplicar un borrador del Estudio.
4. **Ruta demo de diagnóstico en modo bróker y estado actual de la aceptación en vivo:**
   - Para el circuito de verificación de diagnóstico (habilitación manual de la ejecución en Diagnóstico, ejecución de diagnóstico y operaciones de prueba de aceptación `BUY`/`SELL`), se añadió soporte para agentes del Estudio en modo bróker con una doble verificación reciente del estado demo de la cuenta desde el terminal MT5 en el momento de la activación y antes de cada envío de orden (esta ruta de prueba de diagnóstico opera estrictamente en cuentas demo y rechaza cuentas reales, mientras que el soporte general de la plataforma tanto para cuentas `Demo` como `Real` se mantiene intacto);
   - La aceptación funcional en vivo de extremo a extremo de **111 comprobaciones** en el banco de pruebas dedicado **aún no ha concluido** (en la última ejecución registrada sobre el candidato de aceptación anterior, se superaron **84 de 111** comprobaciones, con **4** fallos, **10** pasos dependientes no ejecutados, **6** revisiones manuales de diseño en Figma requeridas y **7** comprobaciones externas pendientes): en el candidato anterior quedaron abiertos la habilitación manual de ejecución, el lanzamiento de diagnóstico y el ciclo de órdenes de verificación (`BUY`/`SELL`, `trailing-stop` y conciliación de ausencia de posiciones residuales), para los cuales ya se han integrado correcciones en la rama principal de cara al siguiente candidato del banco de pruebas, mientras que la comprobación en vivo del subagente investigador secundario y la comparación manual de 6 pantallas con los patrones de Figma siguen pendientes.

No se declara una aceptación completada de trading en vivo en cuenta real (`Real`).

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

Versión preliminar actual: **[Golden Breeze v0.12.0-alpha](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/tag/v0.12.0-alpha)** (para versiones preliminares `alpha`, utilice el enlace directo a la etiqueta o la página de [Releases](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases), ya que el endpoint `/releases/latest` de GitHub excluye las versiones preliminares).

- **Descarga para Windows (FirstInstall):** [`GoldenBreeze-FirstInstall-0.12.0-alpha.exe`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe) (`383,300,782` bytes / `365.5 MiB`)
- **Archivo de suma de comprobación:** [`GoldenBreeze-FirstInstall-0.12.0-alpha.exe.sha256`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/GoldenBreeze-FirstInstall-0.12.0-alpha.exe.sha256)
- **Valor SHA-256:** `d4546bc1fe718020f78315bbe98e4b232db044fb80bdb1061f1d2fe44ffd60a2`
- **Manifiesto de actualización y firma:** [`build-manifest.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/build-manifest.json) · [`first-install.json`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/first-install.json) · [`first-install.json.sig`](https://github.com/nikolaykazakovvs-ux/golden-breeze-releases/releases/download/v0.12.0-alpha/first-install.json.sig)

Comprobación de `SHA-256` en Windows PowerShell antes de ejecutar (confirma la coincidencia exacta byte a byte entre el archivo descargado y el artefacto confiable del lanzamiento):

```powershell
Get-FileHash .\GoldenBreeze-FirstInstall-0.12.0-alpha.exe -Algorithm SHA256
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

Indique la versión exacta de la aplicación (`0.12.0-alpha`), el comportamiento esperado y el comportamiento real. Adjunte capturas de pantalla sin contraseñas, claves API ni números de cuenta.

*Los resultados del análisis histórico o el rendimiento en una cuenta demo no prometen resultados similares en una cuenta real. Golden Breeze no garantiza rentabilidad.*

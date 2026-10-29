# Памятка по публикации витрины на GitHub Pages (`docs/github-pages.md`)

**Актуализация: 28 октября 2026 года.** В каталоге `docs/` размещён статический лендинг продукта Golden Breeze (`docs/index.html`, `docs/styles.css`, `docs/app.js`, `docs/assets/`, `docs/.nojekyll`), опубликованный через **GitHub Pages** в репозитории витрины и релизов `nikolaykazakovvs-ux/golden-breeze-releases`.

Публичный адрес витрины в GitHub Pages:
- Русская версия: `https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/`
- Английская версия: `https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/en/`

*(Развёртывание активно из `main:/docs`, статус: `built`.)*

---

## 1. Устройство статического лендинга в `docs/`

Лендинг реализован на чистом HTML, CSS и компактном JavaScript без сборщиков, сторонней аналитики и внешних CDN:

- **Точки входа:** `docs/index.html` (русская версия `/golden-breeze-releases/`) и `docs/en/index.html` (английская версия `/golden-breeze-releases/en/`).
- **Стили и адаптивность:** `docs/styles.css` (поддержка десктопа, планшетов и мобильных экранов, компактное меню навигации при `<= 1200px` с сохранением кнопок выпуска и переключателя `RU / EN`, учёт `scroll-padding-top` для фиксированной шапки и `prefers-reduced-motion`).
- **Интерактивность:** `docs/app.js` (мобильное меню навигации, явное переключение языка `RU / EN` с сохранением текущего раздела/query/hash без автоматических редиректов, фильтрация направлений дорожной карты по статусам и копирование `SHA-256` / команды PowerShell, локализованный интерактивный макет Пульта).
- **Отключение Jekyll:** пустой файл `docs/.nojekyll` гарантирует прямую раздачу статических файлов без перезаписи путей генератором Jekyll.
- **Ссылки на документацию:** поскольку при включённом `.nojekyll` прямые переходы на `.md`-файлы внутри GitHub Pages открывают необработанный текст, ссылки из HTML-лендинга на подробные документы (`roadmap.md`, `first-start.md`, `en/roadmap.md`, `en/first-start.md`, `github-pages.md`, `CONTENT-MAINTENANCE.md`) ведут на отрисованные страницы GitHub (`blob/main/docs/...`). Все локальные медиа-ресурсы (`./styles.css` и `../styles.css`, `./app.js` и `../app.js`, `./assets/...` и `../assets/...`) подключены относительными путями и одинаково работают локально и по проектному префиксу `/golden-breeze-releases/` и `/golden-breeze-releases/en/`.

---

## 2. Настройка публикации из `main:/docs`

Публикация витрины настраивается штатным механизмом GitHub без создания отдельных GitHub Actions workflows:

1. Репозиторий витрины и раздачи `nikolaykazakovvs-ux/golden-breeze-releases` переводится в публичный режим (`Public`), чтобы посетители могли открывать витрину, читать документацию и напрямую скачивать установщик `FirstInstall` из раздела `Releases` (основной репозиторий разработки ядра остаётся отдельным и закрытым).
2. В настройках репозитория **Settings → Pages** в блоке **Build and deployment** выбирается:
   - **Source:** `Deploy from a branch`
   - **Branch:** `main`, папка `/docs` → **Save**.
3. После завершения развёртывания проверяется открытие страницы по адресу `https://nikolaykazakovvs-ux.github.io/golden-breeze-releases/` и работа ссылок на текущий выпуск `v0.12.0-alpha`.

---

## 3. Локальный предпросмотр

Для локальной проверки вёрстки из корня репозитория используется стандартный HTTP-сервер на локальном интерфейсе (`127.0.0.1`):

```powershell
python -m http.server 8765 --bind 127.0.0.1 --directory docs
```

Локальный адрес предпросмотра: `http://127.0.0.1:8765/`.

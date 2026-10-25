/* ==========================================================================
   Golden Breeze — Независимый клиентский скрипт витрины (без сборщиков и CDN)
   Возможности:
   1. Адаптивная навигация шапки (<= 1200px меню разделов, кнопка выпуска всегда видна, Escape, resize)
   2. Фильтрация матрицы направлений по честным статусам готовности
   3. Копирование SHA-256 и команд PowerShell с понятным подтверждением
   4. Интерактивный демонстрационный блок Пульта управления (профили + пауза/воспроизведение)
   ========================================================================== */

(function () {
  "use strict";

  // 1. Адаптивная навигация шапки (порог 1200px для комфортного размещения русского текста)
  var navToggle = document.getElementById("nav-toggle");
  var siteNav = document.getElementById("site-nav");

  if (navToggle && siteNav) {
    navToggle.addEventListener("click", function () {
      var expanded = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!expanded));
      siteNav.classList.toggle("is-open", !expanded);
    });

    siteNav.addEventListener("click", function (event) {
      var link = event.target.closest("a");
      if (link && window.innerWidth <= 1200) {
        navToggle.setAttribute("aria-expanded", "false");
        siteNav.classList.remove("is-open");
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && siteNav.classList.contains("is-open")) {
        navToggle.setAttribute("aria-expanded", "false");
        siteNav.classList.remove("is-open");
        navToggle.focus();
      }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 1200 && siteNav.classList.contains("is-open")) {
        navToggle.setAttribute("aria-expanded", "false");
        siteNav.classList.remove("is-open");
      }
    });
  }

  // 2. Фильтрация матрицы направлений (Roadmap / Статусы)
  var filterButtons = document.querySelectorAll("[data-filter]");
  var matrixItems = document.querySelectorAll("[data-status]");
  var filterCountEl = document.getElementById("filter-count");

  function updateFilter(selectedFilter) {
    var visibleCount = 0;

    matrixItems.forEach(function (item) {
      var status = item.getAttribute("data-status");
      var matches = selectedFilter === "all" || status === selectedFilter;
      if (matches) {
        item.removeAttribute("hidden");
        visibleCount += 1;
      } else {
        item.setAttribute("hidden", "");
      }
    });

    filterButtons.forEach(function (btn) {
      var active = btn.getAttribute("data-filter") === selectedFilter;
      btn.setAttribute("aria-pressed", String(active));
    });

    if (filterCountEl) {
      filterCountEl.textContent = "Показано направлений: " + visibleCount + " из " + matrixItems.length;
    }
  }

  if (filterButtons.length > 0 && matrixItems.length > 0) {
    filterButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var filterValue = btn.getAttribute("data-filter") || "all";
        updateFilter(filterValue);
      });
    });
  }

  // 3. Копирование контрольных сумм и команд проверки
  var copyButtons = document.querySelectorAll("[data-copy-target]");

  function fallbackCopyText(text) {
    var textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.appendChild(textarea);
    textarea.select();
    var ok = false;
    try {
      ok = document.execCommand("copy");
    } catch (err) {
      ok = false;
    }
    document.body.removeChild(textarea);
    return ok;
  }

  copyButtons.forEach(function (btn) {
    var originalLabel = btn.textContent;
    btn.addEventListener("click", function () {
      var targetId = btn.getAttribute("data-copy-target");
      var targetEl = targetId ? document.getElementById(targetId) : null;
      if (!targetEl) {
        return;
      }
      var textToCopy = (targetEl.textContent || "").trim();
      if (!textToCopy) {
        return;
      }

      function showResult(success) {
        btn.textContent = success ? "Скопировано" : "Ошибка";
        setTimeout(function () {
          btn.textContent = originalLabel;
        }, 1800);
      }

      if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
        navigator.clipboard.writeText(textToCopy).then(
          function () {
            showResult(true);
          },
          function () {
            showResult(fallbackCopyText(textToCopy));
          }
        );
      } else {
        showResult(fallbackCopyText(textToCopy));
      }
    });
  });

  // 4. Интерактивный демонстрационный макет Пульта управления (изолированное состояние)
  function initPultDemo() {
    var toggleBtn = document.getElementById("pult-anim-toggle");
    var statusWrap = document.getElementById("pult-anim-status");
    var statusText = document.getElementById("pult-anim-status-text");
    var profileCards = document.querySelectorAll("[data-agent-profile]");

    if (!toggleBtn || profileCards.length === 0) {
      return;
    }

    var PROFILES = {
      "xau-h1": {
        name: "«XAU · Импульс H1»",
        badgeText: "АКТИВЕН · ДЕМО-СЕССИЯ",
        badgeClass: "pult-status-tag pult-status-tag--active",
        studioBanner: "Рабочая версия стратегии <strong>Momentum-Session v2.4.0 (+sourcefree)</strong> применена в Студии. Все условия допуска демо-контура выполнены.",
        symbol: "XAUUSD",
        tf: "H1 (подтв. M15)",
        account: "MT5 Demo · DEMO-01",
        contour: "Демо (MT5)",
        terminal: "MT5 · Подключён",
        llm: "Выбранная модель · Демо",
        strategy: "Momentum v2.4.0 (+sourcefree)",
        risk: "0.5% / сделка · SL обязателен",
        marketLabel: "РЫНОК · XAUUSD (ЗОЛОТО / ДОЛЛАР США)",
        marketState: "ПОТОК АКТИВЕН · ЗАКРЫТЫЕ БАРЫ + ТИК",
        marketSession: "Сессия: <strong>Лондон / Нью-Йорк (02:00–22:00 UTC)</strong>",
        marketBars: "Данные: <strong>200 закрытых баров H1 · EMA-21 · ATR 14.2</strong>",
        accBalance: "$100 000.00",
        accPos: "1 открыта (BUY 0.20 XAUUSD)",
        accDd: "0.38% из 5.00% (норма риска)",
        accLimit: "до 2 одновременных · SL обязателен",
        actionsTitle: "ДЕЙСТВИЯ · XAU · ИМПУЛЬС H1",
        runPillText: "● Торговая сессия активна (Демо)",
        opsSummary: "<strong>РЕЗУЛЬТАТЫ ОПЕРАЦИЙ:</strong> Изучение рынка: прочитано 200 закрытых баров H1, тренд восходящий · Проверить готовность: терминал MT5 подключён, Algo Trading разрешён, спред 18 п. в норме.",
        logTitle: "ЖУРНАЛ АГЕНТА · XAU · ИМПУЛЬС H1",
        posBadge: "Риск защищён · Trailing SL",
        posInstrument: "XAUUSD · BUY 0.20 лота",
        posTicket: "Тикет #DEMO-01 · MT5 Demo",
        posEntry: "2 641.20",
        posSl: "2 643.50 (безубыток+)",
        posTp: "2 662.00",
        chartEntryLabel: "BUY 0.20 @ 2641.20",
        chartSlLabel: "Trailing SL @ 2643.50 (безубыток+)",
        ticks: [
          {
            clock: "14:20:05",
            price: "2 648.40",
            tagPrice: "2648.40",
            delta: "+0.42% (+11.10)",
            equity: "$100 144.00 (+0.14%)",
            pnl: "+$144.00",
            cardMetric: "BUY 0.20 · +$144",
            priceY: 38,
            wickTop: 32,
            bodyY: 36,
            bodyH: 14,
            decision: "14:20:05 · Удержание позиции BUY 0.20 XAUUSD (вход 2 641.20): закрытие H1 выше EMA-21 (2 641.80), защитный стоп переведён в +2.30 п. (2 643.50, trailing-stop активен).",
            topLog: { time: "14:20:05", badge: "СТОП", kind: "sl", msg: "Trailing-stop подтянут на <strong>2 643.50</strong> (+2.30 п. выше цены входа)." }
          },
          {
            clock: "14:20:08",
            price: "2 649.10",
            tagPrice: "2649.10",
            delta: "+0.45% (+11.80)",
            equity: "$100 158.00 (+0.16%)",
            pnl: "+$158.00",
            cardMetric: "BUY 0.20 · +$158",
            priceY: 34,
            wickTop: 29,
            bodyY: 33,
            bodyH: 17,
            decision: "14:20:08 · Сопровождение BUY 0.20 XAUUSD: котировка 2 649.10, импульс сохраняется выше локального уровня 2 646.00; дистанция до цели TP 12.90 п.",
            topLog: { time: "14:20:08", badge: "РЫНОК", kind: "mkt", msg: "Обновление котировки XAUUSD: <strong>2 649.10</strong> (спред 17 п., ликвидность в норме)." }
          },
          {
            clock: "14:20:11",
            price: "2 648.75",
            tagPrice: "2648.75",
            delta: "+0.43% (+11.45)",
            equity: "$100 151.00 (+0.15%)",
            pnl: "+$151.00",
            cardMetric: "BUY 0.20 · +$151",
            priceY: 36,
            wickTop: 30,
            bodyY: 35,
            bodyH: 15,
            decision: "14:20:11 · Проверка параметров риска MT5 Demo: плавающий результат +$151.00, дневной буфер просадки 4.62% свободен, стоп-ордер 2 643.50 подтверждён у брокера.",
            topLog: { time: "14:20:11", badge: "ГОТОВ", kind: "ok", msg: "Сверка защитного стоп-ордера у брокера: <strong>SL 2 643.50</strong> активен на сервере MT5." }
          },
          {
            clock: "14:20:14",
            price: "2 649.60",
            tagPrice: "2649.60",
            delta: "+0.47% (+12.30)",
            equity: "$100 168.00 (+0.17%)",
            pnl: "+$168.00",
            cardMetric: "BUY 0.20 · +$168",
            priceY: 31,
            wickTop: 26,
            bodyY: 31,
            bodyH: 19,
            decision: "14:20:14 · Импульс XAUUSD продолжается (2 649.60): условие следующего шага trailing-stop — закрепление выше 2 651.00.",
            topLog: { time: "14:20:14", badge: "СТОП", kind: "sl", msg: "Мониторинг trailing-stop: следующий перенос SL запланирован при достижении <strong>2 651.00</strong>." }
          }
        ],
        baseLogs: [
          { time: "14:05:12", badge: "ОРДЕР", kind: "exec", msg: "Открыта демо-позиция <strong>BUY 0.20 XAUUSD @ 2 641.20</strong>, SL 2 634.00, TP 2 662.00." },
          { time: "14:00:04", badge: "РЫНОК", kind: "mkt", msg: "Изучение рынка: закрыт бар H1 (2 640.90), пробой локального максимума сессии." },
          { time: "13:58:40", badge: "ГОТОВ", kind: "ok", msg: "Проверка готовности пройдена (6/6): счёт MT5 Demo · DEMO-01, лимит риска 0.5%." }
        ]
      },
      "xau-m15": {
        name: "«XAU · Возврат M15»",
        badgeText: "ГОТОВ К СТАРТУ · ДЕМО",
        badgeClass: "pult-status-tag pult-status-tag--ready",
        studioBanner: "Рабочая версия стратегии <strong>MeanRevert-Band v1.8.2 (+sourcefree)</strong> применена в Студии. Агент ожидает касания нижней границы канала M15.",
        symbol: "XAUUSD",
        tf: "M15 (фильтр H4)",
        account: "MT5 Demo · DEMO-01",
        contour: "Демо (MT5)",
        terminal: "MT5 · Подключён",
        llm: "Выбранная модель · Демо",
        strategy: "MeanRevert v1.8.2 (+sourcefree)",
        risk: "0.35% / сделка · до 1 поз.",
        marketLabel: "РЫНОК · XAUUSD (КАНАЛ ВОЗВРАТА К СРЕДНЕМУ M15)",
        marketState: "ГОТОВ · ОЖИДАНИЕ ЗОНЫ ВХОДА",
        marketSession: "Сессия: <strong>Лондон / Нью-Йорк (02:00–22:00 UTC)</strong>",
        marketBars: "Данные: <strong>300 закрытых баров M15 · VWAP 2 642.10 · RSI 54.8</strong>",
        accBalance: "$100 000.00",
        accPos: "Ожидание точки входа (лимит 1)",
        accDd: "0.38% из 5.00% (норма риска)",
        accLimit: "до 1 позиции · жёсткий SL 6.5 п.",
        actionsTitle: "ДЕЙСТВИЯ · XAU · ВОЗВРАТ M15",
        runPillText: "● Готов к запуску по сигналу (Демо)",
        opsSummary: "<strong>РЕЗУЛЬТАТЫ ОПЕРАЦИЙ:</strong> Изучение рынка: прочитано 300 закрытых баров M15, отклонение от VWAP +0.24% · Проверить готовность: счёт MT5 Demo · DEMO-01 подтверждён, конфликт позиций исключён.",
        logTitle: "ЖУРНАЛ АГЕНТА · XAU · ВОЗВРАТ M15",
        posBadge: "План заявки · Лимитный расчёт",
        posInstrument: "XAUUSD · План BUY LIMIT 0.15",
        posTicket: "Расчётный ордер · ожидание уровня",
        posEntry: "2 639.50 (зона VWAP)",
        posSl: "2 633.00 (-6.50 п.)",
        posTp: "2 649.00 (+9.50 п.)",
        chartEntryLabel: "Зона входа M15 @ 2639.50",
        chartSlLabel: "Расчётный SL @ 2633.00 (-0.35% риска)",
        ticks: [
          {
            clock: "14:20:05",
            price: "2 648.40",
            tagPrice: "2648.40",
            delta: "Откл. VWAP +6.30 п.",
            equity: "$100 144.00 (общий счёт)",
            pnl: "Ожидание 2 639.50",
            cardMetric: "Ожидание сигнала",
            priceY: 40,
            wickTop: 34,
            bodyY: 38,
            bodyH: 13,
            decision: "14:20:05 · Наблюдение M15: цена 2 648.40 находится в нейтральной зоне выше VWAP (2 642.10); вход без подтверждённого отката не выполняется.",
            topLog: { time: "14:20:05", badge: "РЫНОК", kind: "mkt", msg: "Оценка M15: текущая цена <strong>2 648.40</strong>, до расчётной зоны отката 8.90 п." }
          },
          {
            clock: "14:20:08",
            price: "2 648.10",
            tagPrice: "2648.10",
            delta: "Откл. VWAP +6.00 п.",
            equity: "$100 144.00 (общий счёт)",
            pnl: "Ожидание 2 639.50",
            cardMetric: "Ожидание сигнала",
            priceY: 42,
            wickTop: 35,
            bodyY: 40,
            bodyH: 11,
            decision: "14:20:08 · Проверка фильтра старшего таймфрейма H4: структура восходящая, короткие продажи против тренда H4 заблокированы правилами стратегии.",
            topLog: { time: "14:20:08", badge: "ГОТОВ", kind: "ok", msg: "Фильтр H4 активен: разрешены только покупки от зоны поддержки <strong>2 639.50</strong>." }
          }
        ],
        baseLogs: [
          { time: "14:15:00", badge: "РЫНОК", kind: "mkt", msg: "Закрыт бар M15: пересчитаны границы канала возврата и уровень VWAP (2 642.10)." },
          { time: "14:02:18", badge: "ГОТОВ", kind: "ok", msg: "Проверка готовности (6/6): профиль риска 0.35%, терминал MT5 готов." },
          { time: "13:55:10", badge: "СТОП", kind: "sl", msg: "Проверено правило обязательного защитного стопа: дистанция 6.50 п. зафиксирована." }
        ]
      },
      "eur-m30": {
        name: "«EUR · Диапазон M30»",
        badgeText: "ПАУЗА · ИЗУЧЕНИЕ ИСТОРИИ",
        badgeClass: "pult-status-tag pult-status-tag--paused",
        studioBanner: "Рабочая версия стратегии <strong>London-Range v1.3.0 (+sourcefree)</strong> загружена. Выполнено чтение закрытых баров M30 без запуска ордеров.",
        symbol: "EURUSD",
        tf: "M30 (сессия Лондон)",
        account: "MT5 Demo · DEMO-02",
        contour: "Демо (MT5)",
        terminal: "MT5 · Подключён",
        llm: "Выбранная модель · Демо",
        strategy: "London-Range v1.3.0",
        risk: "0.4% / сделка · до 1 поз.",
        marketLabel: "РЫНОК · EURUSD (ЕВРО / ДОЛЛАР США)",
        marketState: "БАРЫ ПРОЧИТАНЫ · РЕЖИМ ИЗУЧЕНИЯ",
        marketSession: "Сессия: <strong>Европейская / Американская (07:00–20:00 UTC)</strong>",
        marketBars: "Данные: <strong>240 закрытых баров M30 · диапазон 1.0840–1.0892</strong>",
        accBalance: "$50 000.00",
        accPos: "0 открытых позиций",
        accDd: "0.00% из 4.00% (дневной лимит)",
        accLimit: "до 1 позиции · ожидание старта",
        actionsTitle: "ДЕЙСТВИЯ · EUR · ДИАПАЗОН M30",
        runPillText: "⏸ На паузе (только анализ баров)",
        opsSummary: "<strong>РЕЗУЛЬТАТЫ ОПЕРАЦИЙ:</strong> Изучение рынка: прочитано 240 закрытых баров M30, границы утреннего диапазона 1.0840–1.0892 · Проверить готовность: демо-счёт MT5 Demo · DEMO-02 проверен, торговля не запущена.",
        logTitle: "ЖУРНАЛ АГЕНТА · EUR · ДИАПАЗОН M30",
        posBadge: "Без открытых сделок",
        posInstrument: "EURUSD · Позиций нет (режим изучения)",
        posTicket: "Счёт MT5 Demo · DEMO-02",
        posEntry: "1.0864 (граница)",
        posSl: "1.0842 (расчётный)",
        posTp: "1.0908 (расчётный)",
        chartEntryLabel: "Верхняя граница @ 1.0864",
        chartSlLabel: "Расчётный SL @ 1.0842 (22 п.)",
        ticks: [
          {
            clock: "14:20:05",
            price: "1.0862",
            tagPrice: "1.0862",
            delta: "+0.18% (+0.0019)",
            equity: "$50 000.00 (0.00%)",
            pnl: "$0.00 (пауза)",
            cardMetric: "Бары прочитаны",
            priceY: 44,
            wickTop: 38,
            bodyY: 42,
            bodyH: 12,
            decision: "14:20:05 · Режим изучения рынка без торговли: сформирована сводка по 240 закрытым барам M30 EURUSD, ключевое сопротивление 1.0864.",
            topLog: { time: "14:20:05", badge: "РЫНОК", kind: "mkt", msg: "Сводка по закрытым барам M30 сохранена в журнал агента (котировка <strong>1.0862</strong>)." }
          },
          {
            clock: "14:20:08",
            price: "1.0863",
            tagPrice: "1.0863",
            delta: "+0.19% (+0.0020)",
            equity: "$50 000.00 (0.00%)",
            pnl: "$0.00 (пауза)",
            cardMetric: "Бары прочитаны",
            priceY: 42,
            wickTop: 36,
            bodyY: 40,
            bodyH: 13,
            decision: "14:20:08 · Проверка готовности: терминал и демо-счёт MT5 Demo · DEMO-02 готовы; для перехода к сделкам требуется явное действие пользователя «Запустить торговлю».",
            topLog: { time: "14:20:08", badge: "ГОТОВ", kind: "ok", msg: "Готовность подтверждена: сделки не открываются автоматически без команды старта." }
          }
        ],
        baseLogs: [
          { time: "14:10:00", badge: "РЫНОК", kind: "mkt", msg: "Завершено чтение истории M30 EURUSD: волатильность сессии 52 пункта." },
          { time: "14:04:22", badge: "ГОТОВ", kind: "ok", msg: "Профиль «EUR · Диапазон M30» синхронизирован с каталогом стратегий." },
          { time: "13:50:15", badge: "СТОП", kind: "sl", msg: "Правила риска проверены: максимальный риск на сделку ограничен 0.40%." }
        ]
      }
    };

    var currentProfileKey = "xau-h1";
    var tickIndex = 0;
    var prefersReducedMotion = false;
    try {
      prefersReducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    } catch (e) {
      prefersReducedMotion = false;
    }

    var isManuallyPaused = prefersReducedMotion;
    var timerId = null;

    function setText(id, value) {
      var el = document.getElementById(id);
      if (el) {
        el.textContent = value;
      }
    }

    function setHtml(id, value) {
      var el = document.getElementById(id);
      if (el) {
        el.innerHTML = value;
      }
    }

    function renderLogList(topLog, baseLogs) {
      var listEl = document.getElementById("pult-log-list");
      if (!listEl) {
        return;
      }
      var allLogs = [topLog].concat(baseLogs);
      var html = allLogs
        .map(function (item, idx) {
          var freshClass = idx === 0 ? " is-fresh" : "";
          return (
            '<li class="pult-log-item' +
            freshClass +
            '">' +
            '<span class="pult-log-item__time">' +
            item.time +
            "</span>" +
            '<span class="pult-log-item__badge pult-log-item__badge--' +
            item.kind +
            '">' +
            item.badge +
            "</span>" +
            '<span class="pult-log-item__msg">' +
            item.msg +
            "</span>" +
            "</li>"
          );
        })
        .join("");
      listEl.innerHTML = html;
    }

    function renderTick() {
      var profile = PROFILES[currentProfileKey];
      if (!profile) {
        return;
      }
      var tick = profile.ticks[tickIndex % profile.ticks.length];

      setText("pult-demo-clock", tick.clock);
      setText("pult-market-price", tick.price);
      setText("pult-market-delta", tick.delta);
      setText("pult-acc-equity", tick.equity);
      setText("pult-pos-current", tick.price);
      setText("pult-pos-pnl", tick.pnl);
      setText("pult-decision-text", tick.decision);

      if (currentProfileKey === "xau-h1") {
        setText("pult-card-metric-xau-h1", tick.cardMetric);
      }

      // Обновление SVG-графика
      var priceLine = document.getElementById("pult-price-line");
      var priceTagBg = document.getElementById("pult-price-tag-bg");
      var priceTagTxt = document.getElementById("pult-price-tag-txt");
      var liveWick = document.getElementById("pult-live-wick");
      var liveBody = document.getElementById("pult-live-body");

      if (priceLine) {
        priceLine.setAttribute("y1", String(tick.priceY));
        priceLine.setAttribute("y2", String(tick.priceY));
      }
      if (priceTagBg) {
        priceTagBg.setAttribute("y", String(tick.priceY - 10));
      }
      if (priceTagTxt) {
        priceTagTxt.setAttribute("y", String(tick.priceY + 4));
        priceTagTxt.textContent = tick.tagPrice;
      }
      if (liveWick) {
        liveWick.setAttribute("y1", String(tick.wickTop));
      }
      if (liveBody) {
        liveBody.setAttribute("y", String(tick.bodyY));
        liveBody.setAttribute("height", String(tick.bodyH));
      }

      renderLogList(tick.topLog, profile.baseLogs);
    }

    function renderProfile(profileKey) {
      var profile = PROFILES[profileKey];
      if (!profile) {
        return;
      }
      currentProfileKey = profileKey;
      tickIndex = 0;

      profileCards.forEach(function (card) {
        var isMatch = card.getAttribute("data-agent-profile") === profileKey;
        card.classList.toggle("is-selected", isMatch);
        card.setAttribute("aria-selected", String(isMatch));
      });

      setText("pult-active-name", profile.name);
      var activeBadge = document.getElementById("pult-active-badge");
      if (activeBadge) {
        activeBadge.textContent = profile.badgeText;
        activeBadge.className = profile.badgeClass;
      }

      setHtml("pult-studio-banner", profile.studioBanner);
      setText("pult-spec-symbol", profile.symbol);
      setText("pult-spec-tf", profile.tf);
      setText("pult-spec-account", profile.account);
      setText("pult-spec-contour", profile.contour);
      setText("pult-spec-terminal", profile.terminal);
      setText("pult-spec-llm", profile.llm);
      setText("pult-spec-strategy", profile.strategy);
      setText("pult-spec-risk", profile.risk);

      setText("pult-market-label", profile.marketLabel);
      setText("pult-market-state", profile.marketState);
      setHtml("pult-market-session", profile.marketSession);
      setHtml("pult-market-bars", profile.marketBars);

      setText("pult-acc-id", profile.account);
      setText("pult-acc-balance", profile.accBalance);
      setText("pult-acc-pos", profile.accPos);
      setText("pult-acc-dd", profile.accDd);
      setText("pult-acc-limit", profile.accLimit);

      setText("pult-actions-title", profile.actionsTitle);
      setText("pult-run-state-pill", profile.runPillText);
      setHtml("pult-ops-summary", profile.opsSummary);

      setText("pult-log-title", profile.logTitle);
      setText("pult-pos-badge", profile.posBadge);
      setText("pult-pos-instrument", profile.posInstrument);
      setText("pult-pos-ticket", profile.posTicket);
      setText("pult-pos-entry", profile.posEntry);
      setText("pult-pos-sl", profile.posSl);
      setText("pult-pos-tp", profile.posTp);

      setText("pult-chart-entry-text", profile.chartEntryLabel);
      setText("pult-chart-sl-text", profile.chartSlLabel);

      renderTick();
    }

    function updateControlUI() {
      if (isManuallyPaused) {
        toggleBtn.textContent = "Воспроизвести";
        toggleBtn.setAttribute("aria-pressed", "true");
        if (statusWrap) {
          statusWrap.classList.add("is-paused");
        }
        if (statusText) {
          statusText.textContent = "Демо-анимация на паузе";
        }
      } else {
        toggleBtn.textContent = "Пауза";
        toggleBtn.setAttribute("aria-pressed", "false");
        if (statusWrap) {
          statusWrap.classList.remove("is-paused");
        }
        if (statusText) {
          statusText.textContent = "Демо-обновление активно";
        }
      }
    }

    function stopTimer() {
      if (timerId !== null) {
        clearInterval(timerId);
        timerId = null;
      }
    }

    function startTimerIfAllowed() {
      stopTimer();
      if (isManuallyPaused || document.hidden) {
        return;
      }
      timerId = setInterval(function () {
        if (document.hidden || isManuallyPaused) {
          return;
        }
        tickIndex += 1;
        renderTick();
      }, 2800);
    }

    toggleBtn.addEventListener("click", function () {
      isManuallyPaused = !isManuallyPaused;
      updateControlUI();
      startTimerIfAllowed();
    });

    profileCards.forEach(function (card, index) {
      card.addEventListener("click", function () {
        var key = card.getAttribute("data-agent-profile");
        if (key) {
          renderProfile(key);
        }
      });

      card.addEventListener("keydown", function (event) {
        if (event.key === "ArrowRight" || event.key === "ArrowLeft") {
          event.preventDefault();
          var dir = event.key === "ArrowRight" ? 1 : -1;
          var nextIndex = (index + dir + profileCards.length) % profileCards.length;
          var nextCard = profileCards[nextIndex];
          if (nextCard) {
            nextCard.focus();
            var nextKey = nextCard.getAttribute("data-agent-profile");
            if (nextKey) {
              renderProfile(nextKey);
            }
          }
        }
      });
    });

    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        stopTimer();
      } else {
        startTimerIfAllowed();
      }
    });

    updateControlUI();
    renderProfile(currentProfileKey);
    startTimerIfAllowed();
  }

  initPultDemo();
})();

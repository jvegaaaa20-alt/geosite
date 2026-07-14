# 🔥 Landing Page для модели

Красивый лендинг с видео или фото фоном и кнопкой. Автоматически отправляет нужное гео на твою ссылку, остальных — на другую.

---

## Как это работает

Человек заходит на сайт → система определяет его страну → если страна из твоего списка → переходит на твою основную ссылку → все остальные идут на запасную ссылку.

---

## Нужные сервисы

Зарегистрируйся заранее на всех:

| Сервис | Для чего | Ссылка |
|--------|----------|--------|
| GitHub | Хранение кода | [github.com](https://github.com) |
| Railway | Хостинг сайта | [railway.app](https://railway.app) |
| Cloudinary | Хостинг видео | [cloudinary.com](https://cloudinary.com) |
| imgbb | Хостинг фото | [imgbb.com](https://imgbb.com) |
| Namecheap | Купить домен | [namecheap.com](https://namecheap.com) |
| Google Analytics | Аналитика | [analytics.google.com](https://analytics.google.com) |

---

## Шаг 1 — Скопируй репозиторий

1. Нажми зелёную кнопку **Use this template** вверху страницы
2. Нажми **Create a new repository**
3. Придумай название (например `my-landing`) → нажми **Create repository**

---

## Шаг 2 — Подготовь медиафайл для фона

### Вариант А — Видео (рекомендуется)

**Требования к видео:**
- Формат: `.mp4`
- Соотношение сторон: вертикальное `9:16` (как Reels/TikTok)
- Размер: до 50 МБ
- Длина: 10-30 секунд (будет крутиться по кругу)

**Если видео в формате `.MOV` (iPhone) — сконвертируй:**

Открой Терминал на Маке и выполни:
```bash
# Установи ffmpeg если нет
brew install ffmpeg

# Конвертируй
ffmpeg -i твоё_видео.MOV -vcodec h264 -acodec aac -movflags faststart video.mp4
```

**Куда загрузить видео:**

1. Зайди на [cloudinary.com](https://cloudinary.com) → зарегистрируйся бесплатно
2. **Media Library** → **Upload** → загрузи `video.mp4`
3. Кликни на видео → скопируй **URL** вида:
```
https://res.cloudinary.com/твой-id/video/upload/имя_файла.mp4
```

> Если Cloudinary не работает — используй свой video-cdn на Railway (см. раздел ниже)

---

### Вариант Б — Фото

**Требования к фото:**
- Формат: `.jpg` или `.png`
- Соотношение сторон: вертикальное `9:16` для мобильных (например 1080×1920 пикселей)
- Размер: до 5 МБ

**Куда загрузить фото:**

1. Зайди на [imgbb.com](https://imgbb.com)
2. Нажми **Start uploading** → выбери фото
3. После загрузки скопируй **Direct link** вида:
```
https://i.ibb.co/xxxxxxxx/имя_файла.jpg
```

---

## Шаг 3 — Задеплой на Railway

1. Зайди на [railway.app](https://railway.app) → войди через GitHub
2. Нажми **New Project** → **Deploy from GitHub repo**
3. Выбери свой репозиторий → нажми **Deploy Now**
4. Подожди 2-3 минуты пока задеплоится
5. Зайди в сервис → **Settings** → **Networking** → **Generate Domain** → скопируй свой URL

---

## Шаг 4 — Заполни настройки (Variables)

Railway → твой проект → нажми на сервис → вкладка **Variables** → **Raw Editor** → вставь и заполни:

```
SITE_NAME=Lily
SITE_SUBTITLE=Check my exclusive content ❤️
HERO_URL=https://ссылка-на-видео-или-фото
CTA_TEXT=Exclusive content here
MAIN_LINK=https://t.me/+твоя_ссылка
FALLBACK_LINK=https://t.me/+твоя_ссылка
ALLOWED_GEO=US,GB,CA,AU,DE,FR,IT,NL,CH,AT,SE,NO,DK,FI,PT
GA_ID=
```

**Описание каждой переменной:**

| Переменная | Что писать | Пример |
|-----------|-----------|--------|
| `SITE_NAME` | Имя на сайте | `Lily` |
| `SITE_SUBTITLE` | Текст под именем (можно оставить пустым) | `Check my exclusive content ❤️` |
| `HERO_URL` | Ссылка на видео `.mp4` или фото `.jpg` | `https://res.cloudinary.com/.../video.mp4` |
| `CTA_TEXT` | Текст кнопки | `Exclusive content here` |
| `MAIN_LINK` | Ссылка для платёжеспособного гео | `https://t.me/+xxxxxxx` |
| `FALLBACK_LINK` | Ссылка для всех остальных (можно ту же) | `https://t.me/+xxxxxxx` |
| `ALLOWED_GEO` | Страны через запятую (коды ISO) | `US,GB,CA,AU,DE,FR` |
| `GA_ID` | Google Analytics ID (необязательно) | `G-XXXXXXXXXX` |

После заполнения нажми **Deploy** — сайт обновится автоматически.

---

## Шаг 5 — Настрой Google Analytics (необязательно)

Нужно если хочешь видеть откуда приходит трафик, какие страны, сколько кликов по кнопке.

1. Зайди на [analytics.google.com](https://analytics.google.com)
2. Нажми **Создать** → **Аккаунт** → придумай название
3. Создай **Ресурс** → введи название сайта → выбери **Веб**
4. Введи URL своего сайта → нажми **Создать поток**
5. Скопируй **Идентификатор** вида `G-XXXXXXXXXX`
6. Вставь его в Railway переменную `GA_ID`

**Что отслеживается автоматически:**
- Количество посетителей
- Страны откуда приходят
- Устройства (телефон/компьютер)
- Клики по кнопке (событие `click → button`)

Данные появятся в GA4 через 24-48 часов после первых визитов.

---

## Шаг 6 — Проверь что всё работает

Открой в браузере:
```
https://твой-сайт.up.railway.app/check
```

Увидишь ответ вида:
```json
{"ip": "1.2.3.4", "country": "DE", "allowed": true}
```

- `country` — твоя страна
- `allowed: true` — ты попадаешь на MAIN_LINK
- `allowed: false` — ты попадаешь на FALLBACK_LINK

---

## Шаг 7 — Свой домен (необязательно)

**Купить домен:**
1. Зайди на [namecheap.com](https://namecheap.com)
2. Введи желаемое имя в поиск → купи `.com` (~$9/год)
3. При оплате введи промокод `NEWCOM679` для скидки

**Подключить к Railway:**
1. Railway → твой сервис → **Settings** → **Networking** → **Custom Domain**
2. Введи домен → нажми **Add Domain**
3. Railway покажет две записи — CNAME и TXT
4. Namecheap → твой домен → **Manage** → **Advanced DNS**
5. Удали все существующие записи типа CNAME и URL Redirect
6. Добавь новые записи:

| Type | Host | Value |
|------|------|-------|
| CNAME | @ | значение из Railway |
| TXT | _railway-verify | значение из Railway |

7. Нажми **Save All Changes** → жди 10-30 минут

---

## Коды стран для ALLOWED_GEO

**Tier 1 — самые платёжеспособные:**
```
US, GB, CA, AU
```

**Tier 2 — Западная Европа:**
```
DE, FR, NL, CH, AT, SE, NO, DK, FI, BE, IE
```

**Дополнительно:**
```
JP, KR, PT, ES, IT, SG, NZ
```

**Пример для максимального охвата:**
```
ALLOWED_GEO=US,GB,CA,AU,DE,FR,IT,NL,CH,AT,SE,NO,DK,FI,PT,JP,KR,BE,IE,SG,NZ
```

---

## Как добавить второй сайт для другой модели

1. Railway → твой проект → **+ Add** → **GitHub Repo**
2. Выбери тот же репозиторий
3. Нажми **Deploy**
4. Заполни Variables с данными новой модели
5. Каждый сервис получит свой отдельный URL

---

## Как загрузить своё видео на Railway (альтернатива Cloudinary)

Если Cloudinary не работает — можно хостить видео прямо на Railway:

1. Создай новый репозиторий на GitHub `video-cdn`
2. Загрузи туда:
   - своё `video.mp4`
   - файл `main.py` (возьми из папки `video-cdn` этого репо)
   - `requirements.txt` и `Procfile`
3. Railway → **New Project** → выбери репо `video-cdn` → Deploy
4. Settings → Networking → Generate Domain
5. Твоя ссылка на видео:
```
https://video-cdn-xxx.up.railway.app/video.mp4
```

---

## Частые вопросы

**Сайт выдаёт ошибку сразу после деплоя?**
Подожди 2-3 минуты — Railway разворачивает сервис. Потом обнови страницу.

**Видео не играет на сайте?**
- Убедись что ссылка заканчивается на `.mp4`
- Открой ссылку напрямую в браузере — видео должно играть
- Если файл `.MOV` — сконвертируй через ffmpeg

**Кнопка не работает / никуда не ведёт?**
Проверь что `MAIN_LINK` заполнен в Variables и ссылка корректная.

**Домен показывает "Подключение не защищено"?**
Railway выдаёт SSL автоматически — подожди 10-30 минут после добавления DNS записей.

**Как поменять текст или дизайн?**
Редактируй файл `templates/index.html` прямо на GitHub — Railway обновит сайт автоматически.

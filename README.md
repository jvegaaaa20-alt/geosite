# Geo Landing Page

Лендинг с гео-фильтрацией. Пропускает только US, CA, DE, FR, IT, AU, GB. Остальным — 404.

## Структура
```
geosite/
├── app.py              # Flask бэкенд с гео-фильтром
├── requirements.txt
├── Procfile            # для Railway
└── templates/
    └── index.html      # лендинг (редактируй здесь)
```

## Что редактировать в index.html

1. **Имя** — найди `Your <span>Name</span>`, замени
2. **Фото аватарки** — раскомментируй `<img class="avatar" src="YOUR_PHOTO_URL">`, вставь URL
3. **Фото в сетке** — замени `<div class="placeholder-img">` на `<img src="URL">`
4. **Ссылки** — в каждом `.link-card` замени `href="#"`, иконку, title и desc
5. **TG CTA** — ссылка берётся автоматически из переменной окружения `TG_LINK`

## Деплой на Railway

1. Залей папку на GitHub
2. Railway → New Project → Deploy from GitHub → выбери репо
3. Variables → добавь:
   - `TG_LINK` = `https://t.me/твой_канал`
4. Railway сам подхватит Procfile и задеплоит

Railway даст домен: `https://твой-проект.up.railway.app`
Эту ссылку вставляй в рилсы.

## Дебаг

Зайди на `/check` — увидишь свой IP, страну и статус allowed/not.
Удали этот роут перед публикацией (в app.py закомментируй `/check`).

## Добавить/убрать страну

В `app.py`, строка:
```python
ALLOWED_GEO = {"US", "CA", "DE", "FR", "IT", "AU", "GB"}
```
Добавляй/убирай ISO-коды стран.

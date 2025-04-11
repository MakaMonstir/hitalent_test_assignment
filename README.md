# API бронирования столиков

Простое REST API для управления столиками и бронями в ресторане.

## ⚙️ Запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your_user/restaurant_api.git
cd restaurant_api
```

2. Запустите сервисы:

```bash
docker-compose up --build
```

API будет доступно на `http://localhost:8000`

## 📘 Документация

Swagger UI:  
[http://localhost:8000/docs](http://localhost:8000/docs)

## 💾 Миграции

Создание новой миграции:

```bash
alembic revision --autogenerate -m "create tables"
```

Применение миграций:

```bash
alembic upgrade head
```

## 🧪 Тесты

```bash
pytest
```

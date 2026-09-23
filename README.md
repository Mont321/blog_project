# Blog API

REST API для блога на Django REST Framework.

## 🛠 Технологии

- Python 3.14
- Django 6.1
- Django REST Framework
- PostgreSQL
- Token Authentication

## ✨ Возможности

- Регистрация и логин (токены)
- CRUD для постов
- Комментарии к постам
- Лайки постов
- Автор подставляется автоматически
- Только автор может редактировать/удалять свой пост

## 🚀 Запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/Mont321/blog_project.git
cd blog_project
```

2. Создать виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Создать базу данных PostgreSQL:
```sql
CREATE DATABASE blogdb;
```

5. Настроить `settings.py` (DATABASES).

6. Применить миграции:
```bash
python manage.py migrate
```

7. Создать суперпользователя:
```bash
python manage.py createsuperuser
```

8. Запустить сервер:
```bash
python manage.py runserver
```

## 📚 API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/api/register/` | Регистрация |
| POST | `/api/login/` | Логин (получить токен) |
| GET | `/api/posts/` | Список постов |
| POST | `/api/posts/` | Создать пост (нужен токен) |
| GET | `/api/posts/<id>/` | Один пост |
| PUT/PATCH | `/api/posts/<id>/` | Обновить (только автор) |
| DELETE | `/api/posts/<id>/` | Удалить (только автор) |
| GET | `/api/comments/` | Список комментариев |
| POST | `/api/comments/` | Создать комментарий |
| POST | `/api/likes/` | Поставить лайк |

## 🔐 Аутентификация

API использует **Token Authentication**.

При запросах, требующих авторизации, добавь заголовок:
```
Authorization: Token <твой_токен>
```

## 👤 Автор

Вилен — [GitHub](https://github.com/Mont321)
# Проекта Торговой Сети Электроники
Проект торговой сети электроники представляет собой веб-приложение, разработанное на Django и Django REST Framework (DRF), для управления иерархической структурой сети по продаже электроники. Включает в себя управление поставщиками и продуктами через админ-панель и API.

## Особенности
- Иерархическая структура: Поддержка иерархии сети из трех уровней: завод, розничная сеть и индивидуальный предприниматель.
- Управление поставщиками: Создание, просмотр, обновление и удаление (CRUD) информации о поставщиках через админ-панель и API. Обновление поля "Задолженность перед поставщиком" через API запрещено.
- Фильтрация по стране: Возможность фильтрации объектов по стране через API.
- Ограниченный доступ: Доступ к API ограничен только для активных сотрудников.
## Настройка и Запуск
### Предварительные требования
Для работы с проектом у вас должен быть установлен Python 3.8+ и pip. Также проект использует следующие технологии:

- Django 3.8+
- Django REST Framework 3.10+
- PostgreSQL 10+
### Установка
- Клонируйте репозиторий проекта.
- Создайте и активируйте виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
### Установите зависимости:
```
pip install -r requirements.txt
```
- Настройте соединение с базой данных в settings.py.
- Выполните миграции:
```
python manage.py makemigrations
python manage.py migrate
```
### Создайте суперпользователя:
```
python manage.py createsuperuser
```
### Запустите сервер разработки:
```
python manage.py runserver
```
## Использование
После запуска сервера доступ к админ-панели будет по адресу http://127.0.0.1:8000/admin/. Используйте учетные данные суперпользователя для входа.


## Тестирование
Для запуска тестов используйте команду:
```
python manage.py test app
```

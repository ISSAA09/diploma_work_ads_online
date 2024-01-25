# ADS Online

---
### Описание:

Данная работа представляет собой **backend-часть** для сайта объявлений (реализация с помощью Django Rest Framework и JWT).
<p>

**Frontend** часть готова (реализация - React)

------------------------------------------------------------------------------------------------

### Функционал:
- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

----------------------------------------------------------------
### Стэк

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-DRF-informational?style=flat&logo=Django&logoColor=white&color=green)
![](https://img.shields.io/badge/database-Postgresql-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)

### Технологии:
- Python
- Django
- Django REST framework
- psycopg2-binary
- JWT 
- DRF-YASG
- CORS
- Docker
- Docker Compose

------------------------------------------------------------------------------------------------

### Запуск проекта 
<h4>Локально:</h4>

1. Установить локально на свой компьютер Python версией не ниже 3.10.x!
2. Клонировать файлы проекта с GitHub репозитория:
- > https://github.com/ISSAA09/diploma_work_ads_online.git
3. Создать виртуальное окружение:
- `python -m venv venv`
4. Активировать виртуальное окружение:
- `venv/Scripts/activate (Windows)`
- `source venv/bin/activate (Linux, MacOS)`
5. Установить зависимости:
- `pip install -r requirements.txt`
6. Создать файл .env c переменными окружения.
7. Добавить в файл настройки, как в .env.sample и заполнить их.
8. Создайте базу данных, выполните `python skymarket/manage.py migrate`. 
9. Заполнить базу данных:
- `python skymarket/manage.py loaddata skymarket/fixtures/users.json` 
- `python skymarket/manage.py loaddata skymarket/fixtures/ad.json` 
- `python skymarket/manage.py loaddata skymarket/fixtures/comments.json`
10. Создайте администратора, выполните `python skymarket/manage.py csu`. 
11. Запустите сервер разработки, выполните `python skymarket/manage.py runserver`. 
12. Перейдите в веб-браузере по адресу http://localhost:8000 и вы увидите главную страницу сервиса.

<h4>Запуск проекта через docker-compose:</h4>

1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.sample
4. Соберите образ с помощью команды `docker-compose build`
5. Запустите контейнеры с помощью команды `docker-compose up`
> Сборка и запуск контейнера в фоновом режиме:
> docker-compose up -d --build

--------------------------------------------------

### Техническое задание:

- **Этап I.** Настройка Django-проекта.
- **Этап II.** Создание модели юзера. Настройка авторизации и аутентификации.
- **Этап III.** Описание моделей объявлений и отзывов.
- **Этап IV.** Создание views и эндпоинтов.
- **Этап V**. Определение permissions к views.
----------------------------------------------------------------

### Авторы

ISSAA09

----------------------------------------------------------------
### Связь с авторами

https://github.com/ISSAA09


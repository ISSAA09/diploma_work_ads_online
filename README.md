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

**Клонируем проект по ссылке:**
> https://github.com/ISSAA09/diploma_work_ads_online.git

### Через docker
Создаем контейнер:
> docker build -t my-python-app .

Запускаем:
> docker run my-python-app


### Через docker compose
- Сборка и запуск контейнера в фоновом режиме:
> docker-compose up -d --build

--------------------------------------------------

### Техническое задание:

- **Этап I.** Настройка Django-проекта.
- **Этап II.** Создание модели юзера. Настройка авторизации и аутентификации.
- **Этап III.** Описание моделей объявлений и отзывов.
- **Этап IV.** Создание views и эндпоинтов.
- **Этап V**. Определение permissions к views.
----------------------------------------------------------------



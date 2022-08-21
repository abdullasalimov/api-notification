API для системы сервиса уведомлений
=====


Описание проекта
----------

API сервис реализуется на базе фреймворка DRF.


Стек технологий
----------
* Python
* Django
* Django Rest Framework
* PostreSQL
* Сelery
* Redis

Установка проекта из репозитория
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/abdullasalimov/api-notification

cd api-notification
```

2. Cоздать и открыть файл ```.env``` с переменными окружения:


3. Заполнить ```.env``` файл с переменными окружения по примеру:
```bash 
DB_ENGINE=django.db.backends.postgresql
DB_NAME=******************
POSTGRES_PASSWORD=******************
POSTGRES_USER=******************
DB_HOST=localhost
DB_PORT=5432
BROKER=redis://redis
BROKER_URL=redis://redis:6379/0
```
Токен
```bash 
SENDING_API_TOKEN=******************
```

4. Установите необходимые пакеты для проекта:
```bash 
pip install -r requirements.txt
```

5. Запуск миграций:
```bash 
python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --no-input 
```

Root
```http://127.0.0.1/```
API
```http://127.0.0.1/api/```

Документация к проекту
----------
Документация для API после установки доступна по адресу: 

```http://127.0.0.1/docs/```

```http://127.0.0.1/redoc/```

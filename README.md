## Описание проекта

Foodgram это ресурс для публикации рецептов.  
Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в pdf формате

## Установка проекта локально

* Склонировать репозиторий на локальную машину:
```bash
git clone https://github.com/Savich19/foodgram-project-react.git
cd foodgram-project-react
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source venv/Scripts/activate
```

* Cоздайте файл `.env` в директории `/infra/` с содержанием:

```
SECRET_KEY=секретный ключ django
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=DB_password
DB_HOST=db
DB_PORT=5432
```

* Перейти в директирию и установить зависимости из файла requirements.txt:

```bash
cd backend/
pip install -r requirements.txt
```

* Выполните миграции:

```bash
python manage.py migrate
```

* Запустите сервер:
```bash
python manage.py runserver
```

## Запуск проекта в Docker контейнере
* Установите Docker.

Параметры запуска описаны в файлах `docker-compose.yml` и `nginx.conf` которые находятся в директории `infra/`.  
При необходимости добавьте/измените адреса проекта в файле `nginx.conf`

* Запустите docker compose:
```bash
docker-compose up -d --build
```  
  > После сборки появляются 3 контейнера:
  > 1. контейнер базы данных **db**
  > 2. контейнер приложения **backend**
  > 3. контейнер web-сервера **nginx**
* Примените миграции:
```bash
docker-compose exec backend python manage.py migrate
```
* Загрузите ингредиенты:
```bash
docker-compose exec backend python manage.py load_data
```
* Загрузите теги:
```bash
docker-compose exec backend python manage.py load_tags
```
* Создайте администратора:
```bash
docker-compose exec backend python manage.py createsuperuser
```
* Соберите статику:
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

## Сайт
Сайт доступен по ссылке:
[http://62.84.117.165/](http://62.84.117.165/)

## Документация к API
API документация доступна по ссылке (создана с помощью redoc):
[http://62.84.117.165/api/docs/](http://62.84.117.165/api/docs/)

## Стандартная админ-панель Django
Стандартная админ-панель Django доступна по адресу [http://62.84.117.165/admin/](http://62.84.117.165/admin/)

## Авторы
[Савич А.В.](https://github.com/Savich19) Бэкенд для сервиса Foodgram.
[Яндекс.Практикум](https://github.com/yandex-praktikum) Фронтенд для сервиса Foodgram.

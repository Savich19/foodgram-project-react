FROM python:3.7-slim

WORKDIR /app

# Скопировать с локального компьютера файл зависимостей в директорию /app.
COPY requirements.txt ./

# Выполнить установку зависимостей внутри контейнера.
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# Скопировать содержимое директории c локального компьютера в директорию /app.
COPY ./ ./

# Выполнить запуск сервера разработки при старте контейнера.
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]

# Финальный проект спринта: приложение QRKot
## Описание
Проект QRKot — это приложение для Благотворительного фонда поддержки котиков на FastAPI.

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.

## Технологии и  и библиотеки
```
    Python;
    FastAPI;
    SQLAlchemy;
    Alembic;
    Uvicorn;
    FastAPI Users;
```

### 1. Перед использованием
Клонируйте репозиторий к себе на компьютер:
```
git clone git@github.com:Kirill-kuz/cat_charity_fund.git
```
Перейдите в папку.
```
cd cat_charity_fund
```
В корневой папке создайте виртуальное окружение и установите зависимости.
```
python -m venv venv
```
```
source venv/scripts/activate
```
```
pip install -r requirements.txt
```


### 2. Создайте файл .env, в корне проекта выполните команду:
```
mv .env.example .env
```
### 3. Примените миграции
```
alembic upgrade head
```
### 4. Запуск проекта
```
uvicorn main:app
```
или запуск сервера с автоматическим рестартом
```
uvicorn main:app --reload
```
### 5. API
Сервис является API, так что может быть интегрирован в вашу систему.

Для регистрации выполните POST запрос на http://127.0.0.1:8000/auth/register:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/auth/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user@example.com",
  "password": "your_password"
  }'
```
Для аутентификации и получения токена выполните POST запрос на http://127.0.0.1:8000/auth/jwt/login
```
curl -X 'POST' \
  'http://127.0.0.1:8000/auth/jwt/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=username&password=password&scope=&client_id=&client_secret='
```
Пример ответа в случае успешного выполнения:
```
{
  "access_token": "token",
  "token_type": "bearer"
}
```
Далее используйте этот токен при запросах к сервису.

#### *[/swagger](http://127.0.0.1:8000/swagger/)*
#### *[/redoc](http://127.0.0.1:8000/redoc)*
### Автор
Кирилл Кузнецов https://github.com/Kirill-kuz
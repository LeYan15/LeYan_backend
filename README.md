![leyan_workflow](https://github.com/LeYan15/LeYan_backend/actions/workflows/leyan_workflow.yml/badge.svg)

# ...

## Описание проекта
Интерфейс прогноза спроса на 14 дней для товаров собственного производства с использованием гранулярности ТК-SKU-День.

Прогноз позволит повысить доступность и продажи в ТК без повышения списаний и повышение маржинальности.
При изготовлении товаров СП сотрудники будут ориентироваться не на экспертный подход, а на ML прогноз спроса, в соответствии с которым будут изготавливать продукцию и планировать заказы сырья.

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 	![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)  ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) ![DjDT](https://img.shields.io/badge/DjDT-4.2.0-gold)


## Инструкция по запуску локально и в контейнере

### Склонируйте репозиторий и перейдите в него:
```sh
git clone https://github.com/LeYan15/LeYan_backend.git
```
```sh
cd backend
```
### Заполните .env данными для PostgreSQL:
Создайте в директории `infra` файл `.env` командой:
```sh
touch infra/.env
```
Заполните переменные по примеру файла `.env.example`

### Создайте и активируйте виртуальное окружение:
```sh
python -m venv venv
```

* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```

* Если у вас windows
    ```
    source venv/scripts/activate
    ```

### Обновите pip и установите зависимости:
```sh
python -m pip install --upgrade pip
```

```sh
pip install -r backend/requirements.txt
```

## Для локального запуска используйте следующую инструкцию

### Выполните миграции:

* Инициализируйте миграции
```sh
python backend/manage.py migrate
```

* Создайте миграции
```sh
python backend/manage.py makemigrations shop
```
```sh
python backend/manage.py makemigrations product
```
```sh
python backend/manage.py makemigrations sale
```
```sh
python backend/manage.py makemigrations forecast
```

* Примените миграции
```sh
python backend/manage.py migrate
```

### Создайте суперюзера

```sh
python backend/manage.py createsuperuser
```
Данные супер юзера для примера:
```
username: admin
mail: admin@admin.ru
password: admin
password (again): admin
```

### Наполните базу данными

* Команды для выгрузки данных из csv-файлов:
```sh
python backend/manage.py parse_product
```
```sh
python backend/manage.py parse_shops
```
```sh
python backend/manage.py parse_sales
```

PS Для удаления данных из базы, используейте дополнительную опцию ```--delete``` и для помощи ```--h```:
```sh
python backend/manage.py <команда> --delete
```


## Для запуска в контейнере используйте следующую инструкцию

### Подготовьте репозиторий на GitHub

В репозитории на GitHub пропишите в разделе Secrets > Actions:
```sh
DOCKER_USERNAME - имя пользователя DockerHub
DOCKER_PASSWORD - пароль пользователя DockerHub
HOST - IP сервера
USER - текущий пользователь
SSH_KEY - приватный ssh-ключ (начало -----BEGIN OPENSSH PRIVATE KEY----- ... -----END OPENSSH PRIVATE KEY----- конец)
PASSPHRASE - кодовая фраза для ssh-ключа (если ваш ssh-ключ защищён фразой-паролем)
```

### Запустите сборку образа в директории backend:
```
docker build -t leyan .
```
### Запустите сборку контейнеров:
```
docker-compose up -d --build
```
### Перейдите в контейнер
```
docker container exec -it <CONTAINER ID> bash #возьмите ID контейнера проекта
```
### Посмотрите список миграций
```
python manage.py showmigrations
```

### Соберите статистику
```
python manage.py collectstatic --no-input
```


## Адрес админки проекта
*(запускается локально)*
```
http://127.0.0.1:8000/admin/
```

## Адрес проекта
*(запускается локально)*
```
http://127.0.0.1:8000/
```

## Документация
```
http://127.0.0.1:8000/swagger/
```

### Handlers
```
get, /categories # Возвращает товарную иерархию.
get, /sales # Возвращает временной ряд с информацией о количестве проданных товаров. Обязательные входные параметры запроса: id товара, id ТЦ.
get, /shops # Возвращает список ТЦ. Можно добавить фильтры по полям (например, тип, локация, др).
post, /forecast # Принимает спрогнозированные значения для данного товара и данного ТЦ, сохраняет в БД. В теле запроса необходимо отправить JSON файл.
get, /forecast # Возвращает спрогнозированные значения для данного товара и данного ТЦ из сохранённых в БД значений.
```

### Команда проекта

**Проджект**:
- Алёна Станиславская ([@helena_stanislavskaya ](https://t.me/@helena_stanislavskaya))

**Дизайнеры**:
- Малеева Евгения ([@eugenia_maleeva](https://t.me/eugenia_maleeva), **[Eugenia-mei](https://github.com/Eugenia-mei)**)
- Токарский Илья ([@tokarsky_ilya](https://t.me/tokarsky_ilya), **[marolfox](https://github.com/marolfox)**)
- Черкасова Лола ([@lola_cherkasovaa](https://t.me/lola_cherkasovaa), **[...](https://github.com/...)**)

**DS**:
- Киселев Владимир ([@vks1v](https://t.me/vks1v), **[vkslv](https://github.com/vkslv)**)
- Шабров Роман ([@Ekwizor](https://t.me/Ekwizor), **[ekwizor](https://github.com/ekwizor)**)
- Шапиев Магомед ([@ShaurMau](https://t.me/ShaurMau), **[MagomedShapiev](https://github.com/MagomedShapiev)**)

**Backend-разработчики**:
- Оскалов Лев ([@oskalov](https://t.me/oskalov), **[Oskalovlev](https://github.com/Oskalovlev)**)
- Егорова Карина ([@Karina_eg](https://t.me/Karina_eg), **[Karina-Rin](https://github.com/Karina-Rin)**)

**Frontend-разработчики**:
- Никулин Александр ([@alix1982_tg](https://t.me/alix1982_tg), **[alix1982](https://github.com/https://github.com/alix1982)**)
- Табишева Ольга ([@oloatab](https://t.me/oloatab), **[OlgaTabisheva](https://github.com/OlgaTabisheva)**)

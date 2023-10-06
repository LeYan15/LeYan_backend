![leyan_workflow](https://github.com/LeYan15/LeYan_backend/actions/workflows/leyan_workflow.yml/badge.svg)

# ...

## Описание проекта
Интерфейс прогноза спроса на 14 дней для товаров собственного производства с использованием гранулярности ТК-SKU-День.

Прогноз позволит повысить доступность и продажи в ТК без повышения списаний и повышение маржинальности.
При изготовлении товаров СП сотрудники будут ориентироваться не на экспертный подход, а на ML прогноз спроса, в соответствии с которым будут изготавливать продукцию и планировать заказы сырья.

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 	![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)  ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) ![DjDT](https://img.shields.io/badge/DjDT-4.2.0-gold)


## Инструкция по сборке и запуску
1. Склонируйте репозиторий и перейдите в него:
```
git clone https://github.com/LeYan15/LeYan_backend.git
```
```
cd backend
```
2. Создайте в директории `infra` файл `.env` с переменными окружения для работы
с БД по примеру файла `.env.example`

3. Создайте и активируйте виртуальное окружение, обновите pip:
```
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

4. Установите зависимости:
```
pip install -r requirements.txt
```
5. Подготовьте репозиторий на GitHub

В репозитории на GitHub пропишите в разделе Secrets > Actions:
```
DOCKER_USERNAME - имя пользователя DockerHub
DOCKER_PASSWORD - пароль пользователя DockerHub
HOST - IP сервера
USER - текущий пользователь
SSH_KEY - приватный ssh-ключ (начало -----BEGIN OPENSSH PRIVATE KEY----- ... -----END OPENSSH PRIVATE KEY----- конец)
PASSPHRASE - кодовая фраза для ssh-ключа (если ваш ssh-ключ защищён фразой-паролем)
TELEGRAM_TO - ID своего телеграм-аккаунта. Узнать можно у бота `@userinfobot`
TELEGRAM_TOKEN - токен вашего бота. Получить можно у бота `@BotFather`
```

6. Запустите сборку образа в директории backend:
```
docker build -t leyan .
```
7. Запустите сборку контейнеров:
```
docker-compose up -d --build
```
8. Перейдите в контейнер
```
docker container exec -it <CONTAINER ID> bash #возьмите ID контейнера проекта
```
9. Посмотрите список миграций
```
python manage.py showmigrations
```
10. Выполните миграции
```
python manage.py makemigrations
```
11. Примените миграции
```
python manage.py migrate
```
12. Соберите статистику
```
python manage.py collectstatic --no-input
```
13. Наполните базу данными

Команды для выгрузки данных из csv-файлов:

```sh
python backend/manage.py parse_product
```
```sh
python backend/manage.py parse_shops
```
```sh
python backend/manage.py parse_sales
```
Для удаления данных из базы используейте дополнительную опцию ```--delete```, для помощи ```--h```:
```sh
python backend/manage.py <команда> --delete
```
14. Создайте суперюзера
```
python manage.py createsuperuser
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

![leyan_workflow](https://github.com/LeYan15/LeYan_backend/actions/workflows/leyan_workflow.yml/badge.svg)

## Описание проекта
Интерфейс прогноза спроса на 14 дней для товаров собственного производства с использованием гранулярности ТК-SKU-День.

Прогноз позволит повысить доступность и продажи в ТК без повышения списаний и повышение маржинальности.
При изготовлении товаров СП сотрудники будут ориентироваться не на экспертный подход, а на ML прогноз спроса, в соответствии с которым будут изготавливать продукцию и планировать заказы сырья.

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 	![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)  ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![DjDT](https://img.shields.io/badge/DjDT-4.2.0-gold)

<details><summary><h2>Структура проекта</h2></summary>
    <details><summary><h4>Структура базы данных</h4></summary>
        <img src="https://github.com/LeYan15/LeYan_backend/blob/main/docs/BD_LeYan.jpg"/>
    </details>
</details>

---

<details><summary><h2>Адрес проекта</h2></summary>

*(запускается локально)*

    http://127.0.0.1:8000/

**Адрес админки проекта**

    http://127.0.0.1:8000/admin/

**Документация**

    http://127.0.0.1:8000/swagger/

**Handlers**

```sh
get, /product # Возвращает товарную иерархию.
get, /sales # Возвращает временной ряд с информацией о количестве проданных товаров. Обязательные входные параметры запроса: id товара, id ТЦ.
get, /shops # Возвращает список ТЦ. Можно добавить фильтры по полям (например, тип, локация, др).
post, /forecast # Принимает спрогнозированные значения для данного товара и данного ТЦ, сохраняет в БД. В теле запроса необходимо отправить JSON файл.
get, /forecast # Возвращает спрогнозированные значения для данного товара и данного ТЦ из сохранённых в БД значений.
```
</details>

---

<details><summary><h2>Подготовка проекта к запуску</h2></summary>

### `3` и `4` пункты для локального запуска

1. *Склонируйте репозиторий и перейдите в него*:

    ```sh
    git clone https://github.com/LeYan15/LeYan_backend.git
    ```
    ```sh
    cd leyan_backend/
    ```
---
2. *Для работы с PostgreSQL*:

    * Создайте в директории `infra/` файл `.env` командой:

        ```sh
        touch infra/.env
        ```
        > Заполните переменные по примеру файла `.env.example`
---
3. *Создайте и активируйте виртуальное окружение*:

    ```sh
    python -m venv venv
    ```
    - Если у вас Linux/macOS
        ```sh
        source venv/bin/activate
        ```

    - Если у вас windows
        ```sh
        source venv/scripts/activate
        ```
---
4. *Обновите pip и установите зависимости*:

    ```sh
    python -m pip install --upgrade pip
    ```
    ```sh
    pip install -r backend/requirements.txt
    ```
</details>

---

<details><summary><h2>Для запуска в Docker-контейнере используйте инструкцию</h2></summary>

1. *Запустите сборку контейнеров*:

    ```sh
    docker compose -f infra/docker-compose.yaml up -d --build
    ```
2. *Для остановки контейнера*:
    ```sh
    docker compose -f infra/docker-compose.yaml down
    ```
</details>

---

<details><summary><h2>Для локального запуска используйте инструкцию</h2></summary>

1. *Выполните миграции*:

    * Инициализируйте миграции
        ```sh
        python backend/manage.py migrate
        ```

    * Создайте миграции
        ```sh
        python backend/manage.py makemigrations user
        ```
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
---
2. *Создайте суперюзера*:

    ```sh
    python backend/manage.py createsuperuser
    ```

    > Для примера, данные суперюзера:

        username: admin
        mail: admin@admin.ru
        password: admin
        password (again): admin

---
3. *Наполните базу данными*:

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

    -    > Для удаления данных из базы есть доп. опция `--delete`:

            ```sh
            python backend/manage.py <команда> --delete
            ```
---
4. *Соберите статику*:
    ```sh
    python backend/manage.py collectstatic --noinput
    ```
---
5. *Локальный запуск*:

    ```sh
    python backend/manage.py runserver
    ```
</details>

---

### Команда проекта

**Проджект**:
- Алёна Станиславская ([@helena_stanislavskaya ](https://t.me/@helena_stanislavskaya))

**Дизайнеры**:
- Малеева Евгения ([@eugenia_maleeva](https://t.me/eugenia_maleeva), **[Eugenia-mei](https://github.com/Eugenia-mei)**)
- Токарский Илья ([@tokarsky_ilya](https://t.me/tokarsky_ilya), **[marolfox](https://github.com/marolfox)**)
- Черкасова Лола ([@lola_cherkasovaa](https://t.me/lola_cherkasovaa))

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

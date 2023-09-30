# Хакатон.Лента

## Описание проекта
Интерфейс прогноза спроса на 14 дней для товаров собственного производства с использованием гранулярности ТК-SKU-День.

## Стек технологий

- Python 3.11
- Docker
- Django DRF
- Swagger API
- Unitest
- Flask
- Jinja2

### ссылки на сторонние фреймворки, библиотеки, иконки и шрифты если использовались
![Python](https://img.shields.io/badge/Python-3.11-blue) ![Django](https://img.shields.io/badge/Django-3.2-green) ![DRF](https://img.shields.io/badge/DRF-3.12-orange)

## Инструкция по сборке и запуску
1. Склонируйте репозиторий и перейдите в него:
```
git clone https://github.com/LeYan15/LeYan_backend.git
```
```
cd backend
```
2. Создайте и активируйте виртуальное окружение
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

3. Установите зависимости:
```
pip install -r requirements.txt
```

4. Создайте в директории `infra` файл `.env` с переменными окружения для работы
с БД по примеру файла `.env.sample`

5. Создайте и проведите миграции в приложении Django
```
python manage.py makemigrations && python manage.py migrate
```

6.


7. Запускаем приложение:
```
python manage.py runserver
```


7. Запускаем сборку контейнеров:
```
docker-compose up -d --build
```
8. Выполняем миграции
```
python manage.py makemigrations
```
9. Применяем миграции
```
python manage.py migrate
```
10. Собираем статистику
```
python manage.py collectstatic --no-input
```




## тут будет ссылка на Github Pages или иной веб хостинг (если приложение опубликовано)


## Документация
```
http://localhost/swagger/
```


### Команда проекта

**Дизайнеры**:
- Малеева Евгения ([@eugenia_maleeva](https://t.me/eugenia_maleeva), **[...](https://github.com/...)**)
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

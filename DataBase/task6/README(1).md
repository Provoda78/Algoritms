# Практическое задание 6. Индексы и физическая организация

## Что делаем

На практике убеждаемся, что:

1.  B+ индекс радикально ускоряет поиск по столбцу (логарифмическая сложность vs линейная).
2.  `EXPLAIN (ANALYZE, BUFFERS)` показывает план, реальное время и работу с буферным пулом.
3.  Некоторые запросы не используют индекс: функция над столбцом, `LIKE '%...'`, низкая селективность.
4.  Частичный индекс экономит место и работает для редких условий.
5.  Покрывающий индекс (`INCLUDE`) позволяет не читать саму таблицу.
6.  Триграммы (`pg_trgm`) помогают для `LIKE '%...%'`.
7.  Bitmap Index Scan — как PostgreSQL комбинирует индекс и sequential read.

## Что нужно установить ЗАРАНЕЕ

1.  Docker Desktop — бесплатный.

- Windows: https://www.docker.com/products/docker-desktop/
- macOS: то же самое
- Linux: `sudo apt install docker.io docker-compose-v2` или через официальную инструкцию

При установке на Windows обязательно включить WSL 2 (Docker сам предложит).

2.  Python 3.10+ и `pip`.

3.  Проверьте установку:
    ```bash
    docker --version         # должно быть Docker version 24.x или новее
    python --version         # 3.10+
    ```

## Запуск инфраструктуры

Откройте терминал в папке `task6/` и выполните:

```bash
docker compose up -d
```

Скачается образ PostgreSQL 16 (~80 МБ) и запустится контейнер.
Проверьте:

```bash
docker compose ps
```

Должно быть `running` и `healthy`. Если статус `starting` — подождите 5–10 секунд.

### Как зайти внутрь базы (по желанию)

```bash
docker exec -it dbms_task2_postgres psql -U student -d employees_db
```

Внутри `psql` работает обычный SQL. Выход — `\q`.

## Установка Python-зависимостей

```bash
pip install -r requirements.txt
```

## Часть 1. Генерация данных

```bash
cd data
python generate_data.py
cd ..
```

Появится файл `data/employees_1m.csv` (~90 МБ, 1 млн записей).

Структура: `id, name, email, status, salary, dept_id`.
Особенность: только 1% записей имеют `status = 'active'` — это нужно для эксперимента с частичным индексом.

## Часть 2. Импорт без индексов

```bash
python import_data.py
```

Скрипт:

- удалит старую таблицу (если была),
- создаст схему,
- зальёт CSV через `COPY FROM` (быстро — 5–10 секунд),
- соберёт статистику через `ANALYZE`.

Запомните время импорта — оно выведется в консоль.

## Часть 3. Замеры без индексов

```bash
python benchmark.py
```

Скрипт для каждого из 8 запросов выведет:

- время выполнения (секунды),
- `shared hit` — сколько страниц взято из буфера,
- `shared read` — сколько прочитано с диска,
- план (первая значимая строка).

Обратите внимание: у запросов Q2–Q8 будет `Seq Scan employees`.
Это значит — СУБД читает всю таблицу.

## Часть 4. Импорт с индексами

```bash
python import_data.py --with-indexes
python benchmark.py
```

Что изменилось:

- Импорт стал дольше (индексы надо построить).
- У Q2, Q3 появилось `Index Scan using idx_...`.
- Q4, Q6 по-прежнему `Seq Scan` — индекс не подходит.

## Часть 5. Эксперименты с индексами

```bash
python explore_indexes.py
```

Пять экспериментов:

1.  Частичный индекс на `status = 'active'` — ускоряет, занимает мало места.
2.  Покрывающий индекс `INCLUDE (name)` — план становится `Index Only Scan`.
3.  Функциональный индекс `LOWER(name)` — заставляет работать Q4.
4.  Триграммы `pg_trgm` — ускоряют `LIKE '%...%'`.
5.  Bitmap Index Scan на выборке 10% — как PostgreSQL выбирает между `Seq Scan` и `Bitmap Scan`.

## Отчёт

Заполните `report_template.md`. Ответьте на все вопросы, приведите таблицы.

Сохраните как `report_ФАМИЛИЯ_ИМЯ.md` и отправьте в Telegram-чат.

## Остановка контейнера

Когда закончите (не удаляя данные):

```bash
docker compose stop
```

Полностью удалить (включая данные):

```bash
docker compose down -v
```

## Частые ошибки

### `Cannot connect to the Docker daemon`

Docker Desktop не запущен. Запустите его и подождите 30 секунд.

### `Port 5433 is already in use`

У вас уже что-то слушает порт 5433. Откройте `docker-compose.yml`, поменяйте `"5433:5432"` на `"5434:5432"` и `port: 5433` в Python-скриптах на `5434`.

### `psycopg2.OperationalError: connection refused`

Контейнер ещё не поднялся. Подождите и проверьте `docker compose ps`.

### `FileNotFoundError: employees_1m.csv`

Вы не запустили `generate_data.py` или находитесь не в папке `task6/`.

### Долгий импорт (> 1 минуты)

Это странно: `COPY FROM` для 1 млн строк должен занимать секунды. Проверьте, что у Docker выделено хотя бы 2 ГБ памяти (Docker Desktop → Settings → Resources).

### `permission denied for schema public` при `CREATE EXTENSION`

Пользователь `student` должен иметь права. В нашем `docker-compose.yml` он создаётся как `POSTGRES_USER` — это суперпользователь базы. Если ошибка всё же есть, выполните в `psql`:

```sql
GRANT ALL ON SCHEMA public TO student;
```

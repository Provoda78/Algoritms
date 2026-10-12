"""Создаёт таблицу и импортирует CSV через COPY FROM.

Использование:
    python import_data.py                  # без пользовательских индексов
    python import_data.py --with-indexes   # с индексами (name, dept_id, email)
"""
import sys
import time
import os
import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "database": "employees_db",
    "user": "student",
    "password": "student",
}

CSV_FILE = "employees_1m.csv"
CREATE_INDEXES = "--with-indexes" in sys.argv


def main():
    if not os.path.exists(CSV_FILE):
        print(f"Не найден файл {CSV_FILE}.")
        print("Сначала запустите: cd data && python generate_data.py")
        sys.exit(1)

    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = False
    cur = conn.cursor()

    print("Удаление старой таблицы...")
    cur.execute("DROP TABLE IF EXISTS employees CASCADE")
    conn.commit()

    print("Создание схемы...")
    cur.execute("""
        CREATE TABLE employees (
            id       INTEGER PRIMARY KEY,
            name     TEXT    NOT NULL,
            email    TEXT    NOT NULL,
            status   TEXT    NOT NULL,
            salary   INTEGER NOT NULL,
            dept_id  INTEGER NOT NULL
        )
    """)
    conn.commit()

    print("Импорт CSV через COPY...")
    t0 = time.time()
    with open(CSV_FILE, encoding="utf-8") as f:
        cur.copy_expert(
            "COPY employees FROM STDIN WITH (FORMAT CSV, HEADER TRUE)",
            f,
        )
    conn.commit()
    print(f"  Импорт завершён за {time.time() - t0:.1f} сек")

    # Обновляем статистику — критично для планировщика
    print("Сбор статистики (ANALYZE)...")
    cur.execute("ANALYZE employees")
    conn.commit()

    if CREATE_INDEXES:
        print("Создание индексов...")
        t0 = time.time()
        cur.execute("CREATE INDEX idx_name ON employees(name)")
        cur.execute("CREATE INDEX idx_dept ON employees(dept_id)")
        cur.execute("CREATE INDEX idx_email ON employees(email)")
        conn.commit()
        print(f"  Индексы созданы за {time.time() - t0:.1f} сек")
        cur.execute("ANALYZE employees")
        conn.commit()

    cur.close()
    conn.close()
    print("Готово.")


if __name__ == "__main__":
    main()
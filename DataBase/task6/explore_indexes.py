"""Эксперименты с индексами, которые «не работают в лоб».

Запускать ПОСЛЕ: python import_data.py --with-indexes
"""
import psycopg2
import time
import os

DB_CONFIG = {
    "host": "localhost", "port": 5433,
    "database": "employees_db", "user": "student", "password": "student",
}


def time_and_plan(c, sql):
    """Возвращает (время в секундах, план первой значимой строки)."""
    c.execute(f"EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) {sql}")
    rows = c.fetchall()
    lines = [r[0].strip() for r in rows]
    text = "\n".join(lines)

    exec_time = 0.0
    for line in text.splitlines():
        if "Execution Time:" in line:
            try:
                exec_time = float(line.split(":")[1].replace("ms", "").strip()) / 1000.0
            except ValueError:
                pass

    plan = "?"
    for line in lines:
        if line.startswith(("Seq Scan", "Index Scan", "Index Only Scan", "Bitmap")):
            plan = line
            break
    return exec_time, plan


def header(title):
    print()
    print("=" * 75)
    print(title)
    print("=" * 75)


def main():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True
    c = conn.cursor()

    # ============ 1. Partial index ============
    header("ЭКСПЕРИМЕНТ 1. Частичный индекс на редкое значение (1%)")
    sql = "SELECT * FROM employees WHERE status = 'active'"
    t, plan = time_and_plan(c, sql)
    print(f"До:    t = {t:.4f} с   план: {plan}")

    c.execute("CREATE INDEX idx_active ON employees(id) WHERE status = 'active'")
    c.execute("ANALYZE employees")
    t, plan = time_and_plan(c, sql)
    print(f"После: t = {t:.4f} с   план: {plan}")

    c.execute("""
        SELECT pg_size_pretty(pg_relation_size('idx_active'))
    """)
    print(f"Размер частичного индекса: {c.fetchone()[0]}")

    c.execute("""
        SELECT pg_size_pretty(pg_relation_size('employees'))
    """)
    print(f"Размер таблицы: {c.fetchone()[0]}")

    # ============ 2. Covering (INCLUDE) ============
    header("ЭКСПЕРИМЕНТ 2. Покрывающий индекс (dept_id) INCLUDE (name)")
    sql = "SELECT name FROM employees WHERE dept_id = 42"
    t, plan = time_and_plan(c, sql)
    print(f"До (idx_dept):        t = {t:.4f} с   план: {plan}")

    c.execute("CREATE INDEX idx_dept_cover ON employees(dept_id) INCLUDE (name)")
    c.execute("ANALYZE employees")
    t, plan = time_and_plan(c, sql)
    print(f"С INCLUDE(name):      t = {t:.4f} с   план: {plan}")

    # ============ 3. Функциональный индекс ============
    header("ЭКСПЕРИМЕНТ 3. Функциональный индекс LOWER(name)")
    sql = "SELECT * FROM employees WHERE LOWER(name) = 'иван иванов'"
    t, plan = time_and_plan(c, sql)
    print(f"Без индекса:    t = {t:.4f} с   план: {plan}")

    c.execute("CREATE INDEX idx_lower_name ON employees(LOWER(name))")
    c.execute("ANALYZE employees")
    t, plan = time_and_plan(c, sql)
    print(f"С LOWER(name):  t = {t:.4f} с   план: {plan}")

    # ============ 4. Триграммы ============
    header("ЭКСПЕРИМЕНТ 4. Триграммы для LIKE '%ван%'")
    c.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")

    sql = "SELECT * FROM employees WHERE name LIKE '%ван%'"
    t, plan = time_and_plan(c, sql)
    print(f"Без триграмм:        t = {t:.4f} с   план: {plan}")

    c.execute("CREATE INDEX idx_name_trgm ON employees USING GIN (name gin_trgm_ops)")
    c.execute("ANALYZE employees")
    t, plan = time_and_plan(c, sql)
    print(f"С GIN(gin_trgm_ops): t = {t:.4f} с   план: {plan}")

    # Нечёткий поиск через оператор %
    sql = "SELECT * FROM employees WHERE name % 'иванов' LIMIT 5"
    t, plan = time_and_plan(c, sql)
    print(f"Нечёткий (%% иванов): t = {t:.4f} с   план: {plan}")

    # ============ 5. Bitmap scan на средней выборке ============
    header("ЭКСПЕРИМЕНТ 5. Bitmap Scan при 10% выборке (dept_id IN 10 отделов)")
    sql = "SELECT * FROM employees WHERE dept_id BETWEEN 1 AND 10"
    t, plan = time_and_plan(c, sql)
    print(f"dept_id 1..10:  t = {t:.4f} с   план: {plan}")

    c.close()
    conn.close()


if __name__ == "__main__":
    main()
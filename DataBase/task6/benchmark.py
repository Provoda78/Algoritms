"""Замеряет время запросов и печатает план с EXPLAIN (ANALYZE, BUFFERS)."""
import psycopg2
import time

DB_CONFIG = {
    "host": "localhost", "port": 5433,
    "database": "employees_db", "user": "student", "password": "student",
}

QUERIES = [
    ("Q1. Точечный поиск по id (PK)",
     "SELECT * FROM employees WHERE id = 500000"),

    ("Q2. Поиск по имени",
     "SELECT * FROM employees WHERE name = 'Иван Иванов'"),

    ("Q3. Средняя зп по отделу",
     "SELECT AVG(salary), COUNT(*) FROM employees WHERE dept_id = 42"),

    ("Q4. Поиск с LOWER() — индекс не работает",
     "SELECT * FROM employees WHERE LOWER(name) = 'иван иванов'"),

    ("Q5. LIKE с префиксом (Иван%)",
     "SELECT * FROM employees WHERE name LIKE 'Иван%'"),

    ("Q6. LIKE с % в начале (%ван%)",
     "SELECT * FROM employees WHERE name LIKE '%ван%'"),

    ("Q7. Только активные (status = active, 1%)",
     "SELECT * FROM employees WHERE status = 'active'"),

    ("Q8. dept_id = 42, только name",
     "SELECT name FROM employees WHERE dept_id = 42"),
]


def explain(c, sql):
    """Возвращает первую содержательную строку плана."""
    c.execute(f"EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) {sql}")
    rows = c.fetchall()
    plan_lines = [r[0] for r in rows]
    # Первая строка после "Query Text" — либо "Seq Scan", либо "Index Scan" и т.д.
    for line in plan_lines:
        stripped = line.strip()
        if stripped.startswith(("Seq Scan", "Index Scan", "Index Only Scan",
                                 "Bitmap", "Gather", "Sort", "Aggregate")):
            return stripped
    return plan_lines[0].strip() if plan_lines else "?"


def extract_metrics(c, sql):
    """Запускает EXPLAIN ANALYZE и вытаскивает метрики (время, hits, reads)."""
    c.execute(f"EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) {sql}")
    rows = c.fetchall()
    text = "\n".join(r[0] for r in rows)

    # Execution Time
    exec_time = 0.0
    for line in text.splitlines():
        if "Execution Time:" in line:
            try:
                exec_time = float(line.split(":")[1].replace("ms", "").strip())
            except ValueError:
                pass

    hits = reads = 0
    for line in text.splitlines():
        if "shared hit=" in line:
            try:
                hits = int(line.split("shared hit=")[1].split()[0])
            except (ValueError, IndexError):
                pass
        if "read=" in line:
            try:
                reads = int(line.split("read=")[1].split()[0])
            except (ValueError, IndexError):
                pass
    return exec_time / 1000.0, hits, reads


def main():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True
    c = conn.cursor()

    print(f"{'Запрос':<45} {'t, с':>8} {'hit':>6} {'read':>6}  План")
    print("-" * 130)
    for title, sql in QUERIES:
        plan = explain(c, sql)
        t, hits, reads = extract_metrics(c, sql)
        print(f"{title:<45} {t:>8.4f} {hits:>6} {reads:>6}  {plan}")

    c.close()
    conn.close()


if __name__ == "__main__":
    main()
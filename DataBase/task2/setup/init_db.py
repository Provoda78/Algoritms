import sqlite3

DB_FILE = "../employees.db"

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Удаляем старые таблицы, если есть
c.execute("DROP TABLE IF EXISTS works")
c.execute("DROP TABLE IF EXISTS projects")
c.execute("DROP TABLE IF EXISTS employees")
c.execute("DROP TABLE IF EXISTS departments")

# Создаём таблицы
c.execute("""
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL,
    manager TEXT
)
""")

c.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
""")

c.execute("""
CREATE TABLE projects (
    proj_id INTEGER PRIMARY KEY,
    proj_name TEXT NOT NULL,
    manager TEXT
)
""")

c.execute("""
CREATE TABLE works (
    emp_id INTEGER,
    proj_id INTEGER,
    PRIMARY KEY (emp_id, proj_id),
    FOREIGN KEY (emp_id) REFERENCES employees(id),
    FOREIGN KEY (proj_id) REFERENCES projects(proj_id)
)
""")

# Данные отделов
departments = [
    (1, 'IT', 'Ivanov'),
    (2, 'Accounting', 'Petrova'),
    (3, 'Sales', 'Sidorov'),
    (4, 'Marketing', 'Kozlova'),
    (5, 'HR', 'Mikhailov')
]
c.executemany("INSERT INTO departments VALUES (?, ?, ?)", departments)

# Данные сотрудников
employees = [
    (1, 'Anna Smirnova', 75000, 1),
    (2, 'Boris Kuznetsov', 95000, 1),
    (3, 'Viktor Popov', 110000, 1),
    (4, 'Galina Sokolova', 135000, 1),
    (5, 'Dmitry Lebedev', 120000, 2),
    (6, 'Elena Kozlova', 85000, 2),
    (7, 'Ivan Novikov', 90000, 2),
    (8, 'Ksenia Morozova', 105000, 2),
    (9, 'Mikhail Petrov', 140000, 3),
    (10, 'Olga Smirnova', 95000, 3),
    (11, 'Pavel Ivanov', 100000, 3),
    (12, 'Roman Kuznetsov', 125000, 3),
    (13, 'Svetlana Popova', 80000, 4),
    (14, 'Tatiana Sokolova', 70000, 4),
    (15, 'Ulyana Lebedeva', 115000, 4),
    (16, 'Fedor Kozlov', 130000, 4),
    (17, 'Yulia Novikova', 75000, 5),
    (18, 'Yaroslav Morozov', 85000, 5),
    (19, 'Alexey Petrov', 110000, 5),
    (20, 'Ekaterina Ivanova', 95000, 5)
]
c.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees)

# Данные проектов
projects = [
    (1, 'Alpha', 'Ivanov'),
    (2, 'Beta', 'Petrov'),
    (3, 'Gamma', 'Sidorov'),
    (4, 'Delta', 'Ivanov'),
    (5, 'Epsilon', 'Kozlov'),
    (6, 'Zeta', 'Mikhailov'),
    (7, 'Eta', 'Ivanov'),
    (8, 'Theta', 'Petrov'),
    (9, 'Iota', 'Sidorov'),
    (10, 'Kappa', 'Kozlov')
]
c.executemany("INSERT INTO projects VALUES (?, ?, ?)", projects)

# Данные об участии в проектах
works = [
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 4), (2, 5),
    (3, 2), (3, 3), (3, 6),
    (4, 1), (4, 5), (4, 7),
    (5, 2), (5, 3), (5, 8),
    (6, 1), (6, 6), (6, 9),
    (7, 3), (7, 4), (7, 10),
    (8, 1), (8, 2), (8, 5),
    (9, 2), (9, 3), (9, 7),
    (10, 1), (10, 4), (10, 8),
    (11, 3), (11, 5), (11, 9),
    (12, 1), (12, 6), (12, 10),
    (13, 2), (13, 3), (13, 4),
    (14, 1), (14, 5), (14, 6),
    (15, 3), (15, 7), (15, 8),
    (16, 1), (16, 2), (16, 9),
    (17, 3), (17, 4), (17, 10),
    (18, 1), (18, 5), (18, 7),
    (19, 2), (19, 6), (19, 8),
    (20, 3), (20, 9), (20, 10)
]
c.executemany("INSERT INTO works VALUES (?, ?)", works)

conn.commit()
conn.close()
print("✅ База данных employees.db создана и заполнена.")
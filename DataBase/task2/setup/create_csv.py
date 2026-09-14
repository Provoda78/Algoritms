import sqlite3
import csv
import os

DB_FILE = "../employees.db"
OUTPUT_DIR = "../data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

tables = ["employees", "departments", "projects", "works"]

for table in tables:
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    rows = c.fetchall()
    col_names = [desc[0] for desc in c.description]
    conn.close()

    path = os.path.join(OUTPUT_DIR, f"{table}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(col_names)
        writer.writerows(rows)

    print(f"✅ {table}.csv создан")
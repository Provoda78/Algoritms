"""Генератор данных: 1 млн сотрудников."""
import csv
import random
import os

NUM_EMPLOYEES = 1_000_000
NUM_DEPARTMENTS = 100
OUTPUT_FILE = "employees_1m.csv"

FIRST_NAMES = [
    "Анна", "Борис", "Виктор", "Галина", "Дмитрий",
    "Елена", "Иван", "Ксения", "Михаил", "Ольга",
]
LAST_NAMES = [
    "Смирнов", "Иванов", "Кузнецов", "Попов", "Соколов",
    "Лебедев", "Козлов", "Новиков", "Морозов", "Петров",
]
EMAIL_DOMAINS = ["gmail.com", "yandex.ru", "mail.ru", "example.com", "corp.ru"]


def generate(n):
    rows = []
    for i in range(n):
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        email = f"user{i}@{random.choice(EMAIL_DOMAINS)}"
        # 1% активных — для эксперимента с частичным индексом
        status = "active" if random.random() < 0.01 else "inactive"
        salary = random.randint(30_000, 300_000)
        dept_id = random.randint(1, NUM_DEPARTMENTS)
        rows.append([100_000 + i, name, email, status, salary, dept_id])
    return rows


def write_csv(filename, rows):
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "email", "status", "salary", "dept_id"])
        w.writerows(rows)


if __name__ == "__main__":
    print(f"Генерация {NUM_EMPLOYEES} записей...")
    write_csv(OUTPUT_FILE, generate(NUM_EMPLOYEES))
    print(f"Готово: {OUTPUT_FILE}")
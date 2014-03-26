import sqlite3


def create_tables(cursor):
    cursor.execute('''CREATE TABLE employees
                 (id INTEGER PRIMARY KEY, name text, monthly_salary int, yearly_bonus int, position text)''')


def insert(item, cursor):
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    query_lang = "INSERT INTO employees VALUES(?, ?, ?, ?, ?)"
    cursor.execute(query_lang, (None, name, monthly_salary, yearly_bonus, position))


data = [{
    "name": "Ivan Ivanov",
    "monthly_salary": 5000,
    "yearly_bonus": 10000,
    "position": "Software Developer"
}, {
    "name": "Rado Rado",
    "monthly_salary": 500,
    "yearly_bonus": 0,
    "position": "Technical Support Intern"
}, {
    "name": "Ivo Ivo",
    "monthly_salary": 10000,
    "yearly_bonus": 100000,
    "position": "CEO"
}, {
    "name": "Petar Petrov",
    "monthly_salary": 3000,
    "yearly_bonus": 1000,
    "position": "Marketing Manager"
}, {
    "name": "Maria Georgieva",
    "monthly_salary": 8000,
    "yearly_bonus": 10000,
    "position": "COO"
}]

conn = sqlite3.connect("employees.db")
c = conn.cursor()

create_tables(c)

for item in data:
    insert(item, c)

conn.commit()
conn.close()

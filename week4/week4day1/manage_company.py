import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()


#id INTEGER PRYMARY KEY -> pravi id-tata da se uveli4avat avtomati4no

#Global arguments
commands = ["list_employees", "monthly_spending", "yearly_spending", "add_employee", "delete_employee", "update_employee", "finish"]


# command>list_employees
# 1 - Ivan Ivanov - Software Developer
# 2 - Rado Rado - Technical Support Intern
# 3 - Ivo Ivo - CEO
# 4 - Petar Petrov - Marketing Manager
# 5 - Maria Georgieva - COO
def list_employees():
    cursor = conn.cursor()
    result = cursor.execute("SELECT id, name, position FROM employees")

    for row in result:
        formatted_line = str(row[0]) + " - " + row[1] + " - " + row[2]
        print(formatted_line)


# monthly_spending - Prints out the total sum for monthly spending that the
#company is doing for salaries
def monthly_spending():
    cursor = conn.cursor()
    salaries = cursor.execute("SELECT monthly_salary FROM employees")
    spending = 0
    for row in salaries:
        spending += row[0]
    return spending


def yearly_spending():
    result = 12 * monthly_spending()
    return result


def add_employee():
    cursor = conn.cursor()
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")

    query_employee = "INSERT INTO employees VALUES(?, ?, ?, ?, ?)"
    cursor.execute(query_employee, (None, name, monthly_salary, yearly_bonus, position))


def delete_employee(employee_id):
    cursor = conn.cursor()
    current_id = str(employee_id)
    query_employee1 = "SELECT name FROM employees WHERE id = ?"
    row_tuple = cursor.execute(query_employee1, (current_id, ))

    #only one row
    for row in row_tuple:
        name = row[0]
    message = name + " was deleted."
    print(message)

    #actually deleting the employee
    query_employee2 = "DELETE FROM employees WHERE id = ?"
    cursor.execute(query_employee2, (current_id, ))


def update_employee(employee_id):
    cursor = conn.cursor()
    current_id = str(employee_id)

    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")

    query_employee = "UPDATE employees SET name=?, monthly_salary=?, yearly_bonus=?, position=? WHERE id = ?"
    cursor.execute(query_employee, (name, monthly_salary, yearly_bonus, position, current_id))


while True:
    command = input("Enter command>")
    arguments = command.split()

    if (arguments[0] not in commands):
        print("Unknown command!\nTry one of the following:\nlist_employees\nmonthly_spending\nyearly_spending\nadd_employee\ndelete_employee <employee_id>\nupdate_employee <employee_id>\nfinish")

    if (arguments[0] == "list_employees"):
        list_employees()

    if (arguments[0] == "monthly_spending"):
        print(monthly_spending())

    if (arguments[0] == "yearly_spending"):
        print(yearly_spending())

    if (arguments[0] == "add_employee"):
        add_employee()

    if (arguments[0] == "delete_employee"):
        employee_id = int(arguments[1])
        delete_employee(employee_id)

    if (arguments[0] == "update_employee"):
        employee_id = int(arguments[1])
        update_employee(employee_id)

    if (arguments[0] == "finish"):
        conn.commit()
        conn.close()
        break


def main():
    pass


if __name__ == '__main__':
    main()

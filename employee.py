import sqlite3

with sqlite3.connect("employee.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,    
last_name TEXT NOT NULL,
year_joined YEAR NOT NULL,
dept TEXT NOT NULL,
gender TEXT NOT NULL
);""")
    
    cursor.execute("""INSERT INTO employees(first_name, last_name, year_joined, dept, gender) VALUES
    (?, ?, ?, ?, ?),
    (?, ?, ?, ?, ?),
    (?, ?, ?, ?, ?),               
    (?, ?, ?, ?, ?);""",("John", "Adams", 1990, "Python", "M", "Martin", "Luther", 1971, "Html", "M", "Victoria", "Cakes", 1987, "SQL", "F", "Paul", "Stone", 2002, "Excel", "M"))               
                   
    # employees = cursor.execute("SELECT * FROM employees;").fetchall()  
    # print(employees) 

    employees_after_1997 = cursor.execute("SELECT * FROM employees WHERE year_joined < 1998;").fetchall()
    
    print(employees_after_1997)    

    cursor.execute(""" UPDATE employees
    SET dept = ?
    WHERE id = ?;
    """,("Victoria", 3))

    employees= cursor.execute("""DELETE FROM employees 
    WHERE year_joined < ?; """,(1997,))

    employees = cursor.execute("SELECT * FROM employees").fetchall()
    print(employees)

    
                 
                   





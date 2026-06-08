from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_db"
)

cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('index.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    department = request.form['department']
    salary = request.form['salary']

    sql = """
    INSERT INTO employees (Name, Department, Salary)
    VALUES (%s, %s, %s)
    """

    values = (name, department, salary)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    

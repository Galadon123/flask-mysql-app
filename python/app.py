from flask import Flask, jsonify, request
from werkzeug.urls import url_unquote  # Importing url_unquote instead of url_quote
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port=3306, database='db'
)
cursor = db_connection.cursor()

# Endpoint to get all students
@app.route('/students', methods=['GET'])
def get_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    return jsonify(students)

# Endpoint to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    first_name = data.get('first_name')
    surname = data.get('surname')

    if not first_name or not surname:
        return jsonify({'error': 'Both first_name and surname are required'}), 400

    sql = 'INSERT INTO students (FirstName, Surname) VALUES (%s, %s)'
    cursor.execute(sql, (first_name, surname))
    db_connection.commit()

    return jsonify({'message': 'Student added successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

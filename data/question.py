import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age > 22;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE category = 'Veritabanı';")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE first_name LIKE 'A%';")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_name LIKE '%SQL%';")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE age BETWEEN 22 AND 24;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT s.first_name, s.last_name FROM students AS s JOIN enrollments AS e ON e.student_id = s.student_id ORDER BY s.student_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(''' SELECT c.course_name, COUNT(*) FROM courses AS c
JOIN enrollments AS e
ON e.course_id = c.course_id
JOIN students AS s
ON s.student_id = e.student_id
WHERE c.category = 'Veritabanı'
GROUP BY c.course_name
ORDER BY c.course_name DESC;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT c.course_name, i.name FROM courses AS c
JOIN course_instructors AS ci
ON c.course_id = ci.course_id
JOIN instructors AS i
ON i.instructor_id = ci.instructor_id
ORDER BY c.course_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SElECT s.student_id, s.first_name, s.last_name, s.email, s.age FROM students AS s
LEFT JOIN enrollments AS e
ON e.student_id = s.student_id
WHERE e.enrollment_id IS NULL;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT c.course_name, AVG(s.age) FROM courses AS c
JOIN enrollments AS e
ON e.course_id = c.course_id
JOIN students AS s
ON e.student_id = s.student_id
GROUP BY c.course_name
ORDER BY c.course_name ASC;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT s.first_name, s.last_name, COUNT(e.course_id) AS "totat_courses"
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
GROUP BY s.first_name, s.last_name;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT i.name, COUNT(c_i.instructor_id) AS "total_courses"
FROM instructors i
JOIN course_instructors c_i
ON i.instructor_id = c_i.instructor_id
GROUP BY i.name
HAVING COUNT(c_i.instructor_id) > 1''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT c.course_name, COUNT(e.student_id) AS "total_students"
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
JOIN students s
ON s.student_id = e.student_id
GROUP BY c.course_name 
ORDER BY c.course_name DESC;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT
    s.first_name,
    s.last_name
FROM students s
JOIN enrollments e
    ON s.student_id = e.student_id
JOIN courses c
    ON e.course_id = c.course_id
WHERE c.course_name IN ('SQL Temelleri', 'İleri SQL')
GROUP BY
    s.student_id,
    s.first_name,
    s.last_name
HAVING COUNT(DISTINCT c.course_name) = 2;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT s.first_name, s.last_name,c.course_name,i.name,e.enrollment_date
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
JOIN course_instructors c_i
ON c.course_id = c_i.course_id
JOIN instructors i
ON i.instructor_id = c_i.instructor_id
ORDER BY e.enrollment_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
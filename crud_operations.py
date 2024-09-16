import sqlite3

def insert_row(name, age, email, salary, active, created_at, updated_at, phone_number, notes):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO my_table (name, age, email, salary, active, created_at, updated_at, phone_number, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, email, salary, active, created_at, updated_at, phone_number, notes))

    conn.commit()
    conn.close()

def read_rows():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_row(id, name=None, age=None, email=None, salary=None, active=None, created_at=None, updated_at=None, phone_number=None, notes=None):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Build the query dynamically
    fields = []
    values = []

    if name:
        fields.append('name = ?')
        values.append(name)
    if age:
        fields.append('age = ?')
        values.append(age)
    if email:
        fields.append('email = ?')
        values.append(email)
    if salary:
        fields.append('salary = ?')
        values.append(salary)
    if active:
        fields.append('active = ?')
        values.append(active)
    if created_at:
        fields.append('created_at = ?')
        values.append(created_at)
    if updated_at:
        fields.append('updated_at = ?')
        values.append(updated_at)
    if phone_number:
        fields.append('phone_number = ?')
        values.append(phone_number)
    if notes:
        fields.append('notes = ?')
        values.append(notes)

    query = f'UPDATE my_table SET {", ".join(fields)} WHERE id = ?'
    values.append(id)

    cursor.execute(query, values)

    conn.commit()
    conn.close()

def delete_row(id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM my_table WHERE id = ?', (id,))

    conn.commit()
    conn.close()

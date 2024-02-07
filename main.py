from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'registration.db'

# Function to get a database connection
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create a table if it doesn't exist
def create_table():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Registration (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            DateOfBirth DATE
        )
    ''')
    conn.commit()
    conn.close()

# Create operation
@app.route('/register', methods=['POST'])
def create_registration():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    dob = data.get('dob')

    if not name or not email:
        return jsonify({'error': 'Name and Email are required'}), 400

    conn = get_db()
    conn.execute('INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (?, ?, ?)', (name, email, dob))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Registration created successfully'}), 201

# Read operation
@app.route('/register/<int:id>', methods=['GET'])
def get_registration(id):
    conn = get_db()
    cursor = conn.execute('SELECT * FROM Registration WHERE ID = ?', (id,))
    registration = cursor.fetchone()
    conn.close()

    if registration:
        return jsonify(dict(registration)), 200
    else:
        return jsonify({'error': 'Registration not found'}), 404

# Update operation
@app.route('/register/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    dob = data.get('dob')

    conn = get_db()
    conn.execute('UPDATE Registration SET Name=?, Email=?, DateOfBirth=? WHERE ID=?', (name, email, dob, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Registration updated successfully'}), 200

# Delete operation
@app.route('/register/<int:id>', methods=['DELETE'])
def delete_registration(id):
    conn = get_db()
    conn.execute('DELETE FROM Registration WHERE ID = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Registration deleted successfully'}), 200

if __name__ == '__main__':
    create_table()
    app.run(debug=True)

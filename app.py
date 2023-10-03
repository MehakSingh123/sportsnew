from flask import Flask, request, render_template
import sqlite3
import time
app = Flask(__name__)

# SQLite database configuration
DATABASE = "mydatabase.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS registrations (
                        id INTEGER PRIMARY KEY,
                        crn TEXT,
                        urn TEXT,
                        event TEXT,
                        registration_number INTEGER)''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        crn = request.form["crn"]
        urn = request.form["urn"]
        event = request.form["event"]

        # Generate a unique registration number (e.g., timestamp)
        registration_number = int(time.time())

        # Store the registration in the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO registrations (crn, urn, event, registration_number)
                          VALUES (?, ?, ?, ?)''', (crn, urn, event, registration_number))
        conn.commit()
        conn.close()

        return f"You are registered for the {event} event. Your unique registration number is: {registration_number}"

    return render_template("registration_form.html")

if __name__ == "__main__":
    create_table()
    app.run(debug=True, port= 8080)
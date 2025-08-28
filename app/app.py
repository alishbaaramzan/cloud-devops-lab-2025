from flask import Flask, render_template, jsonify
import os
import psycopg2

app = Flask(__name__)

# Load DB credentials from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "flaskdb")
DB_USER = os.getenv("DB_USER", "flaskuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "flaskpass")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_message():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute("SELECT content FROM secret_message LIMIT 1;")
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    return message

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reveal")
def reveal():
    return jsonify({"message": get_message()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

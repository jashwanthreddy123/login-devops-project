from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import psycopg2
import os

from prometheus_client import Counter, generate_latest


app = Flask(__name__)
CORS(app)


# Prometheus metric
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests'
)


@app.before_request
def before_request():
    REQUEST_COUNT.inc()



def get_db_connection():

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return conn



@app.route("/")
def home():
    return "Backend is running"



@app.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data["email"]
    password = data["password"]


    conn = get_db_connection()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email,password)
    )


    user = cursor.fetchone()


    cursor.close()
    conn.close()


    if user:
        return jsonify({
            "message":"Login successful"
        })

    else:
        return jsonify({
            "message":"Invalid credentials"
        })



# Prometheus endpoint
@app.route("/metrics")
def metrics():

    return Response(
        generate_latest(),
        mimetype="text/plain"
    )



app.run(
    host="0.0.0.0",
    port=5000
)   

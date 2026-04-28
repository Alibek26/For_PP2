import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(
        dbname=DB_CONFIG["DB_NAME"],
        user=DB_CONFIG["DB_USER"],
        password=DB_CONFIG["DB_PASSWORD"],
        host=DB_CONFIG["DB_HOST"],
        port=DB_CONFIG["DB_PORT"]
    )
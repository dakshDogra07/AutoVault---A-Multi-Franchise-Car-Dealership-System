from db import get_connection

def get_all_franchises():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM franchises")
    return cursor.fetchall()

def add_franchise(name, city):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO franchises (name, city) VALUES (%s, %s)", (name, city))
    conn.commit()
    conn.close()
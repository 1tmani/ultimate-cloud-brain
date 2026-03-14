import sqlite3

def init_db():
    conn = sqlite3.connect("brain.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logs(command TEXT)")
    conn.commit()
    conn.close()

def save_db(command):
    conn = sqlite3.connect("brain.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?)",(command,))
    conn.commit()
    conn.close()

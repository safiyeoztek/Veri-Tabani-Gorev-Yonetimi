import sqlite3

def connect_db():
    return sqlite3.connect("app.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL
        ) 
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            username TEXT,
            task_name TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    
def add_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        return "Kullanıcı oluşturuldu."
    except sqlite3.IntegrityError:
        return "Hata: Bu kullanıcı adı zaten alınmış."
    except Exception as e:
        return f"Beklenmeyen bir hata oluştu: {e}"
    finally:
        conn.close()

def add_task(username, task):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO tasks (username, task_name) VALUES (?, ?)", (username, task))
        conn.commit()
        return True, "Görev eklendi."
    except Exception as e:
        return False, f"Görev eklenirken hata oluştu: {e}"
    finally:
        conn.close()

def get_tasks(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT task_name FROM tasks WHERE username = ?", (username,))
    tasks = cursor.fetchall()
    conn.close()
    
    return [task[0] for task in tasks]
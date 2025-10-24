import sqlite3 

# Data base conection (file or memory)
# conn = sqlite3.connect(":memory:") # temporal
conn = sqlite3.connect("db/sample.db")
cur = conn.cursor()

# Crate tables
# Reset the db to avoid errors 
cur.execute("DROP TABLE IF EXISTS users;")
cur.execute("DROP TABLE IF EXISTS tasks;")

cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")

cur.execute("""
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    done BOOLEAN,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
""")

# Insert users 
users = [("Alice",), ("Bob",), ("Charlie",), ("Diana",), ("Eve",), ("Frank",)]
cur.executemany("INSERT INTO users(name) VALUES (?);", users)

# Insert tasks (20 total)
tasks = [
    (1, "Tarea A", True),
    (1, "Tarea B", False),
    (1, "Tarea C", True),
    (2, "Tarea D", True),
    (2, "Tarea E", True),
    (2, "Tarea F", True),
    (3, "Tarea G", False),
    (3, "Tarea H", True),
    (3, "Tarea I", False),
    (3, "Tarea J", True),
    (4, "Tarea K", True),
    (4, "Tarea L", True),
    (4, "Tarea M", False),
    (5, "Tarea N", False),
    (5, "Tarea O", False),
    (5, "Tarea P", True),
    (6, "Tarea Q", True),
    (6, "Tarea R", True),
    (6, "Tarea S", True),
    (6, "Tarea T", False),
]
cur.executemany("INSERT INTO tasks(user_id, title, done) VALUES (?, ?, ?);", tasks)

# Query: How many tasks each users have (Only users with 3 or more)
cur.execute("""
SELECT users.name, COUNT(tasks.id) AS task_count
FROM users
JOIN tasks ON users.id = tasks.user_id
GROUP BY users.name
HAVING COUNT(tasks.id) > 3;
""")

# Show results
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()

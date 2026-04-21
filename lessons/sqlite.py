import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()

# commands:
# CREATE - creates a table in the db.
# INSERT - insert data into the table.
# SELECT - query the db.
# UPDATE
# DELETE
# WHERE - filtering

c.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL UNIQUE, 
    age INTEGER CHECK(age >= 0),
    grade TEXT DEFAULT 'F'
    )
""")
conn.commit() #- saves the change. 


# insert data:
# ? - paramatrized data - just a placholder. 
# for data safety. 

c.execute("SELECT * FROM students WHERE name = ? AND age = ? AND grade = ?", ("c", 20, "A"))
if c.fetchone() is None:
    c.execute("""
        INSERT INTO students (name, age, grade)
        VALUES(?, ?, ?) 
    """, ("c", 20, "B"))
    conn.commit()
else:
    print("already in db")

# update

c.execute(
    """
        UPDATE students
        SET grade = ?
        WHERE name = ?
    """, ("A", "c")
)
conn.commit()


# query:

c.execute("SELECT * FROM students")
x = c.fetchall()

for data in x:
    print(data)

# delete:    
c.execute("""
    DELETE FROM students
    WHERE name = ?
""",("c",))
conn.commit()

c.execute("SELECT * FROM students")
x = c.fetchall()

for data in x:
    print(data)

# execute many + indexing

students_data = [
    ("a", 22, "A"),
    ("b", 33, "A"),
    ("d", 44, "A")
]


c.executemany("""
    INSERT INTO students (name, age, grade)
    VALUES(?, ?, ?)
""", students_data)
conn.commit()

c.execute("SELECT * FROM students")
x = c.fetchall()

for data in x:
    print(data)

c.execute("""
    CREATE INDEX IF NOT EXISTS idx_students_name
    ON students(name)
""")
conn.commit()
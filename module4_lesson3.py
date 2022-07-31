import sqlite3
print("Successful")

#connect to a database
conn = sqlite3.connect('student.db')

# create a cursor object
c = conn.cursor()
print("cursor created")

# c.execute(""" 
#             CREATE TABLE students_data(
#                 first_name TEXT,
#                 last_name TEXT,
#                 email TEXT
#                             )
# """)

print("table created successfully")

students_list = [("will", "Johnson", "willjohnson@stutern.com"), 
                ("John", "Smith", "johnsmith@stutern.com"), 
                ("Katy", "Brown", "katybrown@stutern.com")
                ]

#c.execute("ALTER TABLE students_data RENAME TO students_info")
print('Table changed to students_info')

c.executemany("INSERT INTO students_info VALUES(?, ?, ?)", students_list)

print("We have inserted", c.rowcount, "records to the table")

#items = c.execute("SELECT * FROM students_info")




#c.executemany("INSERT INTO students_info VALUES(?, ?, ?)", students_list)

print("We have inserted", c.rowcount, "records to the table")

c.execute("ALTER TABLE students_info ADD COLUMN course TEXT")


c.execute("UPDATE students_info SET course = 'Data Science';")

print('colunm updated')

items = c.execute("SELECT * FROM students_info")

print("FIRSTNAME" + "\t\t" + "SURNAME" + "\t\t\t" + "EMAIL" "\t\t\t\t" + "COURSE" "\n" f"{'-' * 100}")
for i in items:
    print(i[0] + "\t\t\t" + i[1] + "\t\t\t" + i[2] + "\t\t" + i[3])

conn.commit()
conn.close()







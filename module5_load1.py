import sqlite3
import csv

conn = sqlite3.connect("weac.db")

cursor = conn.cursor()
print('sucessful')

# cursor.execute("""CREATE TABLE weac_result(
#             name TEXT, 
#             english INTEGER,
#             maths INTEGER,
#             biology INTEGER,
#             agric INTEGER,
#             geograpghy INTEGER,
#             further_math INTEGER,
#             physics INTEGER,
#             economics INTEGER,
#             yoruba INTEGER
#         )
# """)

print('table created sucessufully')

#load existing csv file
with open('exam.csv', 'r') as opened_file:
    read_file = csv.reader(opened_file)

    #skip header
    next(read_file)

    cursor.executemany("""
    INSERT INTO weac_result VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", read_file)

print("Sucessfully inserted", cursor.rowcount, "records into the table")

conn.commit()
conn.close()
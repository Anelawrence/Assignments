import sqlite3

conn = sqlite3.connect("weac.db")

cursor = conn.cursor()
print("created a cursor\n"f"{'='*100}")

# Which student scored the highest in maths
def highiest_in_maths():
    cursor.execute("SELECT name, MAX(maths) FROM weac_result")
    items = cursor.fetchall()
    for i in items:
        print("The student who score the highest in maths is " + i[0].upper() + " with", i[1],"% mark.\n"f"{'='*100}")


# Which student scored the lowest in english
def lowest_in_english():
    cursor.execute("SELECT name, MIN(english) FROM weac_result")
    items = cursor.fetchall()
    for i in items:
        print("The student has the least score in english is " + i[0].upper() + " with", i[1],"% mark.\n"f"{'='*100}")


# What is the average score of students in maths
def average_maths():
    cursor.execute("SELECT AVG(maths) FROM weac_result")
    items = cursor.fetchall()
    for i in items:
        print("The average score of students in maths is", i[0], "%\n"f"{'='*100}")


# What is the average score of students in english
def average_english():
    cursor.execute("SELECT AVG(english) FROM weac_result")
    items = cursor.fetchall()
    for i in items:
        print("The average score of students in english is", i[0], "%\n"f"{'='*100}")


# Who is the best performing student across all nine subjects in terms of overall scores
def best_overall():
    cursor.execute("""SELECT name, 
                    SUM(maths + english + biology + agric + geograpghy + further_math + physics + economics + yoruba)
                    AS total
                    FROM weac_result          
                    GROUP BY name
                    ORDER BY total DESC
                    LIMIT 1""")
    items = cursor.fetchall()
    for i in items:
        print("The best overall student is " + i[0].upper() + " with", i[1],"aggregate score in the 9 subjects.\n"f"{'='*100}")


# Who is the best performing student across all nine subjects in term of average scores
def average_overall():
    cursor.execute("""SELECT name, 
                    AVG(maths + english + biology + agric + geograpghy + further_math + physics + economics + yoruba)/9
                    AS average
                    FROM weac_result          
                    GROUP BY name
                    ORDER BY average DESC
                    LIMIT 1""")
    items = cursor.fetchall()
    for i in items:
        print("The overall average student is " + i[0].upper() + " with", i[1],"average score in the 9 subjects.\n"f"{'='*100}")


# Which student scored the highest in maths
highiest_in_maths()

# Which student scored the lowest in english
lowest_in_english()

# What is the average score of students in maths
average_maths()

# What is the average score of students in english
average_english()

# Who is the best performing student across all nine subjects in terms of overall scores
best_overall()

# Who is the best performing student across all nine subjects in term of average scores
average_overall()

conn.commit()
conn.close()

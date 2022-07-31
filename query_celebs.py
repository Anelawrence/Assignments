# Create a dummy celebrity dataset with the following features name, genre, num_albums, age, awards, years_in_industry
# Create a celebs database in sqlite and insert the dataset into it
# Make your celebrity dataset have at least 20 rows (i.e 20 unique records)
# Query your data to answer the following questions:
#  - Who is the most decorated celebrity?
#  - Who is the oldest celebrity?
#  - Which celebrity has been in the industry the longest?
#  - Which celebrity has the least number of albums?
#  - What is the most popular genre of music amongst all celebrities in the dataset?

import sqlite3

conn = sqlite3.connect("celebrity.db")

cursor = conn.cursor()

def most_awarded():
    cursor.execute("SELECT name, MAX(awards) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print("The most decorated musician is " + i[0].upper() + " with", i[1], "awards!")

def oldest_celeb():
    cursor.execute("SELECT name, MAX(age) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print("The oldest musician is " + i[0].upper() + ", who is", i[1], "years old.")

def industry_legend():
    cursor.execute("SELECT name, MAX(years_in_industry) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print("The legendary musician is " + i[0].upper() + ", who has been in the industry for", i[1], "years.")

def minimun_album():
    cursor.execute("SELECT name, MIN(num_albums) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print(i[0].upper() + " is the musician with the least album, with just" , i[1], "album.")


def popular_genre():
    cursor.execute("""SELECT genre,
            COUNT(genre) AS value_occurrence 
            FROM celebs
            GROUP BY genre
            ORDER BY value_occurrence DESC
            LIMIT 1;""")
    items = cursor.fetchall()
    #print(items)
    for i in items:
        print(i[0].upper() + " is the most popular genre of music in the dataset")


most_awarded()
oldest_celeb()
industry_legend() 
minimun_album()
popular_genre()
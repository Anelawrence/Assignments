import sqlite3

conn = sqlite3.connect("celebrity.db")

cursor = conn.cursor()

def most_awarded():
    cursor.execute("SELECT name, MAX(awards) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print("The most decorated musician is " + i[0].upper() + " with", i[1], "awards!\n"f"{'='*80}")

def oldest_celeb():
    cursor.execute("SELECT name, MAX(age) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print("The oldest musician is " + i[0].upper() + ", who is", i[1], "years old.\n"f"{'='*80}")

def industry_legend():
    cursor.execute("SELECT name, MAX(years_in_industry) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print("The legendary musician is " + i[0].upper() + ", who has been in the industry for", i[1], "years.\n"f"{'='*80}")

def minimun_album():
    cursor.execute("SELECT name, MIN(num_albums) FROM celebs")
    items = cursor.fetchall()
    for i in items:
        print(i[0].upper() + " is the musician with the least album, with just" , i[1], "album.\n"f"{'='*80}")


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
        print(i[0].upper() + " is the most popular genre of music in the dataset.\n"f"{'='*80}")

# Who is the most decorated celebrity?
most_awarded()

#Who is the oldest celebrity?
oldest_celeb()

#Which celebrity has been in the industry the longest?
industry_legend() 

#Which celebrity has the least number of albums?
minimun_album()

#What is the most popular genre of music amongst all celebrities in the dataset?
popular_genre()

conn.commit()
conn.close()

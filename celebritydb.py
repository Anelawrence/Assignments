import sqlite3

print("succesfull")

conn = sqlite3.connect("celebrity.db")
print("created a database")

cursor = conn.cursor()
print("created a cursor")

# cursor.execute("""
#                 CREATE TABLE celebs(
#                     name TEXT, 
#                     genre TEXT, 
#                     num_albums INTEGER, 
#                     age INTEGER, 
#                     awards INTERGER, 
#                     years_in_industry INTEGER
#                     )
#         """)

print('Table created sucessfully')

celeb_list = [('Davido', 'Afrobeat', 4, 30, 104, 13), 
            ('Wizkid', 'Afrobeat', 4, 32, 65, 13), 
            ('Burnaboy', 'Afrobeat', 4, 31, 25, 10),
            ('Olamide', 'hiphop', 3, 32, 35, 13), 
            ('MI', 'hiphop', 3, 40, 25, 12), 
            ('Tuface', 'R&B', 5, 45, 48, 26), 
            ('DBanj', 'Afrobeat', 2, 37, 25, 18),
            ('Pasuma', 'Fuji', 20, 54, 19, 30),
            ('Frank Edward', 'Gospel', 5, 33, 10, 10),
            ('Fire Boy', 'Afrobeat', 2, 26, 8, 4), 
            ('Flavour', 'Highlife', 4, 38, 25, 15), 
            ('Kizz Daniel', 'Afrobeat', 3, 32, 14, 9), 
            ('Diamond Platnumz', 'Afropop', 4, 36, 25, 13),
            ('Tiwa Savage', 'Afrobeat', 4, 42, 27, 16), 
            ('Yemi Alade', 'Afropop', 2, 37, 15, 10), 
            ('Simi', 'Afrobeat', 2, 33, 14, 8), 
            ('Falz', 'hiphop', 3, 31, 20, 10),
            ('Asake', 'Afrobeat', 1, 36, 3, 3), 
            ('Timi Dakolo', 'R&B', 2, 37, 12, 9), 
            ('Yinka Ayefele', 'Gospel', 6, 47, 21, 20)
            ]

cursor.executemany("INSERT INTO celebs VALUES(?, ?, ?, ?, ?, ?)", celeb_list)

print("We have inserted", cursor.rowcount, "records to the table")

print("ARTIST \t\t GENRE \t\t NO of ALBUMS \t    AGE \t AWARDS \tYEARS IN INDUSTRY \n" f"{'-' * 100}")

cursor.execute('SELECT * FROM celebs')

items = cursor.fetchall()

for i in items:
    name, genre, num_albums, age, awards, years_in_industry = i
    print(f'{name:17}{genre:14}{num_albums:10}{age:14}{awards:14}{years_in_industry:14}')

conn.commit()

conn.close()

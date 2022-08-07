import sqlite3

print("Sucessfully imported module")


conn = sqlite3.connect("SGA_1_3_learners.db")

print("Database created sucessfully!") ; print(type(conn))


cursor = conn.cursor()

print("Cursor created sucessfully \n", type(cursor))


# cursor.execute("""
#                 CREATE TABLE learners (
#                     first_name TEXT,
#                     last_name TEXT,
#                     email TEXT,
#                     course TEXT
#                     )
# """)

print("table created successfully")

learners_list = [("Abubakar", "Adisa", "adisaabubakar@gmail.com", "Data Science"), 
                ("Adebisi", "Afolabi", "wasola.afolabi@yahoo.com", "Data Science"), 
                ("Adedoyin", "Abass", "doyinabass0@gmail.com", "Data Science"), 
                ("Awonaike", "Tawakalitu", "purpleduralumin@gmail.com", "Data Science"), 
                ("Babajide", "Adesugba", "jide_ade@hotmail.com", "Data Science"), 
                ("Bukola", "Ajayi", "bukolam.ajayi@gmail.com", "Data Science"), 
                ("Binta", "Umar", "ubinta63@yahoo.com", "Data Science"), 
                ("Christian", "Uzondu", "uzonduchristian2@gmail.com", "Data Science"), 
                ("Cynthia", "Awiya", "awiyac@yahoo.com", "Data Science"), 
                ("Deborah", "Olorunnishola", "deboraholuwatobi247@gmail.com", "Data Science"), 
                ("Eke", "Ihuoma", "ihuomaeke28@gmail.com", "Data Science"), 
                ("Esther", "Akpanowo", "estherakpanowo@gmail.com", "Data Science"), 
                ("Eniola", "Osadare", "dorcasosadare@gmail.com", "Data Science"), 
                ("Etariemi", "Louis", "etariemilouis@gmail.com", "Data Science"), 
                ("Faith", "Amure", "amuretalodabif@gmail.com", "Data Science"), 
                ("Ganiyat", "Shittu", "ganiyatas@gmail.com", "Data Science"), 
                ("Gideon", "Uko", "ukogideon13@gmail.com", "Data Science"), 
                ("Idowu", "Adesanya", "idsworld22@yahoo.com", "Data Science"), 
                ("Joyce", "Ezeonwu", "joyceokore@gmail.com", "Data Science"), 
                ("Kehinde", "Orolade", "kehindeorolade@gmail.com", "Data Science"), 
                ("Kafayat", "Ibrahim", "kafayatadenike10@gmail.com", "Data Science"), 
                ("Lawrence", "Aneshimokha", "anelawrence1@gmail.com", "Data Science"), 
                ("Mariam", "Adeoti", "adetutuadebola28@gmail.com", "Data Science"), 
                ("Ogechi", "Njemanze", "ogenjemz@gmail.com", "Data Science"), 
                ("Omowunmi", "Awonirana", "Awonirana", "Data Science"), 
                ("Placidus", "Ali", "Placidusali@gmail.com", "Data Science"), 
                ("Praise", "Emmanuel", "praiseemmanuel9ic@gmail.com", "Data Science"), 
                ("Prince", "Ekeocha", "prince.ekeocha@gmail.com", "Data Science"), 
                ("Rasheedat", "Sikiru", "rasheedatsikiru@gmail.com", "Data Science"), 
                ("Ramotallah", "Jubril", "jubrilramotallah03@gmail.com", "Data Science"), 
                ("Sheriiff", "Azeez", "SheriffOlaitan71@gmail.com", "Data Science"), 
                ("Stephen", "Ogungbile", "stephenfunso@gmail.com", "Data Science"), 
                ("Temitope", "Bamidele", "bamideletemitope42@gmail.com", "Data Science"), 
                ("Theresa", "Karamor", "teriekarie@gmail.com", "Data Science"), 
                ("Tina", "Uyateide", "tinauyats@gmail.com", "Data Science"), 
                ("Victoria", "Chukwuno", "chukwunovictoria@gmail.com", "Data Science")]

cursor.executemany('INSERT INTO learners VALUES(?, ?, ?, ?)', learners_list)

print("We have inserted", cursor.rowcount, "records to the table")

cursor.execute("SELECT * FROM learners")

items = cursor.fetchall()

print("FIRST NAME" + "\t LAST NAME" + "\t EMAIL" "\t\t\t\t\t COURSE \n" f"{'.' * 100}")

# for i in items:
#     print(i[0] + "\t\t" + i[1] + "\t\t" + i[2] + "\t\t\t" + i[3])

for i in items:
    first_name, last_name, email, course = i
    print(f"{first_name:16}{last_name:16}{email:16} \t\t\t {course}")

# commit the database and table
conn.commit()

conn.close()
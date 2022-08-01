# Create an inventory table containing  10  or more items, showing cost price and the quantity in stock. Give each item an ID
# The business owner wants to see the items to restock and which is sufficient from the highest to lowest cost price.

import sqlite3

conn = sqlite3.connect("inventory.db")
print('successful')
c = conn.cursor()

# c.execute("""CREATE TABLE stock(
#                     id INTERGER, 
#                     item TEXT, 
#                     quantity INTERGER,
#                     price INTEGER
                    
#     )""")

list_of_items = [(1, 'bread', 38, 600), 
                (2, 'sugar', 16, 200), 
                (3, 'soap', 65, 300), 
                (4, 'indomie', 34, 150), 
                (5, 'milo', 7, 500), 
                (6, 'milk', 23, 400), 
                (7, 'raid', 9, 900), 
                (8, 'coke', 38, 200),
                (9, 'pepsi', 73, 150), 
                (10, 'cooking oil', 54, 850),
                (11, 'butter', 21, 300)
                ]


c.executemany("INSERT INTO stock VALUES(?, ?, ?, ?)", list_of_items)


print("We have inserted", c.rowcount, "records to the table")

conn.commit()
conn.close()



import sqlite3
conn = sqlite3.connect("mall.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS mall
(row int,product_code text ,product_name text,
price int, quantity int,total_price real)''')
conn.commit()
conn.close()

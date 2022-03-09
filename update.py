import sqlite3
conn = sqlite3.connect("mall.db")
c = conn.cursor()
c.execute('UPDATE mall SET product_name = "M" WHERE product_name = "G"');
conn.commit()
conn.close()

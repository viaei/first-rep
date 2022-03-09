import sqlite3
conn = sqlite3.connect("mall.db")
c = conn.cursor()
c.execute("DELETE from mall where row = 5 ",);
conn.commit()
conn.close()

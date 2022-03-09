import sqlite3
conn = sqlite3.connect("mall.db")
c = conn.cursor()
inputs = [(1,'001','A',1200,1000,1200*1000),
          (2,'002','B',500,2000,500*2000),
          (3,'003','C',600,3500,500*3500),
          (4,'004','D',230,4000,230*4000),
          (5,'005','E',150,7000,150*7000),
          (6,'006','F',420,160,420*160),
          (7,'007','G',320,700,3200*700)]
c.executemany('INSERT INTO mall VALUES(?,?,?,?,?,?);',inputs);
conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect('movie list.db')
c = conn.cursor()
c.execute("SELECT * from movies")
c.execute("SELECT * from movies where Actor='chris hemsworth'")
print(c.fetchall())
conn.commit()

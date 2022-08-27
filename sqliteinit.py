import sqlite3
con = sqlite3.connect("database.db")
con.execute("DROP TABLE IF EXISTS Context")
con.execute("CREATE TABLE Context (text TEXT, ctext TEXT)")
con.execute("INSERT INTO Context VALUES ('try it', 'try')")
con.commit()

import sqlite3


class SQLDatabase():
    '''
        Our SQL Database

    '''

    # Get the database running
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def storeText(self, text, ctext):
        query = """
                INSERT INTO Context VALUES (?, ?);
                """
        self.cur.execute(query, (text, ctext))

    def getText(self):
        query = """
                SELECT * FROM Context;
                """
        self.cur.execute(query)
        results = self.cur.fetchall()
        return results


## thing for test
if __name__ == "__main__":
    testpr = SQLDatabase()
    testpr.storeText("fix it", "fix")
    res = testpr.getText()
    print(res)

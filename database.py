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


    def storeText(self, text: str, ctext: str) -> NULL:
        """
        To store the context use input and the result
        concluded from the ML algorithnm

        storeText(text, ctext)
        text: User text input
        ctext: The conclusion of the text user input
        """
        query = """
                INSERT INTO Context VALUES (?, ?);
                """
        self.cur.execute(query, (text,ctext))


    def getText(self) -> str:
        """
        To get the original context and the result concluded from the Algorithnm

        getText()
        output: [(original Context, conclusion text)]
        """
        query = """
                SELECT * FROM Context;
                """
        self.cur.execute(query)
        results = self.cur.fetchall()
        return results

## thing for test
# testpr = SQLDatabase()
# testpr.storeText("fix it", "fix")
# res = testpr.getText()
# print(res)

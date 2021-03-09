import mysql.connector

class Connection:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='storage',
                                            user='root',
                                            password='password')
        self.my_cursor = self.conn.cursor()

    def iud(self, query, values):
        try:
            self.my_cursor.execute(query, values)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def show(self, query):
        self.my_cursor.execute(query)
        return self.my_cursor.fetchall()


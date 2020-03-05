
from mysql.connector import MySQLConnection, Error
from settings import db_config, create_tables_query

class DBmodel:
    def __init__(self):
        self.dbconfig = db_config()
        self.conn = MySQLConnection(**self.dbconfig)
        self.cursor = self.conn.cursor()
        
    def create_tables(self):
        query = create_tables_query()
        try:
            cursor = self.cursor
            for result in cursor.execute(query, multi=True):
                if result.with_rows:
                    print("Rows produced by statement '{}':".format(
                    result.statement))
                    print(result.fetchall())
                else:
                    print("Number of rows affected by statement '{}': {}".format(
                    result.statement, result.rowcount))
        except Error as e:
            print(e)

    def query_with_fetchone(self):
        try:
            cursor = self.cursor
            cursor.execute("SHOW TABLES") 
            row = cursor.fetchone() 
            while row is not None:
                print(row)
                row = cursor.fetchone()
    
        except Error as e:
            print(e)
    
    def insert_request(self, params):
        query = "INSERT INTO requests_table VALUES('',"
        for key, value in params.items():
            query += "'" + str(value) + "', "
        query = query[:-2]
        query += ");"
        try:
            cursor = self.cursor
            cursor.execute(query) 
            self.conn.commit()
            print("Insert request data is success.")
        except Error as e:
            print("Request table: " + e)

    def insert_listings(self, rows):
        try:
            cursor = self.cursor
            for row in rows:
                cursor.execute("INSERT INTO responses_table VALUES %r;" % (tuple(row),)) 
            self.conn.commit()
            print("Insert listing data is success.")
        except Error as e:
            print("Listing Table:" + e)
        
    def test_table(self, table):
        try:
            cursor = self.cursor
            cursor.execute("SELECT * FROM " + table) 
            # cursor.execute("SHOW COLUMNS FROM " + table) 
            # cursor.execute("SHOW TABLES;")
            row = cursor.fetchone() 
            while row is not None:
                print(row)
                row = cursor.fetchone()
    
        except Error as e:
            print(e)
    
    def get_column_names(self, table):
        column_names = []
        try:
            cursor = self.cursor
            cursor.execute("SHOW columns FROM " + table)
            for column in cursor.fetchall():
                column_names.append(column[0])    
            return column_names
        except Error as e:
            print(e)
        
    

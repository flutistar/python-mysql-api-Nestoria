from db import DBmodel

model = DBmodel()
# model.test_table('responses_table')
# model.get_column_names('responses_table')
model.create_tables()
model.cursor.close()
model.conn.close()

HOST = 'sql7.freemysqlhosting.net'
DATABASE = 'sql7324452'
USER = 'sql7324452'
PASSWORD = 'STqAiuN9jI'
PORT = '3306'

def db_config():
    return {
        'host': HOST,
        'database': DATABASE,
        'user': USER,
        'password': PASSWORD,
        'port': PORT
    }

def create_tables_query():
    return "DROP TABLE IF EXISTS requests_table; \
                                                    \
            CREATE TABLE requests_table \
            (id INT NOT NULL AUTO_INCREMENT UNIQUE, \
            country VARCHAR(2), \
            language VARCHAR(2), \
            location VARCHAR(40), \
            num_res VARCHAR(4), \
            offset INT, \
            output VARCHAR(10), \
            page INT, \
            pretty VARCHAR(3), \
            product_type VARCHAR(20), \
            property_type VARCHAR(20), \
            size_type VARCHAR(10), \
            size_unit VARCHAR(5), \
            sort VARCHAR(20), \
            listing_type VARCHAR(20), \
            insert_time DATETIME); \
                                        \
            DROP TABLE IF EXISTS responses_table; \
                                                    \
            CREATE TABLE responses_table \
            (id INT NOT NULL AUTO_INCREMENT UNIQUE, \
            bathroom_number INT, \
            bedroom_number INT, \
            car_spaces VARCHAR(20), \
            commission INT, \
            construction_year INT, \
            datasource_name VARCHAR(20), \
            floor INT, \
            img_height INT, \
            img_url VARCHAR(255), \
            img_width INT, \
            keywords VARCHAR(255), \
            latitude FLOAT, \
            lister_name VARCHAR(30), \
            lister_url VARCHAR(255), \
            listing_type VARCHAR(10), \
            location_accuracy INT, \
            longitude FLOAT, \
            price INT, \
            price_currency VARCHAR(4), \
            price_formatted VARCHAR(10), \
            price_high FLOAT, \
            price_low FLOAT, \
            price_type VARCHAR(10), \
            property_type VARCHAR(10), \
            room_number TINYINT, \
            size INT, \
            size_type VARCHAR(10), \
            size_unit VARCHAR(4), \
            summary TEXT, \
            thumb_height TINYINT, \
            thumb_url VARCHAR(255), \
            thumb_width INT, \
            title VARCHAR(255), \
            updated_in_days TINYINT, \
            updated_in_days_formatted VARCHAR(10), \
            insert_time DATETIME);"
        
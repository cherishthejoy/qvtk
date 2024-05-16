import sqlite3

def connect_db():
    return sqlite3.connect('ishtar.db')

def create_table(cursor):
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS book_info(
                        title TEXT,
                        publisher TEXT,
                        isbn TEXT,
                        published_date DATE,
                        language TEXT,
                        author TEXT,
                        category TEXT,
                        price REAL,
                        dimension TEXT,
                        print_date DATE, 
                        stock TEXT, 
                        cover_type TEXT, 
                        page_count INTEGER)
    ''')


def insert_data(cursor, data):
    cursor.execute('''
        INSERT INTO book_info(
            title, publisher, isbn, published_date, language,
            author, category, price, dimension, print_date, stock,
            cover_type, page_count)
    ''', data)
    
    
def initialize_db():
    connection = connect_db()
    cursor = connection.cursor()
    create_table(cursor)
    connection.commit()
    connection.close()
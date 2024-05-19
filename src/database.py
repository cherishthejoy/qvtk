import os
import sqlite3


def connect_db():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, 'ishtar.db')
    return sqlite3.connect(db_path)

def create_table(cursor):
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS book_info(
                        title TEXT,
                        author TEXT,
                        language TEXT,
                        isbn TEXT,
                        publisher TEXT,
                        published_date DATE,
                        page_count INTEGER,
                        print_date DATE,
                        category TEXT,
                        cover_type TEXT,
                        license TEXT, 
                        dimension TEXT, 
                        price REAL, 
                        stock INTEGER,
                        synopsis TEXT)
    ''')


def insert_data(cursor, data):
    cursor.execute('''
        INSERT INTO book_info(
            title, author, language, isbn, publisher, published_date,
            page_count, print_date, category, cover_type, license, dimension,
            price, stock, synopsis)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    

def initialize_db():
    connection = connect_db()
    cursor = connection.cursor()
    create_table(cursor)
    connection.commit()
    connection.close()
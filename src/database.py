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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    

def initialize_db():
    connection = connect_db()
    cursor = connection.cursor()
    create_table(cursor)
    connection.commit()
    connection.close()
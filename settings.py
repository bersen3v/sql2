import sqlite3
from sqlite3 import Error
import pandas as pd 
from sqlalchemy import create_engine

#Соединиться с файлом
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"Ошибка соединения: '{e}'")
    return connection

def execute_query(db_name, query):
    connection = create_connection(f"{db_name}.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"Ошибка запроса: '{e}'")

def execute_read_query(db_name, query):
    connection = create_connection(f"{db_name}.sqlite")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Ошибка запроса: '{e}'")



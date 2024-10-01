import tkinter as tk
from pandastable import Table
import pandas as pd 
from sqlalchemy import create_engine
import sqlite3

def show_as_new_window(name):
    conn = sqlite3.connect(f'{name}.sqlite')
    df = pd.read_sql(sql=f"SELECT * FROM {name}", con=conn)
    root = tk.Tk()
    root.title(f'{name}')
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)
    pt = Table(frame, dataframe=df)
    pt.show()
    root.mainloop()


def show_to_console(db_name):
    cnx = create_engine(f'sqlite:///{db_name}.sqlite').connect()
    df = pd.read_sql_table(db_name, cnx)
    print(df)  
    print() 
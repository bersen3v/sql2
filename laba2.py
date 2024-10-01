# База данных для казино
import settings as sql
import view
import pandas as pd
import sqlite3
from user import User



class T:
    users = "users" #фио строка
    ages = "ages" #возраст инт
    reg_date = "reg_date" #дата дейттайм
    profit = "profit" #сколько игр сыграл, сколько выиграл, сколько проиграл, на сколько казино в плюсе, bool казино в плюсе или нет, сколько выиграл игрок, bool игрок в плюсе или нет, сколько игрок должен проиграть
    cards = "cards"
    contacts = "contacts"
    

class C:
    id = "id"

    surname = "surname"
    name = "name"

    age = "age"

    credit_card = "credit_card"

    phone_number = "phone_number"

    reg_date = "reg_date" 

    games_counter = "games_counter"
    win_money = "win_money"
    loose_money = "loose_money"
    casino_profit = "casino_profit"
    is_casino_win = "is_casino_win"
    player_profit = "player_profit"
    is_player_win = "is_player_win"
    how_player_need_loose = "how_player_need_loose"



for table in [T.users, T.ages, T.reg_date, T.profit, T.cards, T.contacts]:
    sql.execute_query(
    table,
    f"""
        DROP TABLE {table}
    """
)

sql.execute_query(
    T.users,
    f"""
        CREATE TABLE {T.users} (
            {C.id} INTEGER PRIMARY KEY NOT NULL,
            {C.surname} TEXT NOT NULL,
            {C.name} TEXT NOT NULL
        );
    """
)


sql.execute_query(
    T.ages,
    f"""
        CREATE TABLE {T.ages} (
            {C.id} INTEGER PRIMARY KEY NOT NULL,
            {C.age} INTEGER NOT NULL CHECK({C.age} > 17),
            FOREIGN KEY ({C.id}) REFERENCES {T.users} ({C.id})
        );
    """
)

sql.execute_query(
    T.reg_date,
    f"""
        CREATE TABLE {T.reg_date} (
            {C.id} INTEGER PRIMARY KEY NOT NULL,
            {C.reg_date} INTEGER NOT NULL,
            FOREIGN KEY ({C.id}) REFERENCES {T.users} ({C.id})
        );
    """
)


sql.execute_query(
    T.cards,
    f"""
        CREATE TABLE {T.cards} (
            {C.id} INTEGER PRIMARY KEY NOT NULL,
            {C.credit_card} INTEGER NOT NULL CHECK({C.credit_card} > 999999999999999 AND {C.credit_card} < 10000000000000000),
            FOREIGN KEY ({C.id}) REFERENCES {T.users} ({C.id})
        );
    """
)

sql.execute_query(
    T.contacts,
    f"""
        CREATE TABLE {T.contacts} (
            {C.id} INTEGER PRIMARY KEY NOT NULL,
            {C.phone_number} INTEGER NOT NULL,
            FOREIGN KEY ({C.id}) REFERENCES {T.users} ({C.id})
        );
    """
)

sql.execute_query(
    T.profit,
    f"""
        CREATE TABLE {T.profit} (
            {C.id} INTEGER NOT NULL PRIMARY KEY,
            {C.games_counter} INTEGER NOT NULL,
            {C.win_money} INTEGER NOT NULL,
            {C.loose_money} INTEGER NOT NULL,
            {C.casino_profit} INTEGER GENERATED ALWAYS AS ({C.loose_money} - {C.win_money}) STORED,
            {C.is_casino_win} BLOB GENERATED ALWAYS AS ({C.casino_profit} > 0) STORED,
            {C.player_profit} INTEGER GENERATED ALWAYS AS ({C.win_money} - {C.loose_money}) STORED,
            {C.is_player_win} BLOB GENERATED ALWAYS AS ({C.player_profit} > 0) STORED,
            {C.how_player_need_loose} INTEGER GENERATED ALWAYS AS (0 - {C.player_profit}) STORED,
            FOREIGN KEY ({C.id}) REFERENCES {T.users} ({C.id}) ON DELETE CASCADE
        );
    """
)
users = []
for i in range(100):
    user = User()
    user.id = i
    print(user.id)
    users.append(user)
    sql.execute_query(
        T.users,
        f"""
            INSERT INTO {T.users} VALUES ({user.id}, '{user.name}', '{user.surname}');
        """
    )

view.show_as_new_window(T.users)

for user in users:
    sql.execute_query(
        T.profit,
        f"""
            INSERT INTO {T.profit} VALUES ({user.id}, {user.game_counter}, {user.win_money}, {user.loose_money});
        """
    )

    sql.execute_query(
        T.ages,
        f"""
            INSERT INTO {T.profit} VALUES ({user.id}, {user.game_counter}, {user.win_money}, {user.loose_money});
        """
    )

view.show_as_new_window(T.profit)

sql.execute_query(
    T.users,
    f"""
        DELETE FROM {T.users};
    """
)
view.show_as_new_window(T.profit)


# view.show_as_new_window(T.profit, T.profit)

print('end')








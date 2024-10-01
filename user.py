import random
import datetime
# id = "id"

    # surname = "surname"
    # name = "name"

    # age = "age"

    # credit_card = "credit_card"

    # phone_number = "phone_number"

    # reg_date = "reg_date" 

    # games_counter = "games_counter"
    # win_money = "win_money"
    # loose_money = "loose_money"
    # casino_profit = "casino_profit"
    # is_casino_win = "is_casino_win"
    # player_profit = "player_profit"
    # is_player_win = "is_player_win"
    # how_player_need_loose = "how_player_need_loose"

surnames = ['Иванов', 'Петров', 'Сидоров']
names = ['иван', 'степан', 'сидр']

class User:
    id = 0
    def __init__(self):
        self.surname = surnames[random.randint(0,len(surnames)-1)]
        self.name = names[random.randint(0,len(names)-1)]
        self.age = random.randint(14,100)
        self.credit_card = random.randint(999999999999999, 10000000000000000-1)
        self.phone_number = random.randint(10000000000, 99999999999)
        self.reg_date = datetime.datetime.now().strftime("%d.%m.%Y")
        self.game_counter = random.randint(100, 1000)
        self.win_money = random.randint(0, 10000)
        self.loose_money = random.randint(0, 10000)

    def to_string(self):
        print(self.id, self.name, self.surname)

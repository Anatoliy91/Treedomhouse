import json
import random

# этот метод парсит Джейсон и возвращает дикт
def default_json_to_dict(json_data):
    dict_data = json.loads(json_data)
    return dict_data

# этот метод превращает дикт в Джейсон. Возвращает джейсон
def default_dict_to_json(diction):
    jsondata = json.dumps(diction)
    return jsondata

def get_random_password():
    # возвращает рандомные пароль
    password = "Qazzxca" + str(random.randrange(20, 2000))
    return password

def get_random_email():
    # возвращает рандомны емейл
    email = "dubinaanatolii" + str(random.randint(100, 1000)) + "@gmail.com"
    return email
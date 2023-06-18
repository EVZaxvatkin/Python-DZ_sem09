
import csv
import datetime
import json
import os
import random
from typing import Callable

def deco(func: Callable):
    csv_number()

    def wrapper(*args, **kwargs):

        with open('num_rand.csv', 'r', encoding='UTF-8') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if row and row[0] != 0:
                    func(*row)

    return wrapper()

def csv_number():
    with open('num_rand.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for i in range(10, 100):
            row = [random.randint(1, 15) for j in range(3)]
            writer.writerow(row)

def json_result(func: Callable):
    result = {}
    if os.path.exists('result.json'):
        with open('result.json', 'r', encoding='UTF-8') as file:
            result = json.load(file)

    def wrapper(*args):
        res = func(*args)
        data_func = {'a': args[0], 'b': args[1], 'c': args[2], 'result': res}
        res_key = f'{datetime.datetime.now()}'
        result[res_key] = result.get(res_key) + [data_func] if result.get(res_key) else [data_func]
        with open('result.json', 'w', encoding='UTF-8') as file:
            json.dump(result, file)
        return res
    return wrapper


@deco
@json_result
def func1(a: int, b: int, c: int):

    d = b**2 - (4*a*c)

    if d == 0:
        x = (-b/(2*a))
        return round(x, 2)

    elif d> 0:
        x1 = ((-b + d**0.5)/(2*a))
        x2 = ((-b - d**0.5)/(2*a))
        return round(x1, 2), round(x2, 2)



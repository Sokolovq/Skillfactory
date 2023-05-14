import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CurrencyException():
    @staticmethod
    def get_price(quote, base, amount):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты - {base}')

        if quote not in keys:
            raise ConvertionException(f'Неверно введена валюта {quote}')

        if base not in keys:
            raise ConvertionException(f'Неверно введена валюта {base}')

        try:
            type(float(amount)) != float
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={keys[quote]}{keys[base]}&key=89a5a3f9637963e25ac9a55480c47b50')
        total_base = float(json.loads(r.content)['data'][f'{keys[quote]}{keys[base]}']) * int(amount)

        return total_base

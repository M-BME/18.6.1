python
import requests
import json
from extensions import APIException, CurrencyCodes


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float) -> float:
        if base == quote:
            return amount

        if base not in CurrencyCodes.get_currency_codes() or quote not in CurrencyCodes.get_currency_codes():
            raise APIException('Неверное имя валюты')

        try:
            response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}&symbols={quote}')
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise APIException('Ошибка при запросе курса валют')

        result = json.loads(response.text)['rates'][quote] * amount
        return round(result, 2)
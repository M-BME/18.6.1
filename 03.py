python
class CurrencyCodes:
    @staticmethod
    def get_currency_codes() -> dict:
        return {
            'USD': 'Доллар США',
            'EUR': 'Евро',
            'RUB': 'Российский рубль',
            'GBP': 'Фунт стерлингов',
            'JPY': 'Японская иена',
            'AUD': 'Австралийский доллар',
            'CAD': 'Канадский доллар',
            'CHF': 'Швейцарский франк',
            'CNY': 'Китайский юань',
            'HKD': 'Гонконгский доллар'
        }


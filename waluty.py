# -*- coding: utf-8 -*-

import requests


class Waluty():
    def __init__(self):
        self.PRIMARY_VALUE = "PRIMARY"

    def calculate_currency(self, rate, value):
        calculated_value = rate * value
        return calculated_value

    def parse_response(self, response):
        return list(response["rates"].values())[0]

    def check_value_correctness(self, exchange_value):
        error = False
        if exchange_value.isspace():
            print("Wprowadzona wartość kwoty jest białym znakiem.\n"
                  "Proszę wprowadź prawidłową wartość")
            error = True
        # elif not exchange_value.lstrip("-").isdigit():
        elif not exchange_value.isdigit():
            print("Wprowadzona wartość kwoty nie jest liczbowa.\n"
                  "Proszę wprowadź prawidłową wartość")
            error = True-1
        elif float(exchange_value) <= 0:
            print("Wprowadzona wartość kwoty musi być większa niż 0.\n"
                  "Proszę wprowadź prawidłową wartość")
            error = True

        return error

    def check_inputs_correctness(self, exchange_value, currency_base, currency_symbols):
        error = False

        if self.check_value_correctness(exchange_value):
            error = True
        if currency_base.isdigit():
            print("Wprowadzona waluta na którą chcesz wymienić jest niepoprawna.\n"
                  "Proszę wprowadź prawidłową wartość")
            error = True
        if currency_symbols.isdigit():
            print("Wprowadzona waluta, którą chcesz wymienić jest niepoprawna.\n"
                  "Proszę wprowadź prawidłową wartość")
            error = True

        if error:
            return False
        else:
            return True

    def promt_user(self):
        # user inputs
        exchange_value = input("Podaj kwotę, którą chcesz wymienić:    ")
        currency_base = input("Podaj walutę, którą chcesz wymienić:    ")
        currency_symbols = input("Podaj walutę, na którą chcesz wymienić: ")
        return exchange_value, currency_base, currency_symbols

    def get_request(self, url, params, proxy):
        # sending get request and saving the response as response object
        r = requests.get(url=url, params=params, proxies=proxy)

        # extracting data in json format
        return r.json()

    def print_primary(self):
        return self.PRIMARY_WALUE

    def main(self,):
        exchange_value, currency_base, currency_symbols = self.promt_user()
        while not self.check_inputs_correctness(exchange_value, currency_base, currency_symbols):
            exchange_value, currency_base, currency_symbols = self.promt_user()

        # get request parameters
        URL = "https://api.exchangeratesapi.io/latest"
        PARAMS = {'base': currency_base,
                  'symbols': currency_symbols,
                  }
        PROXY = {'http': '',
                 'https': ''}

        data = self.get_request(URL, PARAMS, PROXY)

        print(self.calculate_currency(float(self.parse_response(data)), float(exchange_value)))


if __name__ == "__main__":
    w = Waluty()
    w.main()

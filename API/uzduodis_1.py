import json
import requests


def get_rate(cur_1: str, cur_2: str):
    try:
        r = requests.get(f'https://api.frankfurter.app/latest?from={cur_1}')
        dictionary = json.loads(r.text)
        print(f"{cur_1}-{cur_2}:\t{dictionary['rates'][cur_2]}")
    except:
        r = requests.get(f'https://api.frankfurter.app/currencies')
        cur_dict = json.loads(r.text).keys()
        print("Neteisingai suvestos valiutos. Galimų variantų sąrašas:")
        print(cur_dict)


get_rate('AUR', 'GBP')

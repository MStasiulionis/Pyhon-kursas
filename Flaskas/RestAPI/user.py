import requests
import json

payload = {'pavadinimas': 'Paskambinti namo', 'atlikta': True}
r = requests.post('http://127.0.0.1:8000/uzduotis', json=payload)
# dictionary = json.loads(r.text)
# print(dictionary)
s = requests.get('http://127.0.0.1:8000/uzduotis')
a = requests.get('http://127.0.0.1:8000/uzduotis/1')
d = requests.delete('http://127.0.0.1:8000/uzduotis/100')
update_payload = {'pavadinimas': 'Pareiti namo', 'atlikta': False}
u = requests.put('http://127.0.0.1:8000/uzduotis/2', json=update_payload)
pass
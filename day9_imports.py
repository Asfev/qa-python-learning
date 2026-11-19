# Задача 1. import math
import math

print(round(math.pi, 4))
print(math.sqrt(144))
print(math.floor(3.7), math.ceil(3.2))

# Задача 2. import random
import random as ran

print(f'Random int: {ran.randint(1, 100)}')
print(f'Random status: {ran.choice([200, 201, 404, 500])}')

# Задача 3. import json
import json

response = {'status': 200, 'body': 'ok', 'headers': {'Content-Type': 'application/json'}}

json_text = json.dumps(response)
print(json_text)
json_parsed = json.loads(json_text)
print(type(json_parsed))
print(json_parsed['status'])

# Задача 4. Свой модуль — utils.py
import utils

print(utils.safe_int('200'))
print(utils.safe_int('abc'))
print(utils.validate_status(200))
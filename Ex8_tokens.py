import requests
import json
from json.decoder import JSONDecodeError
import time


def json_loads(text):
    obj = None
    try:
        if text == '':
            return
        else:
            obj = json.loads(text)
    except NameError:
        print("json_text is empty")
    except JSONDecodeError:
        print("json_text is a not JSON format")
    return obj


def get_json_key_value(key_name):
    try:
        key_value = obj[key_name]
        return key_value
    except KeyError:
        print(f"no key name = {key_name}")


def is_token_has_tasks():
    try:
        error = get_json_key_value("error")
        return error != "No job linked to this token"
    except KeyError:
        return false


URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

# Создаем задачу
response = requests.get(URL)
obj = json_loads(response.text)
token = get_json_key_value("token")
seconds = get_json_key_value("seconds")
print(response.text)

# Проверяем наличие задач на токене
URL_with_token = URL + "?token=" + token
response = requests.get(URL_with_token)
obj = json_loads(response.text)

if is_token_has_tasks():
    # Запрос ДО того как задача готова
    status = get_json_key_value("status")
    print(f"{response.status_code} | {status} - {status == 'Job is NOT ready'}")

    # Ждем завершения задачи
    time.sleep(seconds)

    # Запрос ПОСЛЕ того как задача готова
    response = requests.get(URL_with_token)
    obj = json_loads(response.text)
    result = get_json_key_value("result")
    status = get_json_key_value("status")

    print(f"{response.status_code} | {status} - {status == 'Job is ready'} | result = {result}")
else:
    print(f"Для токена {token} нет задач")

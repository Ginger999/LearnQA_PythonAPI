import requests


class TestCookie:

    def test_homework_cookie(self):
        URL = "https://playground.learnqa.ru/api/get_cookie"

        # Ожидаемые значения запроса
        expected_status_code = 200
        expected_cookie_name = "MyCookie"
        expected_cookie_value = "12345"

        # Отправляем запрос
        response = requests.get(URL)

        # Получаем актуальные значения запроса
        actual_response_code = response.status_code

        # Сравниваем актуальные и ожидаемые значения запроса
        assert actual_response_code == expected_status_code, f"Wrong response code {actual_response_code}"

        actual_cookies = dict(response.cookies)
        # print(f"{actual_cookies}")
        assert expected_cookie_name in actual_cookies, f"There is no field {expected_cookie_name} in cookies"

        actual_cookie_value = actual_cookies[expected_cookie_name]
        assert actual_cookie_value == expected_cookie_value, f"Wrong cookie MyCookie value {actual_cookie_value}"

import requests


class TestCookie:

    def test_homework_cookie(self):
        URL = "https://playground.learnqa.ru/api/get_cookie"

        # Ожидаемые значения запроса
        expected_status_code = 200
        expected_cookie_MyCookie = "12345"

        # Отправляем запрос
        response = requests.get(URL)

        # Получаем актуальные значения запроса
        actual_response_code = response.status_code

        actual_cookies = dict(response.cookies)
        # print(f"{actual_cookies}")
        actual_cookie_MyCookie = actual_cookies.get("MyCookie")

        # Сравниваем актуальные и ожидаемые значения запроса
        assert actual_response_code == expected_status_code, f"Wrong response code {actual_response_code}"
        assert actual_cookie_MyCookie == expected_cookie_MyCookie, f"Wrong cookie MyCookie value {actual_cookie_MyCookie}"

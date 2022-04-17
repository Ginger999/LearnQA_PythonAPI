import requests
import datetime


class TestHeaders:

    def test_homework_headers(self):
        # Отправляем запрос
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        now = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
        # print(now)

        # Ожидаемые значения запроса
        expected_headers = {
            'Date': now,
            'Content-Type': 'application/json',
            'Content-Length': '15',
            'Connection': 'keep-alive',
            'Keep-Alive': 'timeout=10',
            'Server': 'Apache',
            'x-secret-homework-header': 'Some secret value',
            'Cache-Control': 'max-age=0',
            'Expires': now
            }
        expected_status_code = 200

        # Актуальные значения запроса
        actual_response_code = response.status_code
        headers = dict(response.headers)
        print(f"\n{headers}")

        # Сравниваем актуальные и ожидаемые значения запроса
        # 1) Проверяем status_code
        assert actual_response_code == expected_status_code, f"Wrong response code {actual_response_code}"

        # 2) Проверяем вернулся ли заголовок в ответе
        for ex_header in expected_headers:
            assert ex_header in headers.keys(), f"'{ex_header}' header does not present in response.headers"
            assert expected_headers[ex_header] == headers[ex_header], f"'{ex_header}' header contains a wrong value '{headers[ex_header]}' instead of '{expected_headers[ex_header]}'"
            print(f"{ex_header}: headers[ex_header]")

        # 3) Проверяем все ли возможные заголовки изначально заложили в expected_headers
        for header in headers:
            assert header in expected_headers.keys(), f"'{header}' header not taken into account for validation in expected {expected_headers.keys()}"


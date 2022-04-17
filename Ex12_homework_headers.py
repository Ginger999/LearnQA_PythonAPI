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
        expected_headers_len = expected_headers.__len__()

        # Актуальные значения запроса
        actual_response_code = response.status_code
        headers = dict(response.headers)
        actual_headers_len = headers.__len__()
        print(headers)

        # Сравниваем актуальные и ожидаемые значения запроса
        # 1) Проверяем status_code
        assert actual_response_code == expected_status_code, f"Wrong response code {actual_response_code}"

        # 2) Проверяем все ли возможные заголовки изначально заложили в expected_headers
        if actual_headers_len > expected_headers_len:
            print(f"Headers вернулось больше {actual_headers_len}, чем проверяем {expected_headers_len} - не все возможные заголовки учтены изначально!")

        # 3) Проверяем вернулся ли заголовок в ответе
        for ex_header in expected_headers:
            assert ex_header in headers.keys(), f"'{ex_header}' header does not present in response.headers"
            assert expected_headers[ex_header] == headers[ex_header], f"'{ex_header}' header contains a wrong value '{headers[ex_header]}' instead of '{expected_headers[ex_header]}'"

        # 4) Проверяем все ли возможные заголовки изначально заложили в expected_headers
        for header in headers:
            assert header in expected_headers.keys(), f"'{header}' header not taken into account for validation in expected {expected_headers.keys()}"

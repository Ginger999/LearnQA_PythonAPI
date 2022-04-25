import requests
import datetime
import pytest
from requests import Response
import json


class TestHeaders:
    url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

    user_agents = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'),
      ]

    sources = {'device': ['iOS', 'Android', 'iPhone'],
               'browser': ['Chrome', 'Mozilla'],
               'platform': ['Mobile', 'Web', 'Googlebot']
               }

    @pytest.mark.parametrize('user_agent', user_agents)
    def test_homework_headers(self, user_agent):
        # Отправляем запрос
        response = requests.get(self.url, headers={"User-Agent": user_agent})

        # Проверяем, что ответ в формате JSON
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        # Проверяем, что все устройстка из списка есть в ответе
        for source in self.sources:
            pass
            assert source in response_as_dict, f"Response JSON does not have key '{source}'"

        # Проврем, что каждое устройство определилось
        for source in self.sources:
            assert response_as_dict[source] != 'Unknown', f"'{source}' is Unknown. It could be {self.sources[source]}"

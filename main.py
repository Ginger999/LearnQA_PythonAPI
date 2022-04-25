import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
i = 0
url = ''
for h in response.history:
    i += 1
    url = h.url
    print(f"{i}: {h} {h.url}")

print(f" \nNumber of redirects: {i} \nFinal URL: {url}")

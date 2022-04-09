import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
i = 0
for h in response.history:
    i += 1
    print(f"{i}: {h}")

print(f" \nNumber of redirects: {i} \nURL: {h}")
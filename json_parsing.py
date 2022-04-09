import json
from json.decoder import JSONDecodeError

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

try:
    obj = json.loads(json_text)
    print(obj['messages'][1]['message'])
except JSONDecodeError:
    print("json_text is a not JSON format")
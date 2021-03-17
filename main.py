import requests

result = requests.get("https://official-joke-api.appspot.com/jokes/programming/ten")
print(result.status_code)
joke = result.json()
print(joke[0])

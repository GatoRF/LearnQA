import requests


response = requests.post('https://playground.learnqa.ru/api/long_redirect')
history_lincs = response.history
vto = response


print(history_lincs)
print(vto.url)


import requests
import json
from pprint import pprint

user = 'Ermolai'
main_link = f'https://api.github.com/users/{user}/repos'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

response = requests.get(main_link, headers=header)

if response.ok:
    data =json.loads(response.text) # response.json()

# print(type(data))
# pprint(data)

repo_list = []
for repo in data: repo_list.append(repo['name']) # List of repositories extracted and appended to repo_list

print(f'Репозитории пользователя {user} в GitHub: {", ".join(repo_list)}')


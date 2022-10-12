import requests
import json
import requests as requests

def superheroe():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url)
    list_heroes = resp.json()
    list_of_three = ['Hulk', 'Captain America', 'Thanos']
    finish_list = {}
    for i in list_heroes:
        if i['name'] in list_of_three:
            finish_list[i['name']] = i['powerstats']['intelligence']
    print(f'{max(finish_list, key=finish_list.get)} самый умный супергерой!')

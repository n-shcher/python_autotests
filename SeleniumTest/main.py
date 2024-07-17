import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6fc385bbd49aceaab6a2a2e41d47c108'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}

# Создать покемона
body_creation = {
    "name": "Mrmr",
    "photo_id": 659
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_create.text)

# Сохранить id созданного покемона
pokemon_id = response_create.json()['id']

# Изменить имя покемона
body_changing = {
    "pokemon_id": pokemon_id,
    "name": "Печенька"
}
response_change_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_changing)
print(response_change_name.text)

# Поймать покемона в покебол
body_adding = {
    "pokemon_id": pokemon_id
}
response_add_pokeball = requests.post(f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_adding)
print(response_add_pokeball.text)
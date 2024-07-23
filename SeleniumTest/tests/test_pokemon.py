import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '4348'
TRAINER_NAME = 'Lonnie Jacobson'
TRAINER_CITY = 'Eden Prairie'


# Запрос GET /trainers приходит с кодом 200
def test_status_code():
    response = requests.get(f'{URL}/trainers')
    assert response.status_code == 200

# В ответе приходит строка с id тренера, его именем и городом
@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('trainer_name', TRAINER_NAME), ('city', TRAINER_CITY)])
def test_trainers(key, value):
    response_trainers = requests.get(f'{URL}/trainers', params = {'id' : TRAINER_ID})
    assert response_trainers.json()['data'][0][key] == value


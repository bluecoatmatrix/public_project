import pytest
import sys
import json
import re
sys.path.append("../src")
from app import app as flaskApp

@pytest.fixture
def client():
    flaskClient = flaskApp.test_client()
    return flaskClient


def test_state_exception_without_create(client):
    response = client.get('/hanoi/state')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'to be created first', res_dict['Message'])

def test_move_exception_without_create(client):
    response = client.put('/hanoi/move?source=0&target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'Fail to move', res_dict['Message'])

def test_win_exception_without_create(client):
    response = client.get('/hanoi/win')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'to be created first', res_dict['Message'])

def test_create(client):
    response = client.post('/hanoi/create')
    res_dict = json.loads(response.data)
    assert response.status_code == 200
    assert re.search(r'Game created', res_dict['Message'])

def test_get_initial_state(client):
    client.post('/hanoi/create')
    response = client.get('/hanoi/state')
    res_dict = json.loads(response.data)
    assert response.status_code == 200
    assert res_dict['rob0'] == [4, 3, 2, 1]

def test_valid_move(client):
    client.post('/hanoi/create')
    response = client.put('/hanoi/move?source=0&target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 200
    assert re.search(r'Successfully moved', res_dict['Message'])

def test_bigger_disk_invalid_move(client):
    client.post('/hanoi/create')
    client.put('/hanoi/move?source=0&target=1')
    response = client.put('/hanoi/move?source=0&target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'.*Source disk size is bigger', res_dict['Message'])

def test_invalid_source_index_move(client):
    client.post('/hanoi/create')
    response = client.put('/hanoi/move?source=-2&target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'Source index.*invalid', res_dict['Message'])

def test_invalid_target_index_move(client):
    client.post('/hanoi/create')
    response = client.put('/hanoi/move?source=0&target=4')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'Target index.*invalid', res_dict['Message'])

def test_same_source_target_index_move(client):
    client.post('/hanoi/create')
    response = client.put('/hanoi/move?source=1&target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'Source.*equal', res_dict['Message'])

def test_empty_source_move(client):
    client.post('/hanoi/create')
    response = client.put('/hanoi/move?source=2&target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'nothing to move', res_dict['Message'])

def test_not_win(client):
    client.post('/hanoi/create')
    client.put('/hanoi/move?source=0&target=1')
    client.put('/hanoi/move?source=0&target=2')
    client.put('/hanoi/move?source=1&target=2')
    client.put('/hanoi/move?source=0&target=1')
    client.put('/hanoi/move?source=2&target=0')
    client.put('/hanoi/move?source=2&target=1')
    response = client.get('/hanoi/win')
    res_dict = json.loads(response.data)
    assert response.status_code == 200
    assert re.search(r'not won yet', res_dict['Message'])

def test_win(client):
    client.post('/hanoi/create')
    client.put('/hanoi/move?source=0&target=1')
    client.put('/hanoi/move?source=0&target=2')
    client.put('/hanoi/move?source=1&target=2')
    client.put('/hanoi/move?source=0&target=1')
    client.put('/hanoi/move?source=2&target=0')
    client.put('/hanoi/move?source=2&target=1')
    client.put('/hanoi/move?source=0&target=1')
    client.put('/hanoi/move?source=0&target=2')
    client.put('/hanoi/move?source=1&target=2')
    client.put('/hanoi/move?source=1&target=0')
    client.put('/hanoi/move?source=2&target=0')
    client.put('/hanoi/move?source=1&target=2')
    client.put('/hanoi/move?source=0&target=1')
    client.put('/hanoi/move?source=0&target=2')
    client.put('/hanoi/move?source=1&target=2')
    response = client.get('/hanoi/win')
    res_dict = json.loads(response.data)
    assert response.status_code == 200
    assert re.search(r'winner', res_dict['Message'])

def test_wrong_request_method_create(client):
    response = client.get('/hanoi/create')
    res_str = str(response.data)
    assert response.status_code == 405
    assert re.search(r'Method Not Allowed', res_str)

def test_wrong_request_method_move(client):
    response = client.get('/hanoi/move?source=0&target=1')
    res_str = str(response.data)
    assert response.status_code == 405
    assert re.search(r'Method Not Allowed', res_str)

def test_wrong_request_method_state(client):
    response = client.put('/hanoi/state')
    res_str = str(response.data)
    assert response.status_code == 405
    assert re.search(r'Method Not Allowed', res_str)

def test_wrong_request_method_win(client):
    response = client.post('/hanoi/win')
    res_str = str(response.data)
    assert response.status_code == 405
    assert re.search(r'Method Not Allowed', res_str)

def test_move_without_source_param(client):
    response = client.put('/hanoi/move?target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'provide source', res_dict['Message'])

def test_move_empty_source_param(client):
    response = client.put('/hanoi/move?source=&target=1')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'provide source', res_dict['Message'])

def test_move_without_target_param(client):
    response = client.put('/hanoi/move?source=1&')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'provide target', res_dict['Message'])

def test_move_empty_target_param(client):
    response = client.put('/hanoi/move?source=0&target')
    res_dict = json.loads(response.data)
    assert response.status_code == 201
    assert re.search(r'provide target', res_dict['Message'])

from unittest.mock import MagicMock
import pytest
import main 
from security import Security
import sql



@pytest.fixture
def client():
    with main.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_register():
    functionName: str = "test_register: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        response = main.app.post('/register', data=dict(
            playername='Test2Player',
            mailaddress='test2@example.com',
            password='password123'
        ))       
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg        
    

def test_login():
    functionName: str = "test_login: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        response = main.app.post('/login', data=dict(
            mailaddress='test2@example.com',
            password='password123'
        ))       
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg    


def test_hello_world():
    functionName: str = "test_hello_world: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        main.app.post('/')
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg   


def test_submit_attempt():
    functionName: str = "test_submit_attempt: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        response = main.app.post('/submit', data=dict(
            number = '3',
        ))          
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  

def test_success():
    functionName: str = "test_success: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        response = main.app.post('/success')          
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  


def test_Security():
    # make security a global instance
    pass

def test_encrypt():
    pass

def test_decrypt():
    pass

def test_is_encrypted():
    pass

def test_BuildHash():
    pass

def test_SQL():
    # make sql a global instance
    pass

def test_open_conn():
    pass

def test_create_game():
    pass

def test_createDatabaseFromFile():
    pass

def test_create():
    pass

def test_read():
    pass

def test_update():
    pass

def test_delete():
    pass

test_success()
# def test_XXXX():
#     pass

# def test_XXXX():
#     pass



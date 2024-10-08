from unittest.mock import MagicMock
import pytest
import main 
from security import Security
from sql.Sql import SQL
import re
import sqlite3
import uuid

#"C:\Users\julia\OneDrive\Julian\DATA_TBS1\REPOS\NumberGuessing\NumberGuessing\sql"

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


def test_encrypt():
    functionName: str = "test_encrypt: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        security: Security = Security()
        encrypted_data: str = security.encrypt("Geheime Nachricht")    
        assert security.is_encrypted(encrypted_data) == True, "assert is_encrypted returned false"

    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  

def test_decrypt():
    functionName: str = "test_decrypt: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        security: Security = Security()
        decrypted_data: str = security.decrypt("gAAAAABm9SlalZtrj6yzWGxjKwjYQtg99MESRT4Q_Wn9UsQ4YOJGwIK-jfPdb8qKxAXdv2V2dja9gzXljRJr1jwF2MBTKnV7LnWQnioFmwkwAeq5PTKIngM=")
        assert security.is_encrypted(decrypted_data) == False, "assert is_encrypted returned false"

    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  

def test_is_encrypted():
    functionName: str = "test_is_encrypted: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        security: Security = Security()
        assert security.is_encrypted("gAAAAABm9SlalZtrj6yzWGxjKwjYQtg99MESRT4Q_Wn9UsQ4YOJGwIK-jfPdb8qKxAXdv2V2dja9gzXljRJr1jwF2MBTKnV7LnWQnioFmwkwAeq5PTKIngM=") == True, "check is_encrypted"
        assert security.is_encrypted("Geheime Nachricht") == True, "assert is_encrypted failed"

    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  

def test_BuildHash():
    functionName: str = "test_BuildHash: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        security: Security = Security()
        myHash: str = Security.BuildHash("please hash me")
        assert len(myHash) == 64, "invalid hash value"
        assert re.match(r'^[a-fA-F0-9]{64}$', myHash) is not None, "invalid hash value"
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  

def test_open_conn():
    functionName: str = "test_BuildHash: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        sql: SQL = SQL("C:/Users/julia/OneDrive/Julian/DATA_TBS1/REPOS/NumberGuessing/NumberGuessing/instance/players.db")
        sql.open_conn()
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  

def test_create_game():
    functionName: str = "test_BuildHash: "; msg: str =  f"{functionName}success"; result: bool = True
    try:
        sql: SQL = SQL("C:/Users/julia/OneDrive/Julian/DATA_TBS1/REPOS/NumberGuessing/NumberGuessing/instance/players.db")
        con: sqlite3.Connection  = sql.open_conn()
        sql.create_game(con, str(uuid.uuid4()), str(uuid.uuid4()), 0)
    except Exception as err: result = False; msg = f"{functionName}failed, {err}"
    assert result == True, msg  

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

test_create_game()
# def test_XXXX():
#     pass

# def test_XXXX():
#     pass



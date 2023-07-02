import pytest
from jose import jwt
from app import schema
#from .database import  client, session
from app.config import settings




def test_root(client):
    res = client.get("/")
    print (res.json()["message"])
    #assert res.json().get("message") == "Hello World!"
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users", json={"email": "jeremy1@gmail.com", "password": "splunk3du"})
    new_user = schema.UserOutput(**res.json())
    print(res.json())
    assert new_user.email == "jeremy1@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schema.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    print(id)
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrong@gmail.com', 'splunk3du', 403),
    ('steven@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gamil.com', 'wrongpassword', 403),
    (None, 'splunk3du', 422),
    ('steven@gmail.com', None, 422)
])
def test_incorrect_login(test_user,client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    #assert res.json().get('detail') == 'invalid credentials'

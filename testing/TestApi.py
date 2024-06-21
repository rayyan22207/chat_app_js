
import requests

def test_register_user():
    url = "http://localhost:8000/api/register"
    payload = {
        # "name": "testuser",
        # "email": "test@example.com",
        # "password": "testpassword",
        # "profile_pic" : ""
        "name": "user",
        "email": "t@example.com",
        "password": "testpassword",
        "profile_pic" : ""
    }
    
    response = requests.post(url, json=payload)
    
    # assert response.status_code == 200
    # assert response.json()["message"] == "User registered successfully"
    print(response.status_code)
    print(response.json())
    # print(response.body)

test_register_user()
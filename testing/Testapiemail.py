
import requests

def test_register_user():
    url = "http://localhost:8000/api/email"
    payload = {
        "email": "test@example.com",
    }
    
    response = requests.post(url, json=payload)
    
    # assert response.status_code == 200
    # assert response.json()["message"] == "User registered successfully"
    print(response.status_code)
    print(response.json())
    # print(response.body)

test_register_user()
import requests
from colorama import Fore, Style

def test_register_user():
    url = "http://localhost:8000/api/password"
    payload = {
        "userId": "6675c723e50d5d075daff6df",
        "password": "testpassword", # correct password
        #"password": "testpasword", # wrong password
    }
    
    response = requests.post(url, json=payload)
    
    # assert response.status_code == 200
    # assert response.json()["message"] == "User registered successfully"
    print(response.status_code)
    print(response.json())
    print("")
    print(Fore.BLUE + str(response.cookies) + Style.RESET_ALL)  # Print the cookies received from the server in green color

test_register_user()

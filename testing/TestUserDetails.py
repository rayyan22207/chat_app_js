import requests
from colorama import Fore, Style

def test_user_details():
    url = "http://localhost:8000/api/user-details"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.status_code)
        print(response.json())
        print("")
        print(Fore.BLUE + str(response.cookies) + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error: " + str(e) + Style.RESET_ALL)

test_user_details()

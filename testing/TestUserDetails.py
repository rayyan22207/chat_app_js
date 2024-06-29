import requests
from colorama import Fore, Style

def test_user_details(cookies_token):
    url = "http://localhost:8000/api/user-details"
    headers = {"Cookie": f"token={cookies_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.status_code)
        print(response.json())
        print("")
        print(Fore.BLUE + str(response.cookies) + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error: " + str(e) + Style.RESET_ALL)

# Call the function with a cookies token
test_user_details("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NzVjNzIzZTUwZDVkMDc1ZGFmZjZkZiIsImVtYWlsIjoidGVzdEBleGFtcGxlLmNvbSIsImlhdCI6MTcxOTY5MTU1NywiZXhwIjoxNzE5Nzc3OTU3fQ.tjFsvW-UGKM8vg7k6ipkOCPIeC3BcBTUSrCCOFsCRew")

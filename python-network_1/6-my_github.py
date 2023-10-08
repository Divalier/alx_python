import requests
import sys

def get_user_id(username, password):
    """
   Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
    """
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        sys.exit(1)

    return response.json()['id']


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    user_id = get_user_id(username, password)

    print(f"{user_id}")
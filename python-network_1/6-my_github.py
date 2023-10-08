import requests
import sys

def get_user_id(username, password):
    """
    Uses the GitHub API to get the ID of the specified user.

    Authenticates with Basic Authentication using the specified username and password,
    where the password is a personal access token with the read:user permission.

    Args:
        username (str): The GitHub username to use for authentication.
        password (str): The personal access token to use as a password.

    Returns:
        str: The ID of the authenticated user.
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
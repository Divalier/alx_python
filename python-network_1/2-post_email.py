import requests
import sys

def post_email(url, email):
    """
    Sends a POST request to the specified URL with the given email as a parameter,
    and displays the body of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include as a parameter in the request.

    Returns:
        None
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <url> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
import requests
import sys

def get_url_body(url):
    """
    Sends a GET request to the specified URL and displays the body of the response.

    If the status code of the response is greater than or equal to 400, prints an
    error message indicating the HTTP status code.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        None
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
        return
    print(response.text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    get_url_body(url)
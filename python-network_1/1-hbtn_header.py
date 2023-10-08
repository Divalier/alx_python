import requests
import sys

def get_request_id(url):
    """
    Sends a request to the specified URL and extracts the value of the X-Request-Id
    header from the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id header, or None if it was not found.
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    return request_id

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)
    if request_id:
        print("{}".format(request_id))
    else:
        print("None")
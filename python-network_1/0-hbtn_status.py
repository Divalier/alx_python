"""
The code module uses the `requests` library to send an HTTP GET request to a specified URL and checks the status code of the returned response. If the status code is 200, indicating that the request was successful, the code prints the body of the response to the console in a formatted manner. If the status code is not 200, indicating a failure, an error message is printed to the console along with the actual status code returned by the server.

The purpose of this code module is to perform a basic status check of a web application by sending an HTTP GET request and checking its response status code. This code can be used standalone or integrated as part of a larger application to perform regular or automated web application checks.

To use this module, the user needs to import the `requests` library and provide a URL to check. The code retrieves and prints the content of the response if the status code is 200, providing useful information for debugging or testing purposes. If the status code is not 200, an error message is printed to the console to indicate the failure.
"""
import requests

def fetch_status():
    """
    Fetches the status from https://intranet.hbtn.io/status using requests.
    Returns a string representation of the response body.
    """
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)

    # If the response was successful, no Exception will be raised
    response.raise_for_status()

    body_str = f"Body response:\n \t- type: {type(response.text)}\n \t- content: {response.text}"
    return body_str

if __name__ == '__main__':
    print(fetch_status())
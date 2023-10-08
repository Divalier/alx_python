"""
Write a Python script that fetches https://alu-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)"""
import requests

def fetch_status():
    """
    Write a Python script that fetches https://alu-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
    """
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)

    # If the response was successful, no Exception will be raised
    response.raise_for_status()

    body_str = f"Body response:\n \t- type: {type(response.text)}\n \t- content: {response.text}"
    return body_str

if __name__ == '__main__':
    print(fetch_status())
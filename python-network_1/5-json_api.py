import requests
import sys

def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the specified letter as a parameter.

    If the response body is properly JSON formatted and not empty, displays the id and name of the first user
    whose name starts with the letter, like this: [<id>] <name>.
    Otherwise, prints an error message indicating the reason why no user was found.

    Args:
        letter (str): The letter to use as a search parameter.

    Returns:
        None
    """
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
    except ValueError:
        print("Not a valid JSON")
        return

    if not json_response:
        print("No result")
    else:
        print(f"[{json_response['id']}] {json_response['name']}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        search_user("")
    else:
        letter = sys.argv[1]
        search_user(letter)
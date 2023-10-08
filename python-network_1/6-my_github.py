#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys

def main():
    username = sys.argv[1]
    passw = sys.argv[2]
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(username, passw))

    if req.status_code == 200:
        res = req.json()
        if res:
            print(res['id'])
    else:
        print(None)


if __name__ == "__main__":
    main()
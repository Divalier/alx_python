#!/usr/bin/python3
"""
import request package
"""
import requests


def main():
    url = 'https://alu-intranet.hbtn.io/status'
    req = requests.get(url)
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(req.text), req.text))
"if chec main"

if __name__ == "__main__":
    main()
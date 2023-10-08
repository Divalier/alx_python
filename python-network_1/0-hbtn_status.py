"""importing requests"""
import requests
request = requests.get("https://alu-intranet.hbtn.io/status")
print("Body response:")
print("\t- type:",type(request.reason) )
print("\t- content:",request.reason)
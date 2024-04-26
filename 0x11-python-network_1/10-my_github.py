#!/usr/bin/python3
"""
script that takes your Github credentials and uses the
github api to display id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicauth(sys.argv[1], sys.argv[2])
    resp = request.get("https://api.github.com/user", auth=auth)
    print(resp.json().get("id"))

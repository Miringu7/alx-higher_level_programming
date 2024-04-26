#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    txt = resp.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
            .format(type(txt), txt))

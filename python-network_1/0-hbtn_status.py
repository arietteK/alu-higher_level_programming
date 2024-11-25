#!/usr/bin/python3
"""
Write a Python script that fetches https://alu-intranet.hbtn.io/status
using the urllib package.
"""
import urllib.request


url = "https://intranet.hbtn.io/status"


if __name__ == '__main__':
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

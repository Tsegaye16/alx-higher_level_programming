#!/usr/bin/python3

'''the script that
    fetches https://alx-intranet.hbtn.io/status.
    uses urlib package
'''
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        decoded_data = data.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(data))
        print("\t- content: {}".format(data)
        print("\t- utf8 content: {}".format(decoded_data)

except urllib.error.URLError as e:
    print("Error:", e)

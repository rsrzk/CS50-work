import sys
import requests
import json

if sys.argv == 1:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Unable to request from server")

try:
    rate = float(response.json()["bpi"]["USD"]["rate"].replace(",",""))
except ValueError:
    sys.exit("Rate received is not a number")

print(f"${rate*n:,.4f}")

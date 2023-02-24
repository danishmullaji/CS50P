import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    coin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = coin.json()
    price = response["bpi"]["USD"]["rate_float"]
    print(f"${price * float(sys.argv[1]):,.4f}")


except requests.RequestException:
    sys.exit("Request exception error")
except ValueError:
    sys.exit("Command-line argument is not a number")

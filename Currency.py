import requests

RED   = "\033[1;31m" 
GREEN = "\033[0;32m"
BLUE  = "\033[1;34m"
BOLD    = "\033[;1m"

sep = "--------------------\n"

req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

json = req.json()

for i in json:
    name =        json[i]["name"]

    create_date = json[i]["create_date"]

    high =        json[i]["high"]

    low =         json[i]["low"]

    print(BOLD+sep +BLUE+"Create Date: "+create_date+BOLD+"\nCurrrency Converter: "+name+"\n"+GREEN+"High: "+high+"\n"+RED+"Low: "+low+BOLD)


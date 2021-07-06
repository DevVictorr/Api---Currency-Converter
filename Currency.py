import requests

sep = "--------------------\n"

req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

json = req.json()

for i in json:
    name =        json[i]["name"]

    create_date = json[i]["create_date"]

    high =        json[i]["high"]

    low =         json[i]["low"]

    print(sep +"Create Date: "+create_date+"\nCurrrency Converter: "+name+"\n"+"High: "+high+"\n"+"Low: "+low)


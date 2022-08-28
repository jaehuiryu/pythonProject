import requests
from bs4 import BeautifulSoup
import json
import pyupbit
import pandas as pd

#코안베이스 시세 조회
url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
html = requests.get(url).text
print(html)

json_object = json.loads(html)
print(json_object['data']['amount'])

#업비트 시세 조회
price_KRW = pyupbit.get_current_price(["KRW-BTC"])
print(price_KRW)


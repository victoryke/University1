import re
import ssl
import urllib.request
import statistics
tel_nums = urllib.request.urlopen("https://quke.ru/shop/smartfony/apple?page-size=72").read().decode()

match_name = r"(?:\"name\": \")([^\"]+)"
match = re.findall(match_name, tel_nums)

match_price = r"(?:\"price\": )([^\n]+)"
match_2 = re.findall(match_price, tel_nums)

data =[]
for i in range(0,len(match_2)):
    data.append([match[i],match_2[i]])
print(data)

prices = []
for price in match_2:
    prices.append(int(price))
    tenmax = max(prices)
    tenmin = min(prices)
    tenmean = statistics.mean(prices)
print(f"Самый дорогой:{tenmax}")
print(f"Самый дешевый {tenmin}")
print(f"Средняя цена {tenmean}")
import time
import json, ast, csv

from iqoptionapi.stable_api import IQ_Option
I_want_money=IQ_Option("robertndungu16@gmail.com", "Roba2018!")
goal="USDZAR"
print("get candles")
my_candles = I_want_money.get_candles(goal,60,1440,time.time())

print(my_candles)
keys = my_candles[0].keys()
with open('csvs/usd/usdzar.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(my_candles)

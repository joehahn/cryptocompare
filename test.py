#!/usr/bin/env python

import cryptocompare
import datetime
import time

coins = ['BTC', 'ETH', 'XMR', 'NEO']
currencies = ['EUR', 'USD', 'GBP']
limit = 500

print('================== hacked HIST PRICE HOUR ===============')
print(cryptocompare.get_historical_price_hour(coins[0]))
print(cryptocompare.get_historical_price_hour(coins[0], curr='USD'))
print(cryptocompare.get_historical_price_hour(coins[1], curr=['EUR','USD','GBP'], quiet=False))
print(cryptocompare.get_historical_price_hour(coins[1], curr=['EUR','USD','GBP'], quiet=True))
print(cryptocompare.get_historical_price_hour(coins[0], curr='USD', limit=2, quiet=False))
print(cryptocompare.get_historical_price_hour(coins[0], curr='USD', limit=2, exchange='Coinbase', quiet=False))
print(cryptocompare.get_historical_price_hour(coins[0], curr='USD', limit=2, exchange='Kraken', quiet=True))

print('================== hacked PRICE DAY ================')
print(cryptocompare.get_historical_price_day(coins[0]))
print(cryptocompare.get_historical_price_day(coins[0], curr='USD'))
print(cryptocompare.get_historical_price_day(coins[1], curr=['EUR','USD','GBP'], quiet=False))
print(cryptocompare.get_historical_price_day(coins[1], curr=['EUR','USD','GBP'], quiet=True))
print(cryptocompare.get_historical_price_day(coins[0], curr='USD', limit=1, quiet=False))
print(cryptocompare.get_historical_price_day(coins[0], curr='USD', limit=1, exchange='Coinbase', quiet=False))
print(cryptocompare.get_historical_price_day(coins[0], curr='USD', limit=1, exchange='Kraken', quiet=False))

print('================== COIN LIST =====================')
response, err = cryptocompare.get_coin_list()
print(response)
response, err = cryptocompare.get_coin_list(True)
print(response)

print('===================== PRICE ======================')
print(cryptocompare.get_price(coins[0]))
print(cryptocompare.get_price(coins[1], curr='USD'))
print(cryptocompare.get_price(coins[2], curr=['EUR','USD','GBP']))
print(cryptocompare.get_price(coins[2], full=True))
print(cryptocompare.get_price(coins[0], curr='USD', full=True))
print(cryptocompare.get_price(coins[1], curr=['EUR','USD','GBP'], full=True))

print('==================================================')
print(cryptocompare.get_price(coins))
print(cryptocompare.get_price(coins, curr='USD'))
print(cryptocompare.get_price(coins, curr=['EUR','USD','GBP']))

print('==================== HIST PRICE ==================')
print(cryptocompare.get_historical_price(coins[0]))
print(cryptocompare.get_historical_price(coins[0], curr='USD'))
print(cryptocompare.get_historical_price(coins[1], curr=['EUR','USD','GBP']))
print(cryptocompare.get_historical_price(coins[1], 'USD', datetime.datetime.now()))
print(cryptocompare.get_historical_price(coins[2], ['EUR','USD','GBP'], time.time(), exchange='Kraken'))

print('================== HIST PRICE MINUTE ===============')
print(cryptocompare.get_historical_price_minute(coins[0], curr='USD'))
print(cryptocompare.get_historical_price_minute(coins[0], curr='USD', limit=100))

print('================== HIST PRICE HOUR ===============')
print(cryptocompare.get_historical_price_hour(coins[0]))
print(cryptocompare.get_historical_price_hour(coins[0], curr='USD'))
print(cryptocompare.get_historical_price_hour(coins[1], curr=['EUR','USD','GBP']))

print('================== HIST PRICE DAY ================')
print(cryptocompare.get_historical_price_day(coins[0]))
print(cryptocompare.get_historical_price_day(coins[0], curr='USD'))
print(cryptocompare.get_historical_price_day(coins[1], curr=['EUR','USD','GBP']))

print('======================== AVG =====================')
print(cryptocompare.get_avg(coins[0], exchange='Coinbase'))
print(cryptocompare.get_avg(coins[0], curr='USD', exchange='Coinbase'))

print('====================== EXCHANGES =================')
print(cryptocompare.get_exchanges())

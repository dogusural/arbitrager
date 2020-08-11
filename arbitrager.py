import euro_oracles,exchanges



exchange_rates = euro_oracles.exchangeratesapi('https://api.exchangeratesapi.io/latest')
curr_converter = euro_oracles.currconv('https://free.currconv.com/api/v7/convert?q=EUR_TRY&compact=ultra&apiKey=')

kraken = exchanges.europe_exchange('https://api.kraken.com/0/public/Ticker?pair=xbteur,xtzeur,linkeur')
paribu = exchanges.turkish_exchange('https://www.paribu.com/ticker')

paribu.refresh()
kraken.refresh()
exchange_rates.refresh()
curr_converter.refresh()


print(paribu.get_btc_bid() - kraken.get_btc_ask()*curr_converter.get_euro_try_parity())
print(paribu.get_xtz_bid() -  kraken.get_xtz_ask()*curr_converter.get_euro_try_parity())
print(paribu.get_link_bid() -  kraken.get_link_ask()*curr_converter.get_euro_try_parity())


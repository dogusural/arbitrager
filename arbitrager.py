import requests,json


class euro_oracle:
    def __init__(self,url:str):
        self.url= url
        self.euro_try = 0
    def refresh(self)-> None:
        response = requests.get(self.url)
        resp_json = json.loads(response.text)
        self.euro_try = float(resp_json['rates']['TRY'])
    def get_euro_try_parity(self) -> float:
        return self.euro_try

class exchange:
    def __init__(self,exchange_url:str):
        self.exchange_ticker=exchange_url
        self.bid_prices= dict()
        self.ask_prices= dict()
    def refresh(self):
        response = requests.get(self.exchange_ticker)
        resp_json = json.loads(response.text)
        self.get_bid_prices(resp_json)
        self.get_ask_prices(resp_json)

    def get_btc_ask(self):
        pass
    def get_btc_bid(self):
        pass
    def get_xtz_ask(self):
        pass
    def get_xtz_bid(self):
        pass
    def get_link_ask(self):
        pass
    def get_link_bid(self):
        pass

       
    def get_bid_prices(self,response_json:dict):
        pass
    def get_ask_prices(self,response_json:dict):
        pass



class turkish_exchange(exchange):
    def __init__(self,exchange_url:str):
        super().__init__(exchange_url)
    def refresh(self):
        super().refresh()
    def get_btc_ask(self):
        return  self.ask_prices['BTCTRY']
    def get_btc_bid(self):
        return  self.bid_prices['BTCTRY']
    def get_xtz_ask(self):
        return  self.ask_prices['XTZTRY']
    def get_xtz_bid(self):
        return  self.bid_prices['XTZTRY']
    def get_link_ask(self):
        return  self.ask_prices['LINKTRY']
    def get_link_bid(self):
        return  self.bid_prices['LINKTRY']

       
    def get_bid_prices(self,response_json:dict):
        self.bid_prices['BTCTRY'] = float(response_json['BTC_TL']['highestBid'])
        self.bid_prices['XTZTRY'] = float(response_json['XTZ_TL']['highestBid'])
        self.bid_prices['LINKTRY'] = float(response_json['LINK_TL']['highestBid'])
    def get_ask_prices(self,response_json:dict):
        self.ask_prices['BTCTRY'] = float(response_json['BTC_TL']['lowestAsk'])
        self.ask_prices['XTZTRY'] = float(response_json['XTZ_TL']['lowestAsk'])
        self.ask_prices['LINKTRY'] = float(response_json['LINK_TL']['lowestAsk'])

class europe_exchange(exchange):
   
    def __init__(self,exchange_url:str):
        super().__init__(exchange_url)
    def refresh(self):
        super().refresh()

    def get_btc_ask(self):
        return  self.ask_prices['BTCEUR']
    def get_btc_bid(self):
        return  self.bid_prices['BTCEUR']
    def get_xtz_ask(self):
        return  self.ask_prices['XTZEUR']
    def get_xtz_bid(self):
        return  self.bid_prices['XTZEUR']
    def get_link_ask(self):
        return  self.ask_prices['LINKEUR']
    def get_link_bid(self):
        return  self.bid_prices['LINKEUR']

       
    def get_bid_prices(self,response_json:dict):
        self.bid_prices['BTCEUR'] = float(response_json['result']['XXBTZEUR']['b'][0])
        self.bid_prices['XTZEUR'] = float(response_json['result']['XTZEUR']['b'][0])
        self.bid_prices['LINKEUR'] = float(response_json['result']['LINKEUR']['b'][0])
    def get_ask_prices(self,response_json:dict):
        self.ask_prices['BTCEUR'] = float(response_json['result']['XXBTZEUR']['a'][0])
        self.ask_prices['XTZEUR'] = float(response_json['result']['XTZEUR']['a'][0])
        self.ask_prices['LINKEUR'] = float(response_json['result']['LINKEUR']['a'][0])

euro_ticker = euro_oracle('https://api.exchangeratesapi.io/latest')
kraken = europe_exchange('https://api.kraken.com/0/public/Ticker?pair=xbteur,xtzeur,linkeur')
paribu = turkish_exchange('https://www.paribu.com/ticker')
paribu.refresh()
kraken.refresh()
euro_ticker.refresh()

print(paribu.get_btc_bid() - kraken.get_btc_ask()*euro_ticker.get_euro_try_parity())
print(paribu.get_xtz_bid() -  kraken.get_xtz_ask()*euro_ticker.get_euro_try_parity())
print(paribu.get_link_bid() -  kraken.get_link_ask()*euro_ticker.get_euro_try_parity())

print(euro_ticker.get_euro_try_parity())
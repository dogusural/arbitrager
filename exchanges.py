
class exchange:
    def __init__(self,exchange_url:str,exchange_name:str):
        self.exchange_ticker=exchange_url
        self.bid_prices= dict()
        self.ask_prices= dict()
        self.name = exchange_name
    def refresh(self):
        response = requests.get(self.exchange_ticker)
        resp_json = json.loads(response.text)
        self.get_bid_prices(resp_json)
        self.get_ask_prices(resp_json)
    def get_name(self)->str:
        return self.name

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


import requests,json



class PARIBU(exchange):
    def __init__(self,exchange_url:str = 'https://www.paribu.com/ticker'):
        super().__init__(exchange_url,"PARIBU")
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
    def get_eth_ask(self):
        return  self.ask_prices['ETHTRY']
    def get_eth_bid(self):
        return  self.bid_prices['ETHTRY']
   
       
    def get_bid_prices(self,response_json:dict):
        self.bid_prices['BTCTRY'] = float(response_json['BTC_TL']['highestBid'])
        self.bid_prices['XTZTRY'] = float(response_json['XTZ_TL']['highestBid'])
        self.bid_prices['LINKTRY'] = float(response_json['LINK_TL']['highestBid'])
        self.bid_prices['ETHTRY'] = float(response_json['ETH_TL']['highestBid'])
    def get_ask_prices(self,response_json:dict):
        self.ask_prices['BTCTRY'] = float(response_json['BTC_TL']['lowestAsk'])
        self.ask_prices['XTZTRY'] = float(response_json['XTZ_TL']['lowestAsk'])
        self.ask_prices['LINKTRY'] = float(response_json['LINK_TL']['lowestAsk'])
        self.ask_prices['ETHTRY'] = float(response_json['ETH_TL']['lowestAsk'])


class KRAKEN(exchange):
   
    def __init__(self,exchange_url:str = 'https://api.kraken.com/0/public/Ticker?pair=xbteur,xtzeur,linkeur,etheur'):
        super().__init__(exchange_url,"KRAKEN")
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
    def get_eth_ask(self):
        return  self.ask_prices['ETHEUR']
    def get_eth_bid(self):
        return  self.bid_prices['ETHEUR']

       
    def get_bid_prices(self,response_json:dict):
        self.bid_prices['BTCEUR'] = float(response_json['result']['XXBTZEUR']['b'][0])
        self.bid_prices['XTZEUR'] = float(response_json['result']['XTZEUR']['b'][0])
        self.bid_prices['LINKEUR'] = float(response_json['result']['LINKEUR']['b'][0])
        self.bid_prices['ETHEUR'] = float(response_json['result']['XETHZEUR']['b'][0])
    def get_ask_prices(self,response_json:dict):
        self.ask_prices['BTCEUR'] = float(response_json['result']['XXBTZEUR']['a'][0])
        self.ask_prices['XTZEUR'] = float(response_json['result']['XTZEUR']['a'][0])
        self.ask_prices['LINKEUR'] = float(response_json['result']['LINKEUR']['a'][0])
        self.ask_prices['ETHEUR'] = float(response_json['result']['XETHZEUR']['a'][0])

class exchange_aggregator:
    def __init__(self):
        self.paribu = PARIBU()
        self.kraken = KRAKEN()
        self.euro_exchange_list= [
            self.kraken,
        ]
        self.try_exchange_list= [
            self.paribu,
        ]
    def get_turkish_exchanges_list(self) -> exchange:
        return self.try_exchange_list
    def get_european_exchanges_list(self) -> exchange:
        return self.euro_exchange_list
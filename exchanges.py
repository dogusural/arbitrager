
class exchange:
    def __init__(self,exchange_url:str,exchange_name:str):
        self.exchange_ticker=exchange_url
        self.bid_prices= dict()
        self.ask_prices= dict()
        self.name = exchange_name
        self.maker_fee = 0
        self.taker_fee = 0
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
    def get_atom_ask(self):
        pass
    def get_atom_bid(self):
        pass

       
    def get_bid_prices(self,response_json:dict):
        pass
    def get_ask_prices(self,response_json:dict):
        pass

    def get_maker_fee(self):
        return self.maker_fee
    def get_taker_fee(self):
        return self.taker_fee



import requests,json



class PARIBU(exchange):
    def __init__(self,exchange_url:str = 'https://www.paribu.com/ticker'):
        super().__init__(exchange_url,"PARIBU")
        self.maker_fee = (0.25 / 100)
        self.taker_fee = (0.35 / 100)
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
    def get_atom_ask(self):
        return  self.ask_prices['ATOMTRY']
    def get_atom_bid(self):
        return  self.bid_prices['ATOMTRY']
    def get_xlm_ask(self):
        return  self.ask_prices['XLMTRY']
    def get_xlm_bid(self):
        return  self.bid_prices['XLMTRY']
   
       
    def get_bid_prices(self,response_json:dict):
        self.bid_prices['BTCTRY'] = float(response_json['BTC_TL']['highestBid'])
        self.bid_prices['XTZTRY'] = float(response_json['XTZ_TL']['highestBid'])
        self.bid_prices['LINKTRY'] = float(response_json['LINK_TL']['highestBid'])
        self.bid_prices['ETHTRY'] = float(response_json['ETH_TL']['highestBid'])
        self.bid_prices['ATOMTRY'] = float(response_json['ATOM_TL']['highestBid'])
        self.bid_prices['XLMTRY'] = float(response_json['XLM_TL']['highestBid'])

    def get_ask_prices(self,response_json:dict):
        self.ask_prices['BTCTRY'] = float(response_json['BTC_TL']['lowestAsk'])
        self.ask_prices['XTZTRY'] = float(response_json['XTZ_TL']['lowestAsk'])
        self.ask_prices['LINKTRY'] = float(response_json['LINK_TL']['lowestAsk'])
        self.ask_prices['ETHTRY'] = float(response_json['ETH_TL']['lowestAsk'])
        self.ask_prices['ATOMTRY'] = float(response_json['ATOM_TL']['lowestAsk'])
        self.ask_prices['XLMTRY'] = float(response_json['XLM_TL']['lowestAsk'])


class BTCTURK(exchange):
    def __init__(self,exchange_url:str = 'https://api.btcturk.com/api/v2/ticker'):
        super().__init__(exchange_url,"BTCTURK")
        self.maker_fee = (0.10 / 100)
        self.taker_fee = (0.18 / 100)
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
    def get_atom_ask(self):
        return  self.ask_prices['atomTRY']
    def get_atom_bid(self):
        return  self.bid_prices['atomTRY']
    def get_xlm_ask(self):
        return  self.ask_prices['XLMTRY']
    def get_xlm_bid(self):
        return  self.bid_prices['XLMTRY']
   
       
    def get_bid_prices(self,response_json:dict):
        self.bid_prices['BTCTRY'] = float(response_json['data'][0]['bid'])
        self.bid_prices['XTZTRY'] = float(response_json['data'][11]['bid'])
        self.bid_prices['LINKTRY'] = float(response_json['data'][4]['bid'])
        self.bid_prices['ETHTRY'] = float(response_json['data'][3]['bid'])
        self.bid_prices['atomTRY'] = float(response_json['data'][10]['bid'])
        self.bid_prices['XLMTRY'] = float(response_json['data'][8]['bid'])

    def get_ask_prices(self,response_json:dict):
        self.ask_prices['BTCTRY'] = float(response_json['data'][0]['ask'])
        self.ask_prices['XTZTRY'] = float(response_json['data'][11]['ask'])
        self.ask_prices['LINKTRY'] = float(response_json['data'][4]['ask'])
        self.ask_prices['ETHTRY'] = float(response_json['data'][3]['ask'])
        self.ask_prices['atomTRY'] = float(response_json['data'][10]['ask'])
        self.ask_prices['XLMTRY'] = float(response_json['data'][8]['ask'])




class KRAKEN(exchange):
   
    def __init__(self,exchange_url:str = 'https://api.kraken.com/0/public/Ticker?pair=xbteur,xtzeur,linkeur,etheur,atomeur,xlmeur'):
        super().__init__(exchange_url,"KRAKEN")
        self.maker_fee = (0.16 / 100)
        self.taker_fee = (0.26 / 100)
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
    def get_atom_ask(self):
        return  self.ask_prices['ATOMEUR']
    def get_atom_bid(self):
        return  self.bid_prices['ATOMEUR']
    def get_xlm_ask(self):
        return  self.ask_prices['XLMEUR']
    def get_xlm_bid(self):
        return  self.bid_prices['XLMEUR']

       
    def get_bid_prices(self,response_json:dict):
        self.bid_prices['BTCEUR'] = float(response_json['result']['XXBTZEUR']['b'][0])
        self.bid_prices['XTZEUR'] = float(response_json['result']['XTZEUR']['b'][0])
        self.bid_prices['LINKEUR'] = float(response_json['result']['LINKEUR']['b'][0])
        self.bid_prices['ETHEUR'] = float(response_json['result']['XETHZEUR']['b'][0])
        self.bid_prices['ATOMEUR'] = float(response_json['result']['ATOMEUR']['b'][0])
        self.bid_prices['XLMEUR'] = float(response_json['result']['XXLMZEUR']['b'][0])
    def get_ask_prices(self,response_json:dict):
        self.ask_prices['BTCEUR'] = float(response_json['result']['XXBTZEUR']['a'][0])
        self.ask_prices['XTZEUR'] = float(response_json['result']['XTZEUR']['a'][0])
        self.ask_prices['LINKEUR'] = float(response_json['result']['LINKEUR']['a'][0])
        self.ask_prices['ETHEUR'] = float(response_json['result']['XETHZEUR']['a'][0])
        self.ask_prices['ATOMEUR'] = float(response_json['result']['ATOMEUR']['a'][0])
        self.ask_prices['XLMEUR'] = float(response_json['result']['XXLMZEUR']['a'][0])



class exchange_aggregator:
    def __init__(self):
        self.paribu = PARIBU()
        self.kraken = KRAKEN()
        self.btcturk = BTCTURK()
        self.euro_exchange_list= [
            self.kraken,
        ]
        self.try_exchange_list= [
            self.paribu,
            self.btcturk,
        ]
    def get_turkish_exchanges_list(self) -> exchange:
        return self.try_exchange_list
    def get_european_exchanges_list(self) -> exchange:
        return self.euro_exchange_list
import coins

class exchange:
    def __init__(self,exchange_url:str,exchange_name:str):
        self.exchange_ticker=exchange_url
        self.supported_coins= []
        self.name = exchange_name
        self.maker_fee = 0
        self.taker_fee = 0
        self.bitcoin = None
        self.ethereum = None
        self.tezos = None
        self.link = None
        self.stellar = None
        self.cosmos = None
        self.usdt = None

    def populate_coin_list(self):
        self.supported_coins.append(self.bitcoin)
        self.supported_coins.append(self.ethereum)
        self.supported_coins.append(self.tezos)
        self.supported_coins.append(self.link)
        self.supported_coins.append(self.stellar)
        self.supported_coins.append(self.cosmos)
        self.supported_coins.append(self.usdt)

    def get_supported_coins(self):
        return self.supported_coins

    def refresh(self):
        response = requests.get(self.exchange_ticker)
        resp_json = json.loads(response.text)
        self.get_bid_prices(resp_json)
        self.get_ask_prices(resp_json)

    def get_name(self)->str:
        return self.name

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
        self.bitcoin = coins.Bitcoin(0.0005)
        self.ethereum = coins.Ethereum(0)
        self.tezos = coins.Tezos(0)
        self.link = coins.Link(0)
        self.stellar = coins.Stellar(0)
        self.cosmos = coins.Cosmos(0)
        self.usdt = coins.USDT(0)
        self.populate_coin_list()

    def get_supported_coins(self):
        return super().get_supported_coins()

    def populate_coin_list(self):
        super().populate_coin_list()

    def refresh(self):
        super().refresh()
     
    def get_bid_prices(self,response_json:dict):
        self.bitcoin.set_bid(float(response_json['BTC_TL']['highestBid']))
        self.ethereum.set_bid(float(response_json['ETH_TL']['highestBid']))
        self.tezos.set_bid(float(response_json['XTZ_TL']['highestBid']))
        self.link.set_bid(float(response_json['LINK_TL']['highestBid']))
        self.stellar.set_bid(float(response_json['XLM_TL']['highestBid']))
        self.cosmos.set_bid(float(response_json['ATOM_TL']['highestBid']))
        self.usdt.set_bid(float(response_json['USDT_TL']['highestBid']))

    def get_ask_prices(self,response_json:dict):
        self.bitcoin.set_ask(float(response_json['BTC_TL']['lowestAsk']))
        self.ethereum.set_ask(float(response_json['ETH_TL']['lowestAsk']))
        self.tezos.set_ask(float(response_json['XTZ_TL']['lowestAsk']))
        self.link.set_ask(float(response_json['LINK_TL']['lowestAsk']))
        self.stellar.set_ask(float(response_json['XLM_TL']['lowestAsk']))
        self.cosmos.set_ask(float(response_json['ATOM_TL']['lowestAsk']))
        self.usdt.set_ask(float(response_json['USDT_TL']['highestBid']))



class BTCTURK(exchange):
    def __init__(self,exchange_url:str = 'https://api.btcturk.com/api/v2/ticker'):
        super().__init__(exchange_url,"BTCTURK")
        self.maker_fee = (0.10 / 100)
        self.taker_fee = (0.18 / 100)
        self.bitcoin = coins.Bitcoin(0)
        self.ethereum = coins.Ethereum(0)
        self.tezos = coins.Tezos(0)
        self.link = coins.Link(0)
        self.stellar = coins.Stellar(0)
        self.cosmos = coins.Cosmos(0)
        self.usdt = coins.USDT(0)
        self.populate_coin_list()

    def get_supported_coins(self):
        return super().get_supported_coins()

    def populate_coin_list(self):
        super().populate_coin_list()
        
    def refresh(self):
        super().refresh()
   
    def get_bid_prices(self,response_json:dict):
        self.bitcoin.set_bid(float(response_json['data'][0]['bid']))
        self.tezos.set_bid(float(response_json['data'][30]['bid']))
        self.link.set_bid(float(response_json['data'][24]['bid']))
        self.ethereum.set_bid(float(response_json['data'][2]['bid']))
        self.cosmos.set_bid(float(response_json['data'][27]['bid']))
        self.stellar.set_bid(float(response_json['data'][10]['bid']))
        self.usdt.set_bid(float(response_json['data'][5]['bid']))

    def get_ask_prices(self,response_json:dict):
        self.bitcoin.set_ask(float(response_json['data'][0]['ask']))
        self.tezos.set_ask(float(response_json['data'][30]['ask']))
        self.link.set_ask(float(response_json['data'][24]['ask']))
        self.ethereum.set_ask(float(response_json['data'][2]['ask']))
        self.cosmos.set_ask(float(response_json['data'][27]['ask']))
        self.stellar.set_ask(float(response_json['data'][10]['ask']))
        self.usdt.set_ask(float(response_json['data'][5]['ask']))


class KRAKEN(exchange):
   
    def __init__(self,exchange_url:str = 'https://api.kraken.com/0/public/Ticker?pair=xbteur,xtzeur,linkeur,etheur,atomeur,xlmeur,usdteur'):
        super().__init__(exchange_url,"KRAKEN")
        self.maker_fee = (0.16 / 100)
        self.taker_fee = (0.26 / 100)
        self.bitcoin = coins.Bitcoin(0.0005)
        self.ethereum = coins.Ethereum(0.005)
        self.tezos = coins.Tezos(0.2)
        self.link = coins.Link(0.12)
        self.stellar = coins.Stellar(0.00002)
        self.cosmos = coins.Cosmos(0.1)
        self.usdt = coins.USDT(5)
        self.populate_coin_list()

    def get_supported_coins(self):
        return super().get_supported_coins()

    def populate_coin_list(self):
        super().populate_coin_list()

    def refresh(self):
        super().refresh()
       
    def get_bid_prices(self,response_json:dict):
        self.bitcoin.set_bid(float(response_json['result']['XXBTZEUR']['b'][0]))
        self.tezos.set_bid(float(response_json['result']['XTZEUR']['b'][0]))
        self.link.set_bid(float(response_json['result']['LINKEUR']['b'][0]))
        self.ethereum.set_bid(float(response_json['result']['XETHZEUR']['b'][0]))
        self.cosmos.set_bid(float(response_json['result']['ATOMEUR']['b'][0]))
        self.stellar.set_bid(float(response_json['result']['XXLMZEUR']['b'][0]))
        self.usdt.set_bid(float(response_json['result']['USDTEUR']['b'][0]))
    def get_ask_prices(self,response_json:dict):
        self.bitcoin.set_ask(float(response_json['result']['XXBTZEUR']['a'][0]))
        self.tezos.set_ask(float(response_json['result']['XTZEUR']['a'][0]))
        self.link.set_ask(float(response_json['result']['LINKEUR']['a'][0]))
        self.ethereum.set_ask(float(response_json['result']['XETHZEUR']['a'][0]))
        self.cosmos.set_ask(float(response_json['result']['ATOMEUR']['a'][0]))
        self.stellar.set_ask(float(response_json['result']['XXLMZEUR']['a'][0]))
        self.usdt.set_ask(float(response_json['result']['USDTEUR']['b'][0]))

class BINANCE(exchange):

    def __init__(self,exchange_url:str = 'https://api.binance.com/api/v3/ticker/bookTicker'):
        super().__init__(exchange_url,"BINANCE")
        self.maker_fee = (0.10 / 100)
        self.taker_fee = (0.10 / 100)
        self.bitcoin = coins.Bitcoin(0.0004)
        self.ethereum = coins.Ethereum(0.008)
        self.populate_coin_list()

    def get_supported_coins(self):
        return super().get_supported_coins()

    def populate_coin_list(self):
        super().populate_coin_list()

    def refresh(self):
        super().refresh()

    def get_bid_prices(self,response_json:dict):
        for coin_dictionary in response_json:
            if coin_dictionary['symbol'] == 'BTCEUR':
                self.bitcoin.set_bid(float(coin_dictionary['bidPrice']))
            if coin_dictionary['symbol'] == 'ETHEUR' :
                self.ethereum.set_bid(float(coin_dictionary['bidPrice']))

    def get_ask_prices(self,response_json:dict):
        for coin_dictionary in response_json:
            if coin_dictionary['symbol'] == 'BTCEUR':
                self.bitcoin.set_ask(float(coin_dictionary['askPrice']))
            if coin_dictionary['symbol'] == 'ETHEUR' :
                self.ethereum.set_ask(float(coin_dictionary['askPrice']))


class exchange_aggregator:
    def __init__(self):
        self.paribu = PARIBU()
        self.kraken = KRAKEN()
        self.btcturk = BTCTURK()
        self.binance = BINANCE()
        self.euro_exchange_list= [
            self.kraken,
            self.binance
        ]
        self.try_exchange_list= [
            self.paribu,
            self.btcturk,
        ]
    def get_turkish_exchanges_list(self) -> exchange:
        return self.try_exchange_list
    def get_european_exchanges_list(self) -> exchange:
        return self.euro_exchange_list
class cryptocurrency:
    def __init__(self,coin_name:str,withdraw_fee:float):
        self.name=coin_name
        self.withdraw_fee = 0
        self.bid=None
        self.ask=None
    def set_bid(self):
        pass
    def get_bid(self):
        pass
    def set_ask(self):
        pass
    def get_ask(self):
        pass
    def get_withdraw_fee(self)->str:
        return self.withdraw_fee
    def get_name(self)->str:
        return self.name

class Bitcoin(cryptocurrency):
    def __init__(self,withdraw_fee:float):
        super().__init__("Bitcoin",withdraw_fee)
    def set_bid(self,bid_price):
        self.bid = bid_price
    def get_bid(self):
        return self.bid
    def set_ask(self,ask_price):
        self.ask = ask_price
    def get_ask(self):
        return self.ask
    def get_withdraw_fee(self)->str:
        return self.withdraw_fee

class Ethereum(cryptocurrency):
    def __init__(self,withdraw_fee:float):
        super().__init__("Ethereum",withdraw_fee)
    def set_bid(self,bid_price):
        self.bid = bid_price
    def get_bid(self):
        return self.bid
    def set_ask(self,ask_price):
        self.ask = ask_price
    def get_ask(self):
        return self.ask
    def get_withdraw_fee(self)->str:
        return self.withdraw_fee

class Tezos(cryptocurrency):
    def __init__(self,withdraw_fee:float):
        super().__init__("Tezos",withdraw_fee)
    def set_bid(self,bid_price):
        self.bid = bid_price
    def get_bid(self):
        return self.bid
    def set_ask(self,ask_price):
        self.ask = ask_price
    def get_ask(self):
        return self.ask
    def get_withdraw_fee(self)->str:
        return self.withdraw_fee

class Link(cryptocurrency):
    def __init__(self,withdraw_fee:float):
        super().__init__("Link",withdraw_fee)
    def set_bid(self,bid_price):
        self.bid = bid_price
    def get_bid(self):
        return self.bid
    def set_ask(self,ask_price):
        self.ask = ask_price
    def get_ask(self):
        return self.ask
    def get_withdraw_fee(self)->str:
        return self.withdraw_fee

class Cosmos(cryptocurrency):
    def __init__(self,withdraw_fee:float):
        super().__init__("Cosmos",withdraw_fee)
    def set_bid(self,bid_price):
        self.bid = bid_price
    def get_bid(self):
        return self.bid
    def set_ask(self,ask_price):
        self.ask = ask_price
    def get_ask(self):
        return self.ask
    def get_withdraw_fee(self)->str:
        return self.withdraw_fee

class Stellar(cryptocurrency):
    def __init__(self,withdraw_fee:float):
        super().__init__("Stellar",withdraw_fee)
    def set_bid(self,bid_price):
        self.bid = bid_price
    def get_bid(self):
        return self.bid
    def set_ask(self,ask_price):
        self.ask = ask_price
    def get_ask(self):
        return self.ask
    def get_withdraw_fee(self)->str:
        return self.withdraw_fee
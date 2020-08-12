import euro_oracles,exchanges



class exchange_aggregator:
    def __init__(self):
        self.paribu = exchanges.turkish_exchange()
        self.kraken = exchanges.europe_exchange()
        self.exchange_list= {
            'PARIBU': self.paribu,
            'KRAKEN': self.kraken
        }
    def get_exchange(self,exchange_name:str) -> exchanges.exchange:
        return self.exchange_list[exchange_name]



class controller:
    def __init__(self,exchange_1:str,exchange_2:str):
        self.curr_converter = euro_oracles.currconv()
        self.aggregator = exchange_aggregator()
        self.pair_1 = self.aggregator.get_exchange(exchange_1)
        self.pair_2 = self.aggregator.get_exchange(exchange_2)
    def refresh(self):
        self.pair_1.refresh()
        self.pair_2.refresh()
        self.curr_converter.refresh()
    def calculate_arbitrage(self):
        self.refresh()
        print(self.pair_1.get_btc_bid() - self.pair_2.get_btc_ask()*self.curr_converter.get_euro_try_parity())
        print(self.pair_1.get_xtz_bid() -  self.pair_2.get_xtz_ask()*self.curr_converter.get_euro_try_parity())
        print(self.pair_1.get_link_bid() -  self.pair_2.get_link_ask()*self.curr_converter.get_euro_try_parity())


main = controller("PARIBU", "KRAKEN")
main.calculate_arbitrage()


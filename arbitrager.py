import euro_oracles,exchanges
from tabulate import tabulate



class exchange_aggregator:
    def __init__(self):
        self.paribu = exchanges.PARIBU()
        self.kraken = exchanges.KRAKEN()
        self.exchange_list= {
            'PARIBU': self.paribu,
            'KRAKEN': self.kraken
        }
    def get_exchange(self,exchange_name:str) -> exchanges.exchange:
        return self.exchange_list[exchange_name]

class console_drawer:
    @staticmethod
    def draw(text:str):
        table = [[text]]
        output = tabulate(table, tablefmt='grid')
        print(output)


class controller:
    def __init__(self,exchange_1:str,exchange_2:str):
        self.exchange_1 = exchange_1
        self.exchange_2 = exchange_2
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
        self.calculate_btc_arbitrage()
        self.calculate_eth_arbitrage()
        self.calculate_xtz_arbitrage()
        self.calculate_link_arbitrage()


    def calculate_btc_arbitrage(self):   
        text = ('Bitcoin bid price on '+ self.exchange_1 +  ' is ' + str(self.pair_1.get_btc_bid())  +
        '\nBitcoin ask price on '+ self.exchange_2 + ' is ' + str(self.pair_2.get_btc_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.exchange_2 +
        ' Bitcoin price in TRY is '+ str(self.pair_2.get_btc_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_btc_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Bitcoin is ' + str(self.pair_1.get_btc_bid() - self.pair_2.get_btc_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)
    def calculate_eth_arbitrage(self):   
        text = ('Ethereum bid price on '+ self.exchange_1 +  ' is ' + str(self.pair_1.get_eth_bid())  +
        '\nEthereum ask price on '+ self.exchange_2 + ' is ' + str(self.pair_2.get_eth_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.exchange_2 +
        ' Ethereum price in TRY is '+ str(self.pair_2.get_eth_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_eth_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Ethereum is ' + str(self.pair_1.get_eth_bid() - self.pair_2.get_eth_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)

    def calculate_xtz_arbitrage(self):   
        text = ('Tezos bid price on '+ self.exchange_1 +  ' is ' + str(self.pair_1.get_xtz_bid())  +
        '\nTezos ask price on '+ self.exchange_2 + ' is ' + str(self.pair_2.get_xtz_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.exchange_2 +
        ' Tezos price in TRY is '+ str(self.pair_2.get_xtz_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_xtz_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Tezos is ' + str(self.pair_1.get_xtz_bid() - self.pair_2.get_xtz_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)

    def calculate_link_arbitrage(self):   
        text = ('Link bid price on '+ self.exchange_1 +  ' is ' + str(self.pair_1.get_link_bid())  +
        '\nLink ask price on '+ self.exchange_2 + ' is ' + str(self.pair_2.get_link_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.exchange_2 +
        ' Link price in TRY is '+ str(self.pair_2.get_link_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_link_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Link is ' + str(self.pair_1.get_link_bid() - self.pair_2.get_link_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)
       


main = controller("PARIBU", "KRAKEN")
main.calculate_arbitrage()


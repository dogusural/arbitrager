import sys
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
    def draw(text:str,file:str=None):
        table = [[text]]
        output = tabulate(table, tablefmt='grid')
        console_drawer.smart_print(output,file)
    @staticmethod
    def smart_print(text:str,filename:str=None):
        if filename and filename != '-':
            fh = open(filename, 'w')
        else:
            fh = sys.stdout

        try:
            print(text, file=fh) # Python 3.x
        finally:
            if fh is not sys.stdout:
                fh.close()


class controller:
    def __init__(self,try_exchange:str,euro_exchange:str):
        self.try_exchange = try_exchange
        self.euro_exchange = euro_exchange
        self.curr_converter = euro_oracles.currconv()
        self.aggregator = exchange_aggregator()
        self.pair_1 = self.aggregator.get_exchange(try_exchange)
        self.pair_2 = self.aggregator.get_exchange(euro_exchange)
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
        text = ('Bitcoin bid price on '+ self.try_exchange +  ' is ' + str(self.pair_1.get_btc_bid())  +
        '\nBitcoin ask price on '+ self.euro_exchange + ' is ' + str(self.pair_2.get_btc_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.euro_exchange +
        ' Bitcoin price in TRY is '+ str(self.pair_2.get_btc_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_btc_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Bitcoin is ' + str(self.pair_1.get_btc_bid() - self.pair_2.get_btc_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)
    def calculate_eth_arbitrage(self):   
        text = ('Ethereum bid price on '+ self.try_exchange +  ' is ' + str(self.pair_1.get_eth_bid())  +
        '\nEthereum ask price on '+ self.euro_exchange + ' is ' + str(self.pair_2.get_eth_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.euro_exchange +
        ' Ethereum price in TRY is '+ str(self.pair_2.get_eth_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_eth_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Ethereum is ' + str(self.pair_1.get_eth_bid() - self.pair_2.get_eth_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)

    def calculate_xtz_arbitrage(self):   
        text = ('Tezos bid price on '+ self.try_exchange +  ' is ' + str(self.pair_1.get_xtz_bid())  +
        '\nTezos ask price on '+ self.euro_exchange + ' is ' + str(self.pair_2.get_xtz_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.euro_exchange +
        ' Tezos price in TRY is '+ str(self.pair_2.get_xtz_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_xtz_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Tezos is ' + str(self.pair_1.get_xtz_bid() - self.pair_2.get_xtz_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)

    def calculate_link_arbitrage(self):   
        text = ('Link bid price on '+ self.try_exchange +  ' is ' + str(self.pair_1.get_link_bid())  +
        '\nLink ask price on '+ self.euro_exchange + ' is ' + str(self.pair_2.get_link_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ self.euro_exchange +
        ' Link price in TRY is '+ str(self.pair_2.get_link_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(self.pair_2.get_link_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Link is ' + str(self.pair_1.get_link_bid() - self.pair_2.get_link_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY')
        console_drawer.draw(text)
       


main = controller("PARIBU", "KRAKEN")
main.calculate_arbitrage()


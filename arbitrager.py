import euro_oracles,exchanges
from draw import console_drawer



class controller:
    def __init__(self,capital_in_euros:int):
        self.capital = capital_in_euros
        self.curr_converter = euro_oracles.currconv()
        self.aggregator = exchanges.exchange_aggregator()
        self.turkish_exchanges = self.aggregator.get_turkish_exchanges_list()
        self.european_exchanges = self.aggregator.get_european_exchanges_list()
    def refresh(self):
        for turkish_exchange in self.turkish_exchanges:
            turkish_exchange.refresh()
        for european_exchange in self.european_exchanges:
            european_exchange.refresh()
        self.curr_converter.refresh()
    def calculate_arbitrage(self):
        self.refresh()
        for turkish_exchange in self.turkish_exchanges:
            for european_exchange in self.european_exchanges:
                self.calculate_btc_arbitrage(turkish_exchange,european_exchange)
                self.calculate_eth_arbitrage(turkish_exchange,european_exchange)
                self.calculate_xtz_arbitrage(turkish_exchange,european_exchange)
                self.calculate_link_arbitrage(turkish_exchange,european_exchange)

    def calculate_btc_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):   
        text = ('Bitcoin bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_btc_bid())  +
        '\nBitcoin ask price on '+ european_exchange.get_name() + ' is ' + str(european_exchange.get_btc_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Bitcoin price in TRY is '+ str(european_exchange.get_btc_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_btc_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Bitcoin is ' + str(turkish_exchange.get_btc_bid() - european_exchange.get_btc_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY'+
        '\nTotal profit for Bitcoin arbitrage is ' + str((self.capital / european_exchange.get_btc_ask()) * (turkish_exchange.get_btc_bid() - european_exchange.get_btc_ask()*self.curr_converter.get_euro_try_parity())) )
        console_drawer.draw(text)
        
    def calculate_eth_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):   
        text = ('Ethereum bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_eth_bid())  +
        '\nEthereum ask price on '+ european_exchange.get_name() + ' is ' + str(european_exchange.get_eth_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Ethereum price in TRY is '+ str(european_exchange.get_eth_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_eth_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Ethereum is ' + str(turkish_exchange.get_eth_bid() - european_exchange.get_eth_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY'+
        '\nTotal profit for Ethereum arbitrage is ' + str((self.capital / european_exchange.get_eth_ask()) * (turkish_exchange.get_eth_bid() - european_exchange.get_eth_ask()*self.curr_converter.get_euro_try_parity())) )
        console_drawer.draw(text)

    def calculate_xtz_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):   
        text = ('Tezos bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_xtz_bid())  +
        '\nTezos ask price on '+ european_exchange.get_name() + ' is ' + str(european_exchange.get_xtz_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Tezos price in TRY is '+ str(european_exchange.get_xtz_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_xtz_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Tezos is ' + str(turkish_exchange.get_xtz_bid() - european_exchange.get_xtz_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY'+
        '\nTotal profit for Tezos arbitrage is ' + str((self.capital / european_exchange.get_xtz_ask()) * (turkish_exchange.get_xtz_bid() - european_exchange.get_xtz_ask()*self.curr_converter.get_euro_try_parity())) )
        console_drawer.draw(text)

    def calculate_link_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):   
        text = ('Link bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_link_bid())  +
        '\nLink ask price on '+ european_exchange.get_name() + ' is ' + str(european_exchange.get_link_ask()) +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Link price in TRY is '+ str(european_exchange.get_link_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_link_ask()*self.curr_converter.get_euro_try_parity()) +
        '\nArbitrage margin for Link is ' + str(turkish_exchange.get_link_bid() - european_exchange.get_link_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY'+
        '\nTotal profit for link arbitrage is ' + str((self.capital / european_exchange.get_link_ask()) * (turkish_exchange.get_link_bid() - european_exchange.get_link_ask()*self.curr_converter.get_euro_try_parity())) )
        console_drawer.draw(text)
       




def main():
    arbitrager = controller(1000)
    arbitrager.calculate_arbitrage()

if __name__ == "__main__":
    main()
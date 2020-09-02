import euro_oracles,exchanges
from draw import console_drawer



class EuropeantoTurkishArbitrager:
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
                self.calculate_atom_arbitrage(turkish_exchange,european_exchange)
                self.calculate_xlm_arbitrage(turkish_exchange,european_exchange)

    def calculate_btc_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):

        arbitrage = (turkish_exchange.get_btc_bid() - european_exchange.get_btc_ask()*self.curr_converter.get_euro_try_parity())
        buy_exchange_fee = (european_exchange.get_maker_fee() * self.capital )
        coin_amount = (( self.capital - buy_exchange_fee  ) / european_exchange.get_btc_ask())
        sell_exchange_fee = coin_amount * turkish_exchange.get_btc_bid() * turkish_exchange.get_maker_fee()
        total_profit = coin_amount * arbitrage - sell_exchange_fee

        text = ('Bitcoin bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_btc_bid()) + ' TRY' +
        '\nBitcoin ask price on ' + european_exchange.get_name() + ' is ' + str(european_exchange.get_btc_ask()) + ' EUR' +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Bitcoin price in TRY is ' + str(european_exchange.get_btc_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_btc_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY' +
        '\nArbitrage margin for Bitcoin is ' + str(arbitrage) + ' TRY' +
        '\nBitcoin which can be bought with the capital of '+ str(self.capital) + ' EUR is ' + str(self.capital) + ' / ' + str(european_exchange.get_btc_ask()) + ' = ' + str(coin_amount) +
        '\nFees for ' +  european_exchange.get_name() + ' = ' + str(buy_exchange_fee * self.curr_converter.get_euro_try_parity() ) + ' TRY. Fees for ' +  turkish_exchange.get_name() + ' = ' + str(sell_exchange_fee) +' TRY'+
        '\nTotal profit for Bitcoin arbitrage is ' + str(coin_amount) + ' * ' + str(arbitrage) + ' = ' + str(total_profit) + ' TRY' )
        console_drawer.draw(text)
        
    def calculate_eth_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):

        arbitrage = (turkish_exchange.get_eth_bid() - european_exchange.get_eth_ask()*self.curr_converter.get_euro_try_parity())
        buy_exchange_fee = (european_exchange.get_maker_fee() * self.capital )
        coin_amount = ((self.capital - buy_exchange_fee) / european_exchange.get_eth_ask())
        sell_exchange_fee = coin_amount * turkish_exchange.get_eth_bid() * turkish_exchange.get_maker_fee()
        total_profit = coin_amount * arbitrage - sell_exchange_fee

        text = ('Ethereum bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_eth_bid())  + ' TRY' +
        '\nEthereum ask price on ' + european_exchange.get_name() + ' is ' + str(european_exchange.get_eth_ask()) + ' EUR' +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Ethereum price in TRY is ' + str(european_exchange.get_eth_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_eth_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY' +
        '\nArbitrage margin for Ethereum is ' + str(arbitrage) + ' TRY'+
        '\nEthereum which can be bought with the capital of '+ str(self.capital) + ' EUR is ' + str(self.capital) + ' / ' + str(european_exchange.get_eth_ask()) + ' = ' + str(coin_amount) +
        '\nFees for ' +  european_exchange.get_name() + ' = ' + str(buy_exchange_fee * self.curr_converter.get_euro_try_parity() ) + ' TRY. Fees for ' +  turkish_exchange.get_name() + ' = ' + str(sell_exchange_fee) +' TRY'+
        '\nTotal profit for Ethereum arbitrage is ' + str(coin_amount) + ' * ' + str(arbitrage) + ' = ' + str(total_profit) + ' TRY' )
        console_drawer.draw(text)

    def calculate_xtz_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):

        arbitrage = (turkish_exchange.get_xtz_bid() - european_exchange.get_xtz_ask()*self.curr_converter.get_euro_try_parity())
        buy_exchange_fee = (european_exchange.get_maker_fee() * self.capital )
        coin_amount = ((self.capital - (european_exchange.get_maker_fee() * self.capital) ) / european_exchange.get_xtz_ask())
        sell_exchange_fee = coin_amount * turkish_exchange.get_xtz_bid() * turkish_exchange.get_maker_fee()
        total_profit = coin_amount * arbitrage - sell_exchange_fee

        text = ('Tezos bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_xtz_bid())  + ' TRY' +
        '\nTezos ask price on ' + european_exchange.get_name() + ' is ' + str(european_exchange.get_xtz_ask()) + ' EUR' +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Tezos price in TRY is ' + str(european_exchange.get_xtz_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_xtz_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY' +
        '\nArbitrage margin for Tezos is ' + str(arbitrage) + ' TRY'+
        '\nTezos which can be bought with the capital of '+ str(self.capital) + ' EUR is ' + str(self.capital) + ' / ' + str(european_exchange.get_xtz_ask()) + ' = ' + str(coin_amount) +
        '\nFees for ' +  european_exchange.get_name() + ' = ' + str(buy_exchange_fee * self.curr_converter.get_euro_try_parity() ) + ' TRY. Fees for ' +  turkish_exchange.get_name() + ' = ' + str(sell_exchange_fee) +' TRY'+
        '\nTotal profit for Tezos arbitrage is ' + str(coin_amount) + ' * ' + str(arbitrage) + ' = ' + str(total_profit) + ' TRY' )
        console_drawer.draw(text)

    def calculate_link_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):

        arbitrage = (turkish_exchange.get_link_bid() - european_exchange.get_link_ask()*self.curr_converter.get_euro_try_parity())
        buy_exchange_fee = (european_exchange.get_maker_fee() * self.capital )
        coin_amount = ((self.capital - (european_exchange.get_maker_fee() * self.capital) ) / european_exchange.get_link_ask())
        sell_exchange_fee = coin_amount * turkish_exchange.get_link_bid() * turkish_exchange.get_maker_fee()
        total_profit = coin_amount * arbitrage - sell_exchange_fee

        text = ('Link bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_link_bid())  + ' TRY' +
        '\nLink ask price on ' + european_exchange.get_name() + ' is ' + str(european_exchange.get_link_ask()) + ' EUR' +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Link price in TRY is ' + str(european_exchange.get_link_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_link_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY' +
        '\nArbitrage margin for Link is ' + str(turkish_exchange.get_link_bid() - european_exchange.get_link_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY'+
        '\nLink which can be bought with the capital of '+ str(self.capital) + ' EUR is ' + str(self.capital) + ' / ' + str(european_exchange.get_link_ask()) + ' = ' + str(coin_amount) +
        '\nFees for ' +  european_exchange.get_name() + ' = ' + str(buy_exchange_fee * self.curr_converter.get_euro_try_parity() ) + ' TRY. Fees for ' +  turkish_exchange.get_name() + ' = ' + str(sell_exchange_fee) +' TRY'+
        '\nTotal profit for link arbitrage is ' + str(coin_amount) + ' * ' + str(arbitrage) + ' = ' + str(total_profit) + ' TRY' )
        console_drawer.draw(text)

    def calculate_atom_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):

        arbitrage = (turkish_exchange.get_atom_bid() - european_exchange.get_atom_ask()*self.curr_converter.get_euro_try_parity())
        buy_exchange_fee = (european_exchange.get_maker_fee() * self.capital )
        coin_amount = ((self.capital - (european_exchange.get_maker_fee() * self.capital) ) / european_exchange.get_atom_ask())
        sell_exchange_fee = coin_amount * turkish_exchange.get_atom_bid() * turkish_exchange.get_maker_fee()
        total_profit = coin_amount * arbitrage - sell_exchange_fee

        text = ('Atom bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_atom_bid())  + ' TRY' +
        '\nAtom ask price on ' + european_exchange.get_name() + ' is ' + str(european_exchange.get_atom_ask()) + ' EUR' +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Atom price in TRY is ' + str(european_exchange.get_atom_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_atom_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY' +
        '\nArbitrage margin for Atom is ' + str(turkish_exchange.get_atom_bid() - european_exchange.get_atom_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY'+
        '\nAtom which can be bought with the capital of '+ str(self.capital) + ' EUR is ' + str(self.capital) + ' / ' + str(european_exchange.get_atom_ask()) + ' = ' + str(coin_amount) +
        '\nFees for ' +  european_exchange.get_name() + ' = ' + str(buy_exchange_fee * self.curr_converter.get_euro_try_parity() ) + ' TRY. Fees for ' +  turkish_exchange.get_name() + ' = ' + str(sell_exchange_fee) +' TRY'+
        '\nTotal profit for Atom arbitrage is ' + str(coin_amount) + ' * ' + str(arbitrage) + ' = ' + str(total_profit) + ' TRY' )
        console_drawer.draw(text)

    def calculate_xlm_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange):

        arbitrage = (turkish_exchange.get_xlm_bid() - european_exchange.get_xlm_ask()*self.curr_converter.get_euro_try_parity())
        buy_exchange_fee = (european_exchange.get_maker_fee() * self.capital )
        coin_amount = ( (self.capital - (european_exchange.get_maker_fee() * self.capital) ) / european_exchange.get_xlm_ask())
        sell_exchange_fee = coin_amount * turkish_exchange.get_xlm_bid() * turkish_exchange.get_maker_fee()
        total_profit = coin_amount * arbitrage - sell_exchange_fee

        text = ('Xlm bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_exchange.get_xlm_bid())  + ' TRY' +
        '\nXlm ask price on ' + european_exchange.get_name() + ' is ' + str(european_exchange.get_xlm_ask()) + ' EUR' +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' Xlm price in TRY is ' + str(european_exchange.get_xlm_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_exchange.get_xlm_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY' +
        '\nArbitrage margin for Xlm is ' + str(turkish_exchange.get_xlm_bid() - european_exchange.get_xlm_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY'+
        '\nXlm which can be bought with the capital of '+ str(self.capital) + ' EUR is ' + str(self.capital) + ' / ' + str(european_exchange.get_xlm_ask()) + ' = ' + str(coin_amount) +
        '\nFees for ' +  european_exchange.get_name() + ' = ' + str(buy_exchange_fee * self.curr_converter.get_euro_try_parity() ) + ' TRY. Fees for ' +  turkish_exchange.get_name() + ' = ' + str(sell_exchange_fee) +' TRY'+
        '\nTotal profit for Xlm arbitrage is ' + str(coin_amount) + ' * ' + str(arbitrage) + ' = ' + str(total_profit) + ' TRY' )
        console_drawer.draw(text)
       




def main():
    arbitrager = EuropeantoTurkishArbitrager(1000)
    arbitrager.calculate_arbitrage()

if __name__ == "__main__":
    main()
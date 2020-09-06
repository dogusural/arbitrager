import euro_oracles,exchanges
from draw import console_drawer
import coins



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
        maximum_profit = 0
        most_profitable_arbitrage_info = ()
        for turkish_exchange in self.turkish_exchanges:
            for european_exchange in self.european_exchanges:
                console_drawer.draw_header(european_exchange.get_name(),turkish_exchange.get_name())
                for (T,E) in zip(turkish_exchange.get_supported_coins(), european_exchange.get_supported_coins()):
                    if T is not None and E is not None :
                        arbitrage_info = self.display_arbitrage(turkish_exchange,european_exchange,T,E)
                        if arbitrage_info[0] > maximum_profit :
                            most_profitable_arbitrage_info = arbitrage_info
                            maximum_profit = arbitrage_info[0]
        console_drawer.draw_results(most_profitable_arbitrage_info)
                   

    def display_arbitrage(self,turkish_exchange:exchanges.exchange, european_exchange:exchanges.exchange, turkish_coin:coins.cryptocurrency, european_coin:coins.cryptocurrency):

        arbitrage = (turkish_coin.get_bid() - european_coin.get_ask()*self.curr_converter.get_euro_try_parity())
        buy_exchange_fee = (european_exchange.get_maker_fee() * self.capital )
        coin_amount = (( self.capital - buy_exchange_fee  ) / european_coin.get_ask()) - european_coin.get_withdraw_fee()
        sell_exchange_fee = coin_amount * turkish_coin.get_bid() * turkish_exchange.get_maker_fee()
        total_profit = coin_amount * arbitrage - sell_exchange_fee

        text = ( turkish_coin.get_name() + ' bid price on '+ turkish_exchange.get_name() +  ' is ' + str(turkish_coin.get_bid()) + ' TRY' +
        '\n' + turkish_coin.get_name() + ' ask price on ' + european_exchange.get_name() + ' is ' + str(european_coin.get_ask()) + ' EUR' +
        '\nEURO/TRY parity is ' + str(self.curr_converter.get_euro_try_parity()) +'\n'+ european_exchange.get_name() +
        ' ' + turkish_coin.get_name() + ' price in TRY is ' + str(european_coin.get_ask()) + ' * ' + str(self.curr_converter.get_euro_try_parity()) +
        ' = '+ str(european_coin.get_ask()*self.curr_converter.get_euro_try_parity()) + ' TRY' +
        '\nArbitrage margin for ' + turkish_coin.get_name() + ' is ' + str(arbitrage) + ' TRY' +
        '\n' + turkish_coin.get_name() + ' which can be bought with the capital of '+ str(self.capital) + ' EUR is ' + str(self.capital) + ' / ' + str(european_coin.get_ask()) + ' - ' + str(european_coin.get_withdraw_fee()) + ' = ' + str(coin_amount) +
        '\nFees for ' +  european_exchange.get_name() + ' = ' + str(buy_exchange_fee * self.curr_converter.get_euro_try_parity() ) + ' TRY. Fees for ' +  turkish_exchange.get_name() + ' = ' + str(sell_exchange_fee) +' TRY'+
        '\nTotal profit for ' + turkish_coin.get_name() + ' arbitrage is ' + str(coin_amount) + ' * ' + str(arbitrage) + ' = ' + str(total_profit) + ' TRY' )
        console_drawer.draw(text)
        return (total_profit,turkish_exchange.get_name(),european_exchange.get_name(),turkish_coin.get_name())


def main():
    arbitrager = EuropeantoTurkishArbitrager(1000)
    arbitrager.calculate_arbitrage()

if __name__ == "__main__":
    main()
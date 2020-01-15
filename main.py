import requests
from stock_api import Stock_API
from stock_analyzer import Stock_Analyzer
from typing import List


def main():


    stock_API = Stock_API()
    stock_analyzer = Stock_Analyzer()

    tickers: List[str] = stock_API.get_market_tickers("nasdaq")
    flatbased_stocks: List[str] = []
    for i in range(3):

        daily_stock_chart: List[dict] = stock_API.get_stock_month_data(tickers[i])
        if(stock_analyzer.is_flatbase(daily_stock_chart)):
            flatbased_stocks.append(tickers[i])

    for ticker in flatbased_stocks:
        print(f"Ticker: {ticker}")


main()
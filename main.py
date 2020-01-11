import requests
from stock_api import Stock_API
from stock_analyzer import Stock_Analyzer


def main():


    stock_API = Stock_API()
    stock_analyzer = Stock_Analyzer()


    day_stock_chart: List[dict] = stock_API.get_stock_month_data("SRNE")
    
    weekly_data: List[dict] = stock_API.get_monthly_data("SRNE")

    weekly_high: float = stock_analyzer.half_yearly_high(weekly_data)   #26 weekly high

    stock_analyzer.is_flatbase(day_stock_chart)


main()
import requests
import json
from typing import List

class Stock_API():

    def __init__(self):

        self.s = requests.Session()
        self.api_key: str = open("api_key.txt", "r").readline()
        self.api_url: str = "https://www.alphavantage.co/query?function="

    def get_monthly_data(self, ticker: str) -> List[dict]:
        time_function: str = "TIME_SERIES_WEEKLY"
        res = self.s.get(f"{self.api_url}{time_function}&symbol={ticker}&apikey={self.api_key}").content

        return json.loads(res)

    def get_stock_month_data(self, ticker: str) -> List[dict]:

        time_function: str = "TIME_SERIES_DAILY"
        response: dict = json.loads(self.s.get(f"{self.api_url}{time_function}&symbol={ticker}&apikey={self.api_key}").content)

        stock_chart: List[dict] = []
        '''
        {
            "day" : "2020 ...."
            "data" : {
                "open" : "...",
                "close" : "...",
                "high" : "...",
                "volume" : "...."
        }
        '''

        for day in response["Time Series (Daily)"].keys():
            stock_chart.append(
                {   
                    "day": day,
                    "data" : response["Time Series (Daily)"][day]
                }
            )
            #print(day , " " , response["Time Series (Daily)"][day])
        return stock_chart
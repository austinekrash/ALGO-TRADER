from typing import List
import json
import statistics

class Stock_Analyzer():

    def __init__(self):
        self.deviation_max: float = 0.25

    def half_yearly_high(self, stock_chart: List[dict]) -> float:
        highest: float = 0.0
        weeks: list = stock_chart["Weekly Time Series"].keys() #all 
        for i in range(0,26):
            high: float = float(stock_chart["Weekly Time Series"][weeks[i]]["2. high"])
            if (high > highest):
                highest = high  #420 dank
        return highest

    def is_flatbase(self, stock_chart: List[dict]) -> bool:

        #RANGE SHOULD BE FROM CURRENT TO PAST 30 DAYS?
        start: int = 32

        #current: float = float(stock_chart[start]["data"]["open"])
        #oldest: float = float(stock_chart[30]["data"]["close"])
        #median: float
        closing_list: list = []
        for i in range(start, 60): #test
            print("CLOSE: ", stock_chart[i]["data"]["4. close"])
            closing_list.append(float(stock_chart[i]["data"]["4. close"]))
        
        std_deviation: float = statistics.stdev(closing_list)   #Standard deviation of the list of share prices
        print(f"STD DEVIATION: {std_deviation}")

        if(std_deviation < self.deviation_max):
            return True
       

        #high: float
        #low: float

        # for i in range(32, len(stock_chart)):
        #     print("Day: ", stock_chart[i]["day"], json.dumps(stock_chart[i]["data"], indent=4))



        # for day in stock_chart:
        #     print("Day: ", day["day"], " ", json.dumps(day["data"], indent=4))
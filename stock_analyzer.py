from typing import List
import json
import statistics
import pandas as pd

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

        #The higher the number, the earlier the date. The most recent index is the most recent share price.
        start: int = 0 #34

        recent_list: list = []
        for i in range(start, 30): #test
            #print("CLOSE: ", stock_chart[i]["data"]["4. close"])
            recent_list.append(float(stock_chart[i]["data"]["4. close"]))
        
        mean_recent: float = statistics.mean(recent_list)

        #print(f"Mean of recent list {mean_recent}")
            
        std_deviation_recent: float = statistics.stdev(recent_list)   #Standard deviation of the list of share prices
        #print(f"STD DEVIATION of the RECENT LIST: {std_deviation_recent}")

        CV: float = (std_deviation_recent / mean_recent) * 100
        #print(f"CV is: {CV}")

        if (std_deviation_recent < 1):
            return True
# app/robo_advisor.py

import requests
import json
import csv
import os
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    return "${0:.2f}".format(my_price)



# INFO Inputs
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
#print(api_key)
symbol = "MSFT"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
## https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo&datatype=csv
response = requests.get(request_url)
#print(type(response)) #<class 'requests.models.Response'>
#print(response.status_code) # 200
#print(response.text)  

# parses the response.test which is string into a dictionary
parsed_response = json.loads(response.text)
last_refreshed = parsed_response['Meta Data']['3. Last Refreshed']

#breakpoint()
tsd = parsed_response['Time Series (Daily)']
dates = list(tsd.keys())  # assumes first day is on top;sort to ensure latest day is first
latest_day = dates[0]
latest_close = tsd[latest_day]['4. close']

# get high prices from each day
#high_prices =[]
#recent_high = max(high_prices)
high_prices =[]
low_prices = []

for date in dates:
    high_price = tsd[date]['2. high']
    low_price = tsd[date]['3. low']
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))


# take maximum value  
recent_high = max(high_prices)
recent_low = min(low_prices)
#quit()

# INFO Output


#csv_file_path = 'data/prices.csv'
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
   
    for date in dates:
        daily_prices = tsd[date]   #tsd[date] is a dictionary
        writer.writerow({
        "timestamp": date,
         "open": daily_prices['1. open'],
         "high":daily_prices['2. high'],
         "low":daily_prices['3. low'],
         "close":daily_prices['4. close'],
         "volume": daily_prices['5. volume']
        
        })

   
    #writer.writerow({"city": "New York", "name": "Mets"})
    #writer.writerow({"city": "Boston", "name": "Red Sox"})
    #writer.writerow({"city": "New Haven", "name": "Ravens"})



print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")




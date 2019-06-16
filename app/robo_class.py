# app/robo_advisor.py

import requests
import json

def to_usd(my_price):
    return "${0:.2f}".format(my_price)



# INFO Inputs

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
## https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo&datatype=csv
response = requests.get(request_url)
#print(type(response)) #<class 'requests.models.Response'>
#print(response.status_code) # 200
#print(response.text)  

# parses the response.test which is string into a dictionary
parsed_response = json.loads(response.text)
last_refreshed = parsed_response['Meta Data']['3. Last Refreshed']
latest_close = parsed_response['Time Series (Daily)']['2019-06-14']['4. close']

#breakpoint()

#quit()

# INFO Output


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
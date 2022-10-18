import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = "0DVAXK7G8THN4T3Z"
news_api_key = "8a8714ce13e34703adcfd74aea8ce300"

def get_news():
    news_parameters = {
        "q": "tesla",
        "apiKey": news_api_key
    }
    response = requests.get(url="https://newsapi.org/v2/everything?", params=news_parameters)
    response.raise_for_status()
    data = response.json()
    three_news = data["articles"][:3][-1]
    print(three_news)
    
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

response = requests.get(url="https://www.alphavantage.co/query?", params=stock_parameters)
response.raise_for_status()
data =  response.json()
daily = data["Time Series (Daily)"]
indexs = list(daily)
day_before_yesterday =  daily[indexs[2]]
yesterday = daily[indexs[1]]
day_before_yesterday = day_before_yesterday["1. open"]
yesterdays_open = yesterday["1. open"]
difrence = float(yesterdays_open) / float(day_before_yesterday)
if difrence > 1.05 or difrence < 0.95:
    get_news()
get_news()

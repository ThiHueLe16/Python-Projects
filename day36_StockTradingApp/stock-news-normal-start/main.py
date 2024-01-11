import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "5JFLEFTPH54V70XI"
NEWS_API = "a7614faac31f414f93f7182f578aecb9"
# get your TWILIO_SID and TWILIO_AUTH_TOKEN from twilio website
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
# save your actual number hier to send and receive message
FROM_TELNUMBER = "+491111111111"
TO_NUMBER = "+49111111111111"

# ---------------------------------------------TRADE STOCK---------------------------------------
stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
response.raise_for_status()
data = response.json()

today = datetime.now()
yesterdayDate = (today - timedelta(days=1)).date().strftime('%Y-%m-%d')
yesterdayCloseStockPrice = float(data["Time Series (Daily)"][yesterdayDate]["4. close"])

beforeYesterday = (today - timedelta(days=2)).date().strftime('%Y-%m-%d')
beforeYesterdayStockPrice = float(data["Time Series (Daily)"][beforeYesterday]["4. close"])

diff = round(yesterdayCloseStockPrice - beforeYesterdayStockPrice)

percentage = (diff / beforeYesterdayStockPrice) * 100
up_down = None
if diff >= 0:
    up_down = "🔺"
else:
    up_down = "🔻"
if abs(percentage) > 5:
    # ---------------------------------------------GET NEWS---------------------------------------
    newsParams = {
        "q": COMPANY_NAME,
        "from": yesterdayDate,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API
    }
    newResponse = requests.get(url=NEWS_ENDPOINT, params=newsParams)
    newResponse.raise_for_status()
    news = newResponse.json()
    articles = news["articles"]
    threeArticles = articles[:3]

    # ---------------------------------------------SEND MESSAGES---------------------------------------
    ## Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{abs(percentage)}\nHeadline:{articles['title']}.\n Brief:{articles['description']}"
        for articles in threeArticles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for formatted_article in formatted_articles:
        message = client.messages.create(body=formatted_article, from_=FROM_TELNUMBER, to=TO_NUMBER)

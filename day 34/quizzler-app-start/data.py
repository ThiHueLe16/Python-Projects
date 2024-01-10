import requests
QUESTION_AMOUNT=10
QUESTION_TYPE="boolean"

parameter= {
    "amount":QUESTION_AMOUNT,
    "type": QUESTION_TYPE
}
response= requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()
question_data=response.json()["results"]

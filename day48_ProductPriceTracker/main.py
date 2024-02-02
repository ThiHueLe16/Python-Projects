from bs4 import BeautifulSoup
import lxml
import requests
PRODUCT_URL_LINK="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
EXPECTED_PRICE=200
response=requests.get(PRODUCT_URL_LINK)
response.raise_for_status()
soup = BeautifulSoup(response.content, "lxml")
price=soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
product="".join(soup.find(id="productTitle").get_text().rsplit())

if price_as_float<EXPECTED_PRICE:
    print(f"Price allert!!! {product} is now only {price_as_float}. Come to this link {PRODUCT_URL_LINK} and buy it immediately ")

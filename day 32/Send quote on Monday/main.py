import random
import smtplib
import datetime as dt

MY_EMAIL="huethangnhat@gmail.com"
MY_PASSWORD="Lethihue1601."

with open("quotes.txt") as file:
    all_quotes=file.readlines()

now= dt.datetime.now()
weekday=now.weekday()

if weekday==3:
    quote=random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Monday Motivation\n\n{quote}")

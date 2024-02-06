import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

my_mail = "pythontestangela@gmail.com"
my_pass = "P0ptr0p1ca@"

PRODUCT_URL = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_6?keywords=iphone&qid=1644683492&s=electronics&sr=1-6"

response = requests.get(PRODUCT_URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
                                              "Accept-Language": "en-US,en-IN;q=0.9,en-GB;q=0.8,en;q=0.7,ja;q=0.6"})
data = response.text

soup = BeautifulSoup(data, "html.parser")

display_price = soup.find("span", class_="a-offscreen")
price_with_r_sign = display_price.getText()

price = price_with_r_sign[1:]
float_price = float(price.replace(',', ''))

product_url = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_6?keywords=iphone&qid=1644683492&s=electronics&sr=1-6"
message = f"Apple iPhone 12 (128GB) is now under INR 55,000!\nBuy Now! {product_url}"
if float_price < 55000:
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="pptropican6@gmail.com",
            msg=f"Subject: iPhone price below 55k!\n\n{message}"
        )

















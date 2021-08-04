import lxml
from bs4 import BeautifulSoup
import smtplib
import requests

url = "https://www.amazon.com/gp/product/B000QSNYGI?pf_rd_r=VJW0ZNG7VS3T43JF4S62&pf_rd_p=5ae2c7f8-e0c6-4f35-9071-dc3240e894a8&pd_rd_r=6846105f-717f-45c5-a3d5-fbc21ec9991a&pd_rd_w=jCt1W&pd_rd_wg=qpwNy&ref_=pd_gw_unk&th=1"
#HTTP HEADER can be found on myhttpheader.com
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

#if the price is unavailable, you may receive an error
price = soup.find(id="priceblock_ourprice").get_text()
#print("hi")
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

#my_email = "reminder.imhungry@gmail.com"
#password = ""

#
# file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
# with open(file_path) as letter_file:
#     contents = letter_file.read()
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(my_email, password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg=f"Subject:Happy Birthday!\n\n{contents}"
#     )
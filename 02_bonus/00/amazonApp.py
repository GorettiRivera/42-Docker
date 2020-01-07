import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/gp/product/B07XSQT4Q3?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=M9J2QGW02KFEMMHR072C'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}


def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup1 = BeautifulSoup(soup.prettify(), "html.parser")

    #title
    try:
        title = soup1.find(id="productTitle").get_text().strip()
    except:
        pass

    #price
    try:
        if soup1.find(id="priceblock_saleprice"):
            price = soup1.find(id="priceblock_saleprice").get_text()
        if soup1.find(id="priceblock_ourprice"):
            price  = soup1.find(id="priceblock_ourprice").get_text()
        if soup1.find(id="priceblock_dealprice"):
            price = soup1.find(id="priceblock_dealprice").get_text()
        if not price:
            print("Sorry, We don't know when or if this item will be back in stock.")
        else: 
            converted_price = price[1:].strip()
            converted_price = converted_price.replace(",", "")
            converted_price = converted_price.replace("$", "")
            converted_price = float(converted_price)

            print(title.strip())
            print(converted_price)

            if(converted_price > 128):
                send_mail()
                # print("Send email function")
    except:
        print("Error, please check the price")
    
  

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mgoretti.rivera@gmail.com','pfnnsmyjampvvcfx')

    subject = 'Price fell down!!'
    body = 'Check the amazon link  https://www.amazon.com/Sony-Interchangeable-Digital-28-70mm-Accessory/dp/B00R1P93SC/ref=sr_1_2_sspa?keywords=sony+a7&qid=1570044483&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSU1IUDlYUzhYVkZFJmVuY3J5cHRlZElkPUEwNTI5NDc0MlkwTk8xQjdaQ0FZRyZlbmNyeXB0ZWRBZElkPUExMDMyNTczM08yTlJEMlFQRzJIVCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mgoretti.rivera@gmail.com',
        'goretti_rivera@hotmail.com',
        msg
    )

    print('Email has been sent!!')

    server.quit()

check_price()

# while(True):
#     check_price()
#     time.sleep(86400) # the time is in seconds, so it is set to 1 day


# no price available 
# 'https://www.amazon.com/Bose-SoundLink-Color-Bluetooth-Speaker/dp/B07NHVWP31/ref=sr_1_3?crid=R4LKBEVD8RAN&keywords=bose+speaker&qid=1570073577&s=gateway&sprefix=bose+sp%2Caps%2C204&sr=8-3'

# price id="priceblock_dealprice"
# 'https://www.amazon.com/JUVEA-Supportive-Sleeping-Breathable-Absorbent/dp/B07PP94RHP/ref=sr_1_2?pf_rd_i=gb_main&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=56beed47-26cb-401c-95f5-738a157f0f49&pf_rd_r=CPYM1QQHBYF4F0FY94AH&pf_rd_s=slot-5&pf_rd_t=701&qid=1570423685&smid=A21VHZ1TV3ZUZI&sr=8-2'

# price id="priceblock_ourprice"
# 'https://www.amazon.com/JETech-Samsung-Galaxy-Protective-Shock-Absorption/dp/B06XPQVDMH/ref=pd_ys_c_rfy_2335752011_0?_encoding=UTF8&pd_rd_i=B06XPQVDMH&pd_rd_r=YSYMNH0A7D1C3RKCGQSM&pd_rd_w=MH56A&pd_rd_wg=iuWBm&pf_rd_p=6636a75a-fbe2-408a-b440-ad7d93dc2134&pf_rd_r=YSYMNH0A7D1C3RKCGQSM&psc=1&refRID=YQYCRW5YDH3BZG4RN95P'


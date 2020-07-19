import requests
import smtplib
import time
from bs4 import BeautifulSoup

while True:
    url = "https://liveramp.com/careers/open-positions/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    if str(soup).find("intern") == -1:
        time.sleep(60)
        continue
        
    else:
        msg = '[scrappy notification]: intern posting found'
        fromaddr = ''
        toaddrs  = []
        
      
        break
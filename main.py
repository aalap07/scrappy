import requests
import smtplib
import time
from bs4 import BeautifulSoup
from twilio.rest import Client


while True:
    url = "https://liveramp.com/careers/open-positions/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    # Insert desired job title here
    job = "intern"
    if str(soup).find(job) == -1:
        time.sleep(60)
        continue

    else:
        # Text message version
        account_sid = "SID"


        auth_token  = "TOKEN"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+YOUR_NUMBER",
            from_="+12058595480",
            body="There is a new match for \"" + job + "\" at " + url)


        # Email version

        # Message to be sent upon finding job
        msg = """\
Subject: [scrappy notification]: new intern listing

There is a new match for """ + "\"" + job + "\"" + " at " + url
        
        # Setup gmail server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Sensitive info for logging into server and to/from emails
        fromaddr = 'EMAIL'
        toaddrs = ['EMAIL']
        server.login("EMAIL", "KEY")
        

        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

        break


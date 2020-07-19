import requests
import smtplib
import time
from bs4 import BeautifulSoup
from twilio.rest import Client

# Insert all job board urls here
urls = ["https://liveramp.com/careers/open-positions/"]

while True:
    for url in urls:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        
        # Insert desired job title here
        job = "intern"
        if str(soup).find(job) == -1:
            time.sleep(1800) # Try again half an hour later
            continue

        else:
            # Text messages 
            account_sid = "INSERT_SID"
            auth_token  = "INSERT_TOKEN"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                to="INSERT_NUMBER",
                from_="TWILIO_NUMBER",
                body="There is a new match for \"" + job + "\" at " + url)

            # Email notifications

            # Message to be sent upon finding job
            msg = """\
Subject: [scrappy notification]: Job listing matching """ + job + " has been found" + """

There is a match for """ + "\"" + job + "\"" + " at " + url
            
            # Setup gmail server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Email info for logging into server and to/from emails
            fromaddr = 'YOUR_EMAIL'
            toaddrs = ['YOUR_EMAILS']
            server.login("YOUR_EMAIL", "YOUR_KEY")

            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
            time.sleep(86400) # Send a reminder/check again 24 hours later

            continue


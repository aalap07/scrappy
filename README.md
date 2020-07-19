# scrappy
This is a Python script that allows a user to enter in URLs of job boards they want to watch as well as
the keywords or job titles they are seeking by scraping the pages with Beautiful Soup. The script will run through all of the URLs and check if there are any matches for those keywords on that page. 

Notification options
* Text message using Twilio API
* Email

If a match is found on a given URL, the app will send a notification immediately. It will then wait 24 hours before
sending another one as an additional check/reminder. If there are no matches, the page will be checked again at
30 minute intervals.

# Inspiration
Making the job searching process easier! This can be utilized for any careers page that does not have a mailing
list of its own to notify candidates of future opportunities and reduces the amount of manual checking required to keep
up with new listings.

# Note
All credentials must be provided by the user. This includes email address and email authentication key as well as Twilio API
sid, auth token, and phone numbers.

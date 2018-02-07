import requests
from lxml import html

USERNAME = ""
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/repositories"

session_requests = requests.session()

print "Select ticket"


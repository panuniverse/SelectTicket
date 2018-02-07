import requests
from lxml import html

USERNAME = ""
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/repositories"

session_requests = requests.session()

htmls = requests.get("http://www.12306.cn/mormhweb/")
htmls.encoding = "utf-8"

print htmls.text


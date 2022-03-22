import re
import requests
import urllib
from bs4 import BeautifulSoup
from PIL import Image

#open url page
url= 'https://www.wow4u.com/quote-of-the-day/'
page_request = requests.get(url)

#parse entire website
soup = BeautifulSoup(page_request.text, 'html.parser')

#find first image url
for img in soup.findAll('img'):
    raw_img_link = img.get('src')

    if 'graphics' in raw_img_link:
        break

#further parsing/cleaning
raw_img_link = raw_img_link[2:]
img_link = 'https://www.wow4u.com' + raw_img_link
print(img_link)

#open url and define a random user-agent to bypass security blocks
#what is an user-agent? it's a code that helps you communicate with
#a webpage tailored to your webrowser

#more here: https://www.geeksforgeeks.org/http-headers-user-agent/#:~:text=The%20HTTP%20headers%20User%2DAgent,every%20website%20you%20connect%20to.
#and here: https://whatismyipaddress.com/user-agent
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

#download the image!
local= '/your/path/to/saved/image/daily_quote.jpg'
urllib.request.urlretrieve(img_link,local)

#display the image!
img = Image.open('daily_quote.jpg')
img = img.resize((1000, 900))
img.show()

#Burrowed code:
#https://stackoverflow.com/questions/34692009/download-image-from-url-using-python-urllib-but-receiving-http-error-403-forbid
#https://stackoverflow.com/questions/16627227/problem-http-error-403-in-python-3-web-scraping       
#https://pypi.org/project/beautifulsoup4/
#https://pythonprogramminglanguage.com/get-all-links-from-webpage/

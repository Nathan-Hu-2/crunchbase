import requests
from bs4 import BeautifulSoup
from csv import writer
import time
import random
import re
import sys
import time
# from torpy.http.requests import TorRequests

# companies = ['pipe', 'google', 'airbnb', 'facebook', 'fakkerererererp']

base_url = 'https://www.google.com'

# headers = {'User-Agent': UserAgent().random, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

# What gets sent to scraperAPI
payload = {
    'api_key': 'c794899b092324ebc72c168409214828',
    'url': base_url,
}
start = time.time()
html = requests.get('http://async.scraperapi.com', params=payload)
end = time.time()
print(end - start)


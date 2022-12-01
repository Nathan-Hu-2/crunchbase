

# API = 'https://api.crunchbase.com/api/v4/entities/organizations/airbnb?card_ids=[founders,raised_funding_rounds]&field_ids=[categories,short_description,rank_org_company,linkedin, facebook]&user_key=0fea1a1aa26cb1c4dc60bf758a208f51'

# res = requests.get(API)
# print(res.content)
# print(res.text)

import requests
from bs4 import BeautifulSoup
from csv import writer
import time
import random
import re
import sys
import time
# from torpy.http.requests import TorRequests
from fake_useragent import UserAgent

from stem import Signal
from stem.control import Controller
def switchIP():
    with Controller.from_port(port = 3000) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def delay() -> None:
    time.sleep(random.uniform(2, 7))
    return None

# companies = ['pipe', 'google', 'airbnb', 'facebook', 'fakkerererererp']
companies = ['pipe']

header_added = False

for company in companies:
    try:
        base_url = f'https://www.crunchbase.com/organization/{company}'
        technology_url = f'https://www.crunchbase.com/organization/{company}/technology'
        signals_url = f'https://www.crunchbase.com/organization/{company}/signals_and_news'
        # headers = {'User-Agent': UserAgent().random, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

        # What gets sent to scraperAPI
        payload = {
            'api_key': 'c794899b092324ebc72c168409214828',
            'url': base_url,
        }
        start = time.time()
        html = requests.get('http://async.scraperapi.com', params=payload)
        end = time.time()

        soup_base = BeautifulSoup(html.text, 'html.parser')
        print(html.status_code)

        # Grab Tech Related Information
        payload = {
            'api_key': 'c794899b092324ebc72c168409214828',
            'url': technology_url,
        }    
        html = requests.get('http://api.scraperapi.com', params=payload)
        soup_tech = BeautifulSoup(html.text, 'html.parser')

        # Grab Signal & News Related Information
        payload = {
            'api_key': 'c794899b092324ebc72c168409214828',
            'url': signals_url,
        } 
        html = requests.get('http://api.scraperapi.com', params=payload)
        soup_signal = BeautifulSoup(html.text, 'html.parser')

        # print(company_info)
        with open('crunchbase.csv', 'a', encoding='utf8', newline='') as f:
            theWriter = writer(f)
            header = ['Company Name', 'Description', 'Funding', 'Founded', 'Monthly Site Visits', 'Monthly Visits Growth', 'Number of Articles']

            # if not header_added:
            #     theWriter.writerow(header)
            #     heaeder_added = True

            company_name = soup_base.find('h1', class_="profile-name").text
            company_description = soup_base.find('span', class_="description").text
            total_funding = soup_base.find('span', class_="component--field-formatter field-type-money ng-star-inserted").text
            founded = soup_base.find('span', class_="component--field-formatter field-type-date_precision ng-star-inserted").text

            i = 0
            while i < 3:
                list = soup_tech.find_all('span', class_="component--field-formatter field-type-integer ng-star-inserted")
                monthly_site_visits = list[2].text
                i += 1

            monthly_visits_growth = soup_tech.find('span', class_="component--field-formatter field-type-decimal ng-star-inserted").text

            num_articles = soup_signal.find('a', class_="component--field-formatter field-type-integer link-accent ng-star-inserted").text

            info = [company_name, company_description, total_funding, founded, monthly_site_visits, monthly_visits_growth, num_articles]

            theWriter.writerow(info)
            # switchIP()
    except:
        print(company + 'not found')

print(end - start)

# print("Company Name:", company_name)
# print("Company Description:", company_description)
# print("Total Funding:", total_funding)


# Code to web scrape a website for the proxies
# res_proxy = requests.get('https://free-proxy-list.net/')
# proxy_soup = BeautifulSoup(res_proxy.text, 'html.parser')
# table = proxy_soup.find('table')
# rows = table.find_all('tr')
# cols = [[col.text for col in row.find_all('td')] for row in rows]

# proxies = []
# proxy_index = 0
# for col in cols:
#     try:
#         if col[4] == 'elite proxy' and col[6] == 'yes':
#             proxies.append('https://' + col[0] + ':' + col[1])
#     except:
#         pass
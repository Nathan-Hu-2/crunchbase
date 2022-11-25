# import requests
# import timeit

# API = 'https://api.crunchbase.com/api/v4/entities/organizations/airbnb?card_ids=[founders,raised_funding_rounds]&field_ids=[categories,short_description,rank_org_company,linkedin, facebook]&user_key=0fea1a1aa26cb1c4dc60bf758a208f51'

# res = requests.get(API)
# print(res.content)
# print(res.text)


import requests
from bs4 import BeautifulSoup
from csv import writer


base_url = 'https://www.crunchbase.com/organization/pipe'
technology_url = 'https://www.crunchbase.com/organization/pipe/technology'

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

res = requests.get(base_url, headers=headers)

# Base Organisation information
soup_base = BeautifulSoup(res.text, 'html.parser')

res = requests.get(technology_url, headers=headers)
soup_tech = BeautifulSoup(res.text, 'html.parser')


# print(company_info)

with open('crunchbase.csv', 'w', encoding='utf8', newline='') as f:
    theWriter = writer(f)
    header = ['Company Name', 'Description', 'Funding', 'Founded', 'Monthly Site Visits', 'Monthly Visits Growth']

    theWriter.writerow(header)

    company_name = soup_base.find('h1', class_="profile-name").text
    company_description = soup_base.find('span', class_="description").text
    total_funding = soup_base.find('span', class_="component--field-formatter field-type-money ng-star-inserted").text
    founded = soup_base.find('span', class_="component--field-formatter field-type-date_precision ng-star-inserted").text

    monthly_site_visits = soup_tech.find_all('span', class_="component--field-formatter field-type-integer ng-star-inserted")


    info = [company_name, company_description, total_funding, founded, monthly_site_visits]
    print(info)
    theWriter.writerow(info)


# print("Company Name:", company_name)
# print("Company Description:", company_description)
# print("Total Funding:", total_funding)

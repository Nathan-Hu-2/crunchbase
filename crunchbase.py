# import requests
# import timeit

# API = 'https://api.crunchbase.com/api/v4/entities/organizations/airbnb?card_ids=[founders,raised_funding_rounds]&field_ids=[categories,short_description,rank_org_company,linkedin, facebook]&user_key=0fea1a1aa26cb1c4dc60bf758a208f51'

# res = requests.get(API)
# print(res.content)
# print(res.text)


import requests
from bs4 import BeautifulSoup


url = 'https://www.crunchbase.com/organization/pipe'
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

res = requests.get(url, headers=headers)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

company_info = {
    'company_name': soup.find('h1', class_="profile-name").text,
    'company_description': soup.find('span', class_="description").text,
    'total_funding': soup.find('span', class_="component--field-formatter field-type-money ng-star-inserted").text
}

print(company_info)


# print("Company Name:", company_name)
# print("Company Description:", company_description)
# print("Total Funding:", total_funding)

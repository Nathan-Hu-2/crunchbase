# import requests
# import timeit

# API = 'https://api.crunchbase.com/api/v4/entities/organizations/airbnb?card_ids=[founders,raised_funding_rounds]&field_ids=[categories,short_description,rank_org_company,linkedin, facebook]&user_key=0fea1a1aa26cb1c4dc60bf758a208f51'

# res = requests.get(API)
# print(res.content)
# print(res.text)


import requests
from bs4 import BeautifulSoup
from csv import writer
import time
start = time.time()

companies = ['pipe']

res_proxy = requests.get('https://free-proxy-list.net/')
proxy_soup = BeautifulSoup(res_proxy.text, 'html.parser')
table = proxy_soup.find('table')
rows = table.find_all('tr')
cols = [[col.text for col in row.find_all('td')] for row in rows]

proxies = []
proxy_index = 0
for col in cols:
    try:
        if col[4] == 'elite proxy' and col[6] == 'yes':
            proxies.append('https://' + col[0] + ':' + col[1])
    except:
        pass


for company in companies:
    base_url = f'https://www.crunchbase.com/organization/{company}'
    technology_url = f'https://www.crunchbase.com/organization/{company}/technology'
    signals_url = f'https://www.crunchbase.com/organization/{company}/signals_and_news'

    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    while proxy_index < len(proxies):
        try:
            print('hi')
            # Base Organisation Information
            print('Trying proxy:', proxies[proxy_index])

            res = requests.get(base_url, headers=headers, proxies={'https':proxies[proxy_index]})

            soup_base = BeautifulSoup(res.text, 'html.parser')
            # Grab Tech Related Information
            print('Trying proxy:', proxies[proxy_index])
            res = requests.get(technology_url, headers=headers, proxies={'https':proxies[proxy_index]})
            print(res.status_code)

            soup_tech = BeautifulSoup(res.text, 'html.parser')
            # Grab Signal & News Related Information
            res = requests.get(signals_url, headers=headers, proxies={'https':proxies[proxy_index]})
            print(res.status_code)
            soup_signal = BeautifulSoup(res.text, 'html.parser')

            # print(company_info)
            with open('crunchbase.csv', 'a', encoding='utf8', newline='') as f:
                theWriter = writer(f)
                header = ['Company Name', 'Description', 'Funding', 'Founded', 'Monthly Site Visits', 'Monthly Visits Growth', 'Number of Articles']

                theWriter.writerow(header)

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
                print(info)
                theWriter.writerow(info)
        except:
            print('Bad Proxy...')
            proxy_index += 1

        

end = time.time()
print(end - start)

# print("Company Name:", company_name)
# print("Company Description:", company_description)
# print("Total Funding:", total_funding)

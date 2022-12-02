import requests
from bs4 import BeautifulSoup
from csv import writer
import time

companies = ['pipe', 'google', 'airbnb', 'facebook', '']

for company in companies:
    try:
        # Grab Crunchbase company information pages
        base_url = f'https://www.crunchbase.com/organization/{company}'
        technology_url = f'https://www.crunchbase.com/organization/{company}/technology'
        signals_url = f'https://www.crunchbase.com/organization/{company}/signals_and_news'

        # Create Payload for ScraperAPI
        payload = {
            'api_key': 'c794899b092324ebc72c168409214828',
            'url': base_url,
        }

        # Time the request
        start = time.time()
        html = requests.get('http://api.scraperapi.com', params=payload)
        end = time.time()
        print(end - start)

        # Parse the html text into our variable 
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

        # Open our CSV file where we will append all out information into
        with open('crunchbase.csv', 'a', encoding='utf8', newline='') as f:
            theWriter = writer(f)
            header = ['Company Name', 'Description', 'Funding', 'Founded', 'Monthly Site Visits', 'Monthly Visits Growth', 'Number of Articles']

            # Write the header (find out how to only write once)
            theWriter.writerow(header)

            # Extract information we want from how html page
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

            # Write the company information into our CSV
            info = [company_name, company_description, total_funding, founded, monthly_site_visits, monthly_visits_growth, num_articles]
            theWriter.writerow(info)
    except:
        print(company + ' not found')
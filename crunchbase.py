import requests
import timeit

API = 'https://api.crunchbase.com/api/v4/entities/organizations/airbnb?card_ids=[founders,raised_funding_rounds]&field_ids=[categories,short_description,rank_org_company]&user_key=0fea1a1aa26cb1c4dc60bf758a208f51'

res = requests.get(API)
print(res.status_code)
print(res.text)
from py_crunchbase import PyCrunchbase
from py_crunchbase.apis.search.predicates import Currency

pycb = PyCrunchbase('0fea1a1aa26cb1c4dc60bf758a208f51')
api = pycb.search_funding_rounds_api()

api.select(
    'name', 'short_description'
).where(
    announced_on__gte=2012, num_investors__lte=4, money_raised__gte=Currency(10000000)
).order_by(
    'announced_on'
)

for page in api.iterate():
    for funding_round in page:
        print(funding_round.permalink)
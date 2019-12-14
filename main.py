from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

region_id_to_name = {'W': 'Wales',
                     'E': 'England',
                     'S': 'Scotland',
                     'N': 'Northern Ireland'}

# Make dataframe for party ids -> full names
party_id_to_name = {'LAB': 'Labour',
                    'CON': 'Conservative',
                    'BRX': 'The Brexit Party',
                    'PC': 'Plaid Cymru',
                    'LD': 'Liberal Democrat',
                    'IND': 'Independent',
                    'GRN': 'Green'}

party_ids_to_names = pd.DataFrame(party_id_to_name.items(), columns=['pid', 'name'])

# Get all constituency urls
soup = BeautifulSoup(urlopen('https://www.bbc.co.uk/news/politics/constituencies'))
constituency_urls = ['https://bbc.co.uk' + x.a['href'] for x in soup.find_all("tr", {"class":"az-table__row"})]

# Extract all results
data = pd.DataFrame(columns=['constituency', 'pid', 'mp', 'votes', 'vote_share', 'vote_share_change'])
constituencies = pd.DataFrame(columns=['name', 'region', 'outcome', 'majority', 'registered', 'turnout', 'turnout_delta'])
i = 0

for j, url in enumerate(constituency_urls):
    html = urlopen(url)
    soup = BeautifulSoup(html)

    constituency_name = soup.find("h1", {"class":"constituency-title__title"}).text
    outcome = soup.find("p", {"class":"ge2019-constituency-result-headline__text"}).text
    region = region_id_to_name[url.split('/')[-1][0]]

    turnout_stats = [x.text for x in soup.find_all("span", {"class": "ge2019-constituency-result-turnout__value"})]
    constituencies.loc[j] = [constituency_name, region, outcome, *turnout_stats]

    res = soup.find_all("li", {"class":"ge2019-constituency-result__item"})
    ignore = ['\n', 'Votes:', 'Vote share %:', 'Vote share change:']
    for r in res:
        nums = [x for x in r.strings if x not in ignore]
        del nums[1]
        data.loc[i] = [constituency_name] + nums
        i += 1
    print(f"Done {j}/{len(constituency_urls)} {constituency_name}")

import pdb; pdb.set_trace()
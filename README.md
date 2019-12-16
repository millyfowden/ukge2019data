# GE2019 Data Analyis

Small repo to track some data analysis on the 2019 UK general election.
All GE data scraped from BBC website.
This is somewhat thrown together so feel free to contribute, e.g. the csvs aren't really in 3NF.

### `data/vote_data.csv`:
This is a csv of all party results for all constituencies. The format is:

| Column | Description |
| ------------- | ------------- |
| constituency | The constituency name for each result (row). Each constitency will have several result for each party |
| pid | The party id of each result. One of LAB,CON,BRX,LD,PC,SF,SNP,etc... |
| mp | The name of the candidate running in each result |
| votes | The number of votes that candidate received in this constituency |
| vote_share | The number of votes as a proportion of total votes cast |
| vote_share_change | The vote share swing compared to 2017 |

### `data/constituencies.csv`:
This is a csv of all 650 constituencies. The format is:

| Column | Description |
| - | - |
| name | Name of the constituency |
| region | The region of the constituency, e.g. Wales, Scotland etc |
| cid | The Ordnance Survery Constituency ID e.g. E14000554 |
| outcome | The outcome of the constituency. E.g. "LAB" HOLD, or "CON" GAIN FROM "LAB" as reported by BBC |
| majority | The majority of the winning party over the second party (in raw votes) |
| registered | The number of people who registered to vote in this constituency |
| turnout | The turnout of the constituency as a percentage of the number who registered |
| turnout_delta | The change in turnout percentage as compared to 2017 |

### `data/pop_by_age.csv`:
The third sheet - 'Age of year data' - from the excel book downloaded from [here](https://commonslibrary.parliament.uk/local-data/constituency-statistics-population-by-age/ ) (last accessed 2019/12/16).

### `data/party_names.csv`:
A csv that maps the BBC party IDs (pids) to their full party names, for convenience.

| Column | Description |
| - | - |
| pid | The party ID |
| name | The full name of the party |

### Additional scripts:
* get_data_from_bbc.py: The script used to scrape BBC for the GE data. It's a little slow and could be improved.
* cities.py: Script to generate plots of all constituency age distributions and entropies.
* pop.py: Script to compare the representative demographics of party voters to the national average + vote share distributions.
* 'GE2019 Post Mortem.pdf': A short WIP report on some analysis of the data.

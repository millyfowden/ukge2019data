import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt
from get_data_from_bbc import party_id_to_name
import math

parties = {'LAB': 'crimson',
           'CON': 'dodgerblue',
           'BRX': 'cyan',
           'LD': 'darkorange',
           'GRN': 'green',
           'SNP': 'yellow'}
sqrtPN = math.sqrt(len(parties))

def hist(x, bins=15, title='Histogram', color=None, mean_median=False):
    plt.hist(x, bins=bins, color=color)
    plt.title(title)
    if mean_median:
        plt.axvline(x=np.mean(x), color='black', label="Mean")
        plt.axvline(x=np.median(x), color='grey', label="Median")
        plt.legend()

agedata = pd.read_csv('data/pop_by_age.csv')
vote_data = pd.read_csv('data/vote_data.csv')
cons = pd.read_csv('data/constituencies.csv')

# vote_data = vote_data.merge(cons.query('region == "Scotland"').rename(columns={'name':'constituency'}), on='constituency', how='inner')

# Compare distributions of vote shares
total_pops = agedata.groupby('PCON11NM').first()['All Ages'].reset_index()
winning_only = False
shares = []
for i, (pid, col) in enumerate(list(parties.items())):
    plt.subplot(math.floor(sqrtPN), math.ceil(sqrtPN), i+1)
    if winning_only:
        share = vote_data.groupby('constituency').first().query(f'pid == "{pid}"').vote_share.to_numpy()
    else:
        share = vote_data.query(f'pid == "{pid}"').vote_share.to_numpy()
    hist(share, title=f'{party_id_to_name[pid]}', color=parties[pid], mean_median=True, bins=45)
    shares.append(share)
plt.show()

def _mean_std_plot(x, y, color='black'):
    plt.plot(x, y, color=color)
    plt.plot(x, y - np.std(y), linestyle=':', color=color)
    plt.plot(x, y + np.std(y), linestyle=':', color=color)

# Plot age distributions (relative to national) of top N UK LAB constituencies on vote share
N = 25
ylims=None
for i, (pid, col) in enumerate(list(parties.items())):
    #plt.subplot(math.floor(sqrtPN),math.ceil(sqrtPN),i+1)
    top5labcons = vote_data.query(f'pid == "{pid}"').sort_values('vote_share', ascending=False).constituency[:N].reset_index().rename(columns={'constituency':'name'})
    top5labcons = cons.merge(top5labcons, on='name', how='right')
    top5labcons = agedata.rename(columns={'PCON11CD':'region_code'}).merge(top5labcons, on='region_code', how='right')
    for i, (name, group) in enumerate(top5labcons.groupby('region_code')):
        pass#plt.plot(group.Age_year, group.Age_percent, alpha=0.05)
    # Plot national age mean
    #_mean_std_plot(group.Age_year, group.UK_percent, color='black')
    # Plot top n constituencies age mean
    top5labconsmean = top5labcons.groupby('Age_year').Age_percent.mean()
    #_mean_std_plot(group.Age_year, top5labconsmean, color=col)
    plt.plot(group.Age_year, top5labconsmean - group.UK_percent.to_numpy(), color=col, label=party_id_to_name[pid])
    axes = plt.gca()
    if not ylims:
        ylims = axes.get_ylim()
    else:
        ylims = [max(x,y) for x,y in zip(ylims, axes.get_ylim())]
        #axes.set_ylim(ylims)
    #plt.title(party_id_to_name[pid])
plt.axhline(y=0, color='black')
plt.legend()
plt.show()
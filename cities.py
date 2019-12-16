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

agedata = pd.read_csv('data/pop_by_age.csv')
vote_data = pd.read_csv('data/vote_data.csv')
cons = pd.read_csv('data/constituencies.csv')

for name, group in agedata.groupby('PCON11NM'):
    plt.plot(group.Age_year, group.Age_percent)
plt.plot(group.Age_year, group.UK_percent, color='black')
plt.show()

def entropy(x):
    return -np.sum(x * np.log(x))
entropies = [(n, entropy(g.Age_percent)) for n, g in agedata.groupby('PCON11NM')]

entropies = sorted(entropies, key=lambda x: x[1])

for n, e in entropies[:10]:
    print(n)
import pdb; pdb.set_trace()
import pandas as pd

data = pd.read_excel('population-by-age.xlsx', sheet_name='Age by year data')

constituency = 'Aldershot'
constituency_data = data[data.PCON11NM == constituency]
age_deviation = constituency_data.Age_percent - constituency_data.UK_percent
import pdb; pdb.set_trace()
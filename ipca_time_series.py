import pandas as pd
#import API Banco Central do Brasil
import sgs

# code of the time series desired on source
IPCA_Code = 433

# import the time series using the API, it already comes as a pandas series
ipca_ts = sgs.time_serie(IPCA_Code,start='',end='')

# transform the series in a DataFrame
df = pd.DataFrame(data=ipca_ts)

# reset the index, because the API brings the information with de date as the index
df = df.rename_axis('index').reset_index()

# rename the columns to Date and Values
df = df.rename(columns = {'index':'Date', 433:'% Values'})

df.head()

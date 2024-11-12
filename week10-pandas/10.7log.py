
import pandas as pd
import re

logFilename = 'access.log.demo'

colNames= ('ip',
'dash1',
'userId',
'time',
'url',
'status code',
'size of response',
'referer',
'user agent',
'dunno'
)

df = pd.read_csv(logFilename, delimiter= ' ', header = None, names = colNames)

#print(df.head())

# Drop the columns with dashes, so dash1, userID

df = df.drop(['dash1', 'userId'], axis= 1)  # else df.drop(columns = list of cols, inplace = True), avoids the axis = confusion

#print(df.head())

# Format the time column
# First remove the []
# re.search returns a match object and .group() extracts the final matched string.
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())


df['time'] = pd.to_datetime(df['time'], format = '%d/%b/%Y:%H:%M:%S')
df = df.set_index(['time'])
print(df.head())

download_samples = df['size of response'].resample(rule= '30Min').mean()

print(download_samples)

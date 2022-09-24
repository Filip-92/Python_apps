import pandas
from datetime import datetime, tzinfo
from pytz import utc

data = pandas.read_csv("Data analysis/reviews.csv", parse_dates = ['Timestamp'])

data.shape
data.columns
data['Course Name'].unique()

# Selecting data from the dataframe
data['Rating']
data[['Course Name', 'Rating']]

# Selecting a row
data.iloc[3]
data.iloc[1:3]

# Selecting a section
data[['Course Name', 'Rating']].iloc[1:3]

# Selecting a cell
data['Timestamp'].iloc[2]

# Filtering data based on conditions
d2 = data[data['Rating'] > 4]
d2['Rating']

data[(data['Rating'] > 4) & (data['Course Name'] == 
    'The Complete Python Course: Build 10 Professional OOP Apps')]['Rating'].mean()

# Time-based filtering
data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo = utc)) & (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo = utc))]

data['Timestamp']

# Average rating
data['Rating'].mean()
# Average rating for a particular course
data[data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications']['Rating'].mean()
# Average rating for a particular period
data[(data['Timestamp'] >= datetime(2020, 1, 1, tzinfo = utc)) & (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo = utc))]
# Average rating for a particular period for a particular course
data[(data['Timestamp'] >= datetime(2020, 1, 1, tzinfo = utc)) & 
(data['Timestamp'] <= datetime(2020, 12, 31, tzinfo = utc)) &
(data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications')]['Rating'].mean()
# Average of uncommented ratings
data[data['Comment'].isnull()]['Rating'].mean()
# Average of commented ratings
data[data['Comment'].notnull()]['Rating'].mean()
# Number of uncommented ratings
data[data['Comment'].isnull()]['Rating'].count()
# Number of commented ratings
data[data['Comment'].notnull()]['Rating'].count()
# Number of comments containing a certain word
data[data['Comment'].str.contains('accent', na=False)]['Rating'].count()
# Average of commented ratings with "accent" in comment
data[data['Comment'].str.contains('accent', na=False)]['Rating'].mean()


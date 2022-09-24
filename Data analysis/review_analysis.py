from calendar import week
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("Data analysis/reviews.csv", parse_dates = ['Timestamp'])
data.head()

data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

plt.figure(figsize = (25, 3))
plt.plot(day_average.index, day_average['Rating'])

# Rating average by week
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

plt.figure(figsize = (25, 3))
plt.plot(week_average.index, week_average['Rating'])

# Rating average by month
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby(['Month']).mean()

plt.figure(figsize = (25, 3))
plt.plot(month_average.index, month_average['Rating'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name']).mean().unstack()
print(month_average_crs.plot(figsize = (25, 8)))

# What day are people the happiest?
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
weekday_average = data.groupby(['Weekday']).mean()
weekday_average = weekday_average.sort_values('Weekday')

plt.figure(figsize = [15, 3])
plt.plot(weekday_average.index.get_level_values(0), weekday_average['Rating'])

# Number of ratings by course
share = data.groupby(['Course Name'])['Rating'].count()
print(share)

plt.pie(share, labels = share.index)
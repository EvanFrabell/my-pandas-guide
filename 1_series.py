import pandas as pd
import csv

# Series are only specialized singular columns in pandas

ice_cream = ['Chocolate', 'Vanilla', 'Strawberry', 'Rum Raisin']

# Create a series object - from list
pd.Series(ice_cream)
# 0     Chocolate
# 1       Vanilla
# 2    Strawberry
# 3    Rum Raisin
# dtype: object

fun = {'marbles': 'great circle game',
       'banana': 'yellow food to eat',
       'book': 'pages of glory'}

# Create a series object - from dict
pd.Series(fun)
# marbles     great circle game
# banana     yellow food to eat
# book           pages of glory
# dtype: object

my_skills = ['inventor', 'innovator', 'fixer', 'polymath']

# Store series object into variable
obj = pd.Series(my_skills)

# ATTRIBUTES
print(obj.values)
# ['inventor' 'innovator' 'fixer' 'polymath']
print(obj.index)
# RangeIndex(start=0, stop=4, step=1)

# METHOD
obj = obj.replace("o", "@", regex=True)
print(obj.values)
# ['invent@r' 'inn@vat@r' 'fixer' 'p@lymath']

fruits = ['Apple', 'Orange', 'Banana', 'Strawberry', 'Kiwi', 'Watermelon']
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Friday']
# Parameters
print(pd.Series(data=fruits, index=week_days))
# Monday            Apple
# Tuesday          Orange
# Wednesday        Banana
# Thursday     Strawberry
# Friday             Kiwi
# Friday       Watermelon
# dtype: object


# For csv not in UTF-8 Format
# path = 'data/nz_deaths.csv'
#
# with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open(path + 'convert.csv', 'w', newline='') as outfile:
#     inputs = csv.reader(infile)
#     output = csv.writer(outfile)
#
#     for index, row in enumerate(inputs):
#         output.writerow(row)

# READ CSV into a squeezed series...rather than as a dataframe with 2 or more columns
# This file is the count of people that died by age group from 2008-2019 in NZ
deaths = pd.read_csv('data/nz_deaths_utf8.csv', usecols=['Count'], squeeze=True)
# 0        198
# 1         45
# 2         18
# 3         33
# 4        132
#        ...
# 823     5889
# 824     4599
# 825     1890
# 826      324
# 827    34260
# Name: Count, Length: 828, dtype: int64
deaths.sum()
# 1484055 (Deaths between 2008 and 2019 in NZ)
deaths.describe()
# count      828.000000
# mean      1792.336957
# std       4464.064236
# min          6.000000
# 25%        117.000000
# 50%        366.000000
# 75%       1635.000000
# max      34260.000000
# Name: Count, dtype: float64
seven_deaths = deaths.head(7)
# 0    198
# 1     45
# 2     18
# 3     33
# 4    132
# 5    153
# 6    120
# Name: Count, dtype: int64
last_deaths = deaths.tail(2)
# 826      324
# 827    34260
# Name: Count, dtype: int64
len(deaths)
# 828 -- Total number of rows (series)
type(deaths)
# <class 'pandas.core.series.Series'>
sorted(deaths)
# [6, 6, 9, 9, 12, 12, 12, 12, 12, ....
new_list = list(deaths)
index_dic = dict(deaths)
max(deaths)
# 34260
min(deaths)
# 6
print(deaths.is_unique)
# False -- Not every value is different
print(deaths.shape)
# (828,) -- Will show count per column if attribute called on dataframe
deaths.name = "Total Deaths"
print(deaths.head(2))
# 0    198
# 1     45
# Name: Total Deaths, dtype: int64 -- Changes column header from Count to Total Deaths

# Chaining Methods & Sorting
deaths.sort_values().head()
# 209     6
# 163     6
# 439     9
# 232     9
# 508    12
# Name: Total Deaths, dtype: int64

deaths.sort_values(ascending=False).tail()
# 370    12
# 439     9
# 232     9
# 163     6
# 209     6
# Name: Total Deaths, dtype: int64

# INPLACE Paremeter -- We will now start storing data!!
deaths = pd.read_csv('data/nz_deaths_utf8.csv', usecols=['Count'], squeeze=True)

deaths = deaths.sort_values()
print(deaths)
# 209        6
# 163        6
# 439        9
# 232        9
# 508       12
#        ...
# 620    31179
# 551    31608
# 758    33222
# 689    33339
# 827    34260
# Name: Count, Length: 828, dtype: int64

# OR LIKE THIS
deaths.sort_values(ascending=False, inplace=True)
print(deaths)
# 827    34260
# 689    33339
# 758    33222
# 551    31608
# 620    31179
#        ...
# 715       12
# 439        9
# 232        9
# 163        6
# 209        6
# Name: Count, Length: 828, dtype: int64

# Sort index based on storing from above
deaths.sort_index()
# 0        198
# 1         45
# 2         18
# 3         33
# 4        132
#        ...
# 823     5889
# 824     4599
# 825     1890
# 826      324
# 827    34260
# Name: Count, Length: 828, dtype: int64
deaths.sort_index(ascending=False)

# Keywords - Check for inclusion in index and series values
print(33 in deaths)  # or 33 in deaths.index
# True
print(70000 in deaths.values)
# False

# Extract values by index
print(deaths[37])
# 858
print(deaths[[100, 102, 118]])
# 100    117
# 102    291
# 118     54
# Name: Count, dtype: int64
deaths = pd.read_csv('data/nz_deaths_utf8.csv', usecols=['Count'], squeeze=True)
print(deaths[15:20])
# 15    1506
# 16    2148
# 17    2529
# 18    2040
# 19     978
# Name: Count, dtype: int64
print(deaths[:15])
print(deaths[-5:])
print(deaths[-20:-20])

# Setup next exercise ***Not a series***
# deaths = pd.read_csv('data/nz_deaths_utf8.csv')
# deaths = deaths[:22]
# deaths.to_csv('data/nz_deaths_short.csv')

# Exract series by index label
age_death = pd.read_csv('data/nz_deaths_short.csv', index_col='Age', usecols=['Age', 'Count'], squeeze=True)
print(age_death[[5, 7]])
# Age
# 2024    153
# 3034    123
# Name: Count, dtype: int64
print(age_death['Infant'])
# 198
print(age_death[['Infant', '3034']])
# Age
# Infant    198
# 3034      123
# Name: Count, dtype: int64
print(age_death['Infant':'4044':2])
# Age
# Infant    198
# 59         18
# 1519      132
# 2529      120
# 3539      189
# Name: Count, dtype: int64

# Create a new index if unknown
age_death.reindex(index=['300304'])
# Age
# 300304   NaN
# Name: Count, dtype: float64

# Another way to retrieve values by index
age_death.get('3539')
# 189
# Now there will be no errors
age_death.get('nonsense')
# None
age_death.get('nonsense', default='This is not an index')
# This is not an index


# .value_counts() method or frequency amount
print(age_death.value_counts())
# 249     2 -- Two age groups had 249 deaths in  2008
# 978     2
# 33      1
# 2040    1
# 189     1
# 123     1
# 153     1
# 120     1
# 2148    1
# 18      1
# 366     1
# 1506    1
# 45      1
# 1260    1
# 39      1
# 711     1
# 198     1
# 132     1
# 2529    1
# 477     1
# Name: Count, dtype: int64


# idxmax and idxmin methods
deaths = pd.read_csv('data/nz_deaths_utf8.csv', usecols=['Count'], squeeze=True)
deaths.idxmax()
# 827 -- Retrieves index of max Count
deaths.idxmin()


# 163 -- Retrieves index of min Count


# .apply() method to invoke a function
age_death = pd.read_csv('data/nz_deaths_short.csv', index_col='Age', usecols=['Age', 'Count'], squeeze=True)


def death_indicator(num):
    if num < 50:
        return "Not many dead"
    elif 50 <= num <= 1000:
        return "An average amount dead"
    else:
        return "A lot dead"


age_death.apply(death_indicator)
# Age
# Infant          An average amount dead
# 14                       Not many dead
# 59                       Not many dead
# 1014                     Not many dead
# 1519            An average amount dead
# .........
# Name: Count, dtype: object

# Add 1000 more deaths to each count with lambda function
print(age_death.apply(lambda x: x+1000))
# Age
# Infant          1198
# 14              1045
# 59              1018
# 1014            1033
# 1519            1132
# ....
# Name: Count, dtype: int64

# Using .map() method with a terrible example
ages = pd.read_csv('data/nz_deaths_short.csv', usecols=['Age'], squeeze=True)
age_death = pd.read_csv('data/nz_deaths_short.csv', index_col='Age', usecols=['Age', 'Count'], squeeze=True)

print(ages.map(age_death))
# 0      198
# 1       45
# 2       18
# 3       33
# 4      132
# 5      153
# 6      120
# 7      123
# ....
# Name: Age, dtype: int64

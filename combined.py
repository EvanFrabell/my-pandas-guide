import pandas as pd
import numpy as np
import csv

############################ 1. SERIES #################
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


############################# 2. Dataframes Basics  #########################################

# Dataframes are vector tables
# It is always important to remember that changes to dataframes will not be saved if the parameter inplace=True is not used.  The other option is storing the dataframe into a new variable each time.

# Calibrating view in console
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

nba = pd.read_csv("data/nba.csv")
# series | series | series
#               Name            Team  ...            College     Salary
# 0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
# 1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
# 2     John Holland  Boston Celtics  ...  Boston University        NaN
# 3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
# 4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
# ..             ...             ...  ...                ...        ...
# 453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
# 454      Raul Neto       Utah Jazz  ...                NaN   900000.0
# 455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
# 456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0
# 457            NaN             NaN  ...                NaN        NaN
# [458 rows x 9 columns]

# Repeated methods and attributes from Series
nba.head(2)
nba.tail(5)
print(nba.index)
print(nba.values)
print(nba.dtypes)
# Name         object
# Team         object
# Number      float64
# Position     object
# Age         float64
# Height       object
# Weight      float64
# College      object
# Salary      float64
# dtype: object

# Methods and attributes only in Dataframe
print(nba.columns)
# Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'College', 'Salary'], dtype='object')
print(nba.axes)
# [RangeIndex(start=0, stop=458, step=1), Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'College', 'Salary'], dtype='object')]
nba.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 458 entries, 0 to 457
# Data columns (total 9 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   373 non-null    object
#  8   Salary    446 non-null    float64
# dtypes: float64(4), object(5)
# memory usage: 32.3+ KB

# Math scaled on axis
revenue = pd.read_csv('data/revenue.csv', index_col='Date')
revenue.sum()  # axis=0 | axis='index'
# New York       5475
# Los Angeles    5134
# Miami          5641
print(revenue.sum(axis=1))  # axis='columns'
# Date
# 1/1/16     1606
# 1/2/16     2060
# 1/3/16      967
# 1/4/16     2519
# ....


# Select desired column(s) from Dataframe
nba = pd.read_csv("data/nba.csv")

# creates series off of one column, but can't select headers with spaces
print(nba.Team)
# or
print(nba['Team'])

# Select multiple columns
print(nba[['Name', 'Team']])
nba[['Team', 'Name']].head(3)
#      Team           Name
# 0    Boston Celtics  Avery Bradley
# 1    Boston Celtics    Jae Crowder
# 2    Boston Celtics   John Holland
select = ['Salary', 'Team', 'Name']
nba[select].head(3)

# Add new column
nba['League'] = 'National Basketball Association'
#               Name            Team  Number Position   Age Height  Weight            College     Salary                           League
# 0    Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas  7730337.0  National Basketball Association
# 1      Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette  6796117.0  National Basketball Association
# 2     John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University        NaN  National Basketball Association
# 3      R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State  1148640.0  National Basketball Association
# 4    Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN  5000000.0  National Basketball Association

# Insert column in exact position
# nba.insert(loc, column, value, allow_duplicates=False)
nba.insert(3, column='Sport', value='Basketball')
#               Name            Team  Number       Sport Position   Age Height  Weight            College     Salary                           League
# 0    Avery Bradley  Boston Celtics     0.0  Basketball       PG  25.0    6-2   180.0              Texas  7730337.0  National Basketball Association
# 1      Jae Crowder  Boston Celtics    99.0  Basketball       SF  25.0    6-6   235.0          Marquette  6796117.0  National Basketball Association

nba = pd.read_csv("data/nba.csv")

# Broadcasting changes across a column of itself
nba["Age"].add(5)
nba['Age'] = nba["Age"] + 5
nba['Salary'].sub(5000000)
nba['Salary'] = nba['Salary'] - 5000000

# Create new row while interacting/broadcasting with other columns
nba["Weight in Kilograms"] = nba['Weight'] * 0.4523592

# Value Count again!!  Frequencies chart

print(nba['Height'].value_counts())
# 6-9     59
# 6-10    47
# 6-7     45
# 6-8     43
# 6-6     42
# ....
# Name: Height, Length: 18, dtype: int64
print(nba['College'].value_counts())
# Kentucky            22
# Duke                20
# Kansas              18
# North Carolina      16
# UCLA                15
# Name: College, Length: 118, dtype: int64

nba = pd.read_csv("data/nba.csv")

# Drop rows with null values
nba.tail(5)
# will drop any row with a NaN value
print(nba.dropna())  # Last row and Tibor Pleiss should be removed from example
# drops only if all values in row are NaN
nba.dropna(how='all')
# Drops entire column if NaN in any row
nba.dropna(axis=1)
# Drops row with NaN in only specified column
nba.dropna(subset=['Salary'])

# Fill null values -- Keep value types consistent
nba = pd.read_csv("data/nba.csv")
# Will set all null values in dataframe to 0. Something you'll probably never use.
nba.fillna(0)
# Set all null values in Series to 0
nba['Salary'].fillna(0, inplace=True)
nba['College'].fillna('No College', inplace=True)

# Change the datatype within a column
print(nba.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 458 entries, 0 to 457
# Data columns (total 9 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   458 non-null    object
#  8   Salary    458 non-null    float64
# dtypes: float64(4), object(5)
# memory usage: 32.3+ KB
nba['Salary'] = nba['Salary'].astype('int')
print(nba.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 458 entries, 0 to 457
# Data columns (total 9 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   458 non-null    object
#  8   Salary    458 non-null    int32
# dtypes: float64(3), int32(1), object(5)
# memory usage: 30.5+ KB

# Change type to cateogry to save memory usage
nba['Position'].nunique()
# 5
nba['Position'] = nba['Position'].astype('category')
# Saved me some memory usage


# SORT VALUES
nba.sort_values('Name', ascending=False)
nba.sort_values('Salary', inplace=True)
# Place NaN values at top
nba.sort_values('Salary', na_position='first')

# Sort by Multiple Values
# Both columns will be in reverse
nba.sort_values(['Team', 'Name'], ascending=False)

# Sort team last->first and names first->last
nba.sort_values(['Team', 'Name'], ascending=[False, True])

# Order by index
nba.sort_index(ascending=True)

# Re-sort index when out of order
nba.reset_index(drop=True, inplace=True)

# Rank attributes in a series
nba['Salary Rank'] = nba['Salary'].rank(ascending=False).astype('int')
# Salaries will now be ranked as 1 being the highest salary and ~452 being the lowest

nba.sort_values('Salary', ascending=False, inplace=True)
#                Name                 Team  Number Position   Age Height  Weight       College    Salary  Salary Rank
# 457      Kobe Bryant   Los Angeles Lakers    24.0       SF  37.0    6-6   212.0    No College  25000000            1
# 456     LeBron James  Cleveland Cavaliers    23.0       SF  31.0    6-8   250.0    No College  22970500            2
# 455  Carmelo Anthony      New York Knicks     7.0       SF  32.0    6-8   240.0      Syracuse  22875000            3

##################### 3. Filtering Data Frames #################

# Dataframes are vector tables
# It is always important to remember that changes to dataframes will not be saved if the parameter inplace=True is not used.  The other option is storing the dataframe into a new variable each time.

# Calibrating view in console
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

nba = pd.read_csv("data/nba.csv")
# series | series | series
#               Name            Team  ...            College     Salary
# 0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
# 1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
# 2     John Holland  Boston Celtics  ...  Boston University        NaN
# 3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
# 4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
# ..             ...             ...  ...                ...        ...
# 453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
# 454      Raul Neto       Utah Jazz  ...                NaN   900000.0
# 455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
# 456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0
# 457            NaN             NaN  ...                NaN        NaN
# [458 rows x 9 columns]

# Repeated methods and attributes from Series
nba.head(2)
nba.tail(5)
print(nba.index)
print(nba.values)
print(nba.dtypes)
# Name         object
# Team         object
# Number      float64
# Position     object
# Age         float64
# Height       object
# Weight      float64
# College      object
# Salary      float64
# dtype: object

# Methods and attributes only in Dataframe
print(nba.columns)
# Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'College', 'Salary'], dtype='object')
print(nba.axes)
# [RangeIndex(start=0, stop=458, step=1), Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'College', 'Salary'], dtype='object')]
nba.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 458 entries, 0 to 457
# Data columns (total 9 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   373 non-null    object
#  8   Salary    446 non-null    float64
# dtypes: float64(4), object(5)
# memory usage: 32.3+ KB

# Math scaled on axis
revenue = pd.read_csv('data/revenue.csv', index_col='Date')
revenue.sum()  # axis=0 | axis='index'
# New York       5475
# Los Angeles    5134
# Miami          5641
print(revenue.sum(axis=1))  # axis='columns'
# Date
# 1/1/16     1606
# 1/2/16     2060
# 1/3/16      967
# 1/4/16     2519
# ....


# Select desired column(s) from Dataframe
nba = pd.read_csv("data/nba.csv")

# creates series off of one column, but can't select headers with spaces
print(nba.Team)
# or
print(nba['Team'])

# Select multiple columns
print(nba[['Name', 'Team']])
nba[['Team', 'Name']].head(3)
#      Team           Name
# 0    Boston Celtics  Avery Bradley
# 1    Boston Celtics    Jae Crowder
# 2    Boston Celtics   John Holland
select = ['Salary', 'Team', 'Name']
nba[select].head(3)

# Add new column
nba['League'] = 'National Basketball Association'
#               Name            Team  Number Position   Age Height  Weight            College     Salary                           League
# 0    Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas  7730337.0  National Basketball Association
# 1      Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette  6796117.0  National Basketball Association
# 2     John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University        NaN  National Basketball Association
# 3      R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State  1148640.0  National Basketball Association
# 4    Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN  5000000.0  National Basketball Association

# Insert column in exact position
# nba.insert(loc, column, value, allow_duplicates=False)
nba.insert(3, column='Sport', value='Basketball')
#               Name            Team  Number       Sport Position   Age Height  Weight            College     Salary                           League
# 0    Avery Bradley  Boston Celtics     0.0  Basketball       PG  25.0    6-2   180.0              Texas  7730337.0  National Basketball Association
# 1      Jae Crowder  Boston Celtics    99.0  Basketball       SF  25.0    6-6   235.0          Marquette  6796117.0  National Basketball Association

nba = pd.read_csv("data/nba.csv")

# Broadcasting changes across a column of itself
nba["Age"].add(5)
nba['Age'] = nba["Age"] + 5
nba['Salary'].sub(5000000)
nba['Salary'] = nba['Salary'] - 5000000

# Create new row while interacting/broadcasting with other columns
nba["Weight in Kilograms"] = nba['Weight'] * 0.4523592

# Value Count again!!  Frequencies chart

print(nba['Height'].value_counts())
# 6-9     59
# 6-10    47
# 6-7     45
# 6-8     43
# 6-6     42
# ....
# Name: Height, Length: 18, dtype: int64
print(nba['College'].value_counts())
# Kentucky            22
# Duke                20
# Kansas              18
# North Carolina      16
# UCLA                15
# Name: College, Length: 118, dtype: int64

nba = pd.read_csv("data/nba.csv")

# Drop rows with null values
nba.tail(5)
# will drop any row with a NaN value
print(nba.dropna())  # Last row and Tibor Pleiss should be removed from example
# drops only if all values in row are NaN
nba.dropna(how='all')
# Drops entire column if NaN in any row
nba.dropna(axis=1)
# Drops row with NaN in only specified column
nba.dropna(subset=['Salary'])

# Fill null values -- Keep value types consistent
nba = pd.read_csv("data/nba.csv")
# Will set all null values in dataframe to 0. Something you'll probably never use.
nba.fillna(0)
# Set all null values in Series to 0
nba['Salary'].fillna(0, inplace=True)
nba['College'].fillna('No College', inplace=True)

# Change the datatype within a column
print(nba.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 458 entries, 0 to 457
# Data columns (total 9 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   458 non-null    object
#  8   Salary    458 non-null    float64
# dtypes: float64(4), object(5)
# memory usage: 32.3+ KB
nba['Salary'] = nba['Salary'].astype('int')
print(nba.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 458 entries, 0 to 457
# Data columns (total 9 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   458 non-null    object
#  8   Salary    458 non-null    int32
# dtypes: float64(3), int32(1), object(5)
# memory usage: 30.5+ KB

# Change type to cateogry to save memory usage
nba['Position'].nunique()
# 5
nba['Position'] = nba['Position'].astype('category')
# Saved me some memory usage


# SORT VALUES
nba.sort_values('Name', ascending=False)
nba.sort_values('Salary', inplace=True)
# Place NaN values at top
nba.sort_values('Salary', na_position='first')

# Sort by Multiple Values
# Both columns will be in reverse
nba.sort_values(['Team', 'Name'], ascending=False)

# Sort team last->first and names first->last
nba.sort_values(['Team', 'Name'], ascending=[False, True])

# Order by index
nba.sort_index(ascending=True)

# Re-sort index when out of order
nba.reset_index(drop=True, inplace=True)

# Rank attributes in a series
nba['Salary Rank'] = nba['Salary'].rank(ascending=False).astype('int')
# Salaries will now be ranked as 1 being the highest salary and ~452 being the lowest

nba.sort_values('Salary', ascending=False, inplace=True)
#                Name                 Team  Number Position   Age Height  Weight       College    Salary  Salary Rank
# 457      Kobe Bryant   Los Angeles Lakers    24.0       SF  37.0    6-6   212.0    No College  25000000            1
# 456     LeBron James  Cleveland Cavaliers    23.0       SF  31.0    6-8   250.0    No College  22970500            2
# 455  Carmelo Anthony      New York Knicks     7.0       SF  32.0    6-8   240.0      Syracuse  22875000            3


########################## 4. Dataframes - Data Extraction ####################

# The Juice of Pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

bond = pd.read_csv('data/jamesbond.csv', index_col='Film')

# LOC vs. ILOC
# LOC = Label row location  ILOC = Index Numberic Location

# Set a new index
bond.set_index('Year', inplace=True)
# Year
# 1962    Sean Connery       Terence Young       448.8     7.0                0.6
# 1963    Sean Connery       Terence Young       543.8    12.6                1.6
# 1964    Sean Connery        Guy Hamilton       820.4    18.6                3.2
# 1965    Sean Connery       Terence Young       848.1    41.9                4.7
# 1967     David Niven          Ken Hughes       315.0    85.0                NaN
# 1967    Sean Connery       Lewis Gilbert       514.2    59.9                4.4
# 1969  George Lazenby       Peter R. Hunt       291.5    37.3                0.6

# Reset to numerical index
bond.reset_index(inplace=True)
#     Year           Actor            Director  Box Office  Budget  Bond Actor Salary
# 0   1962    Sean Connery       Terence Young       448.8     7.0                0.6
# 1   1963    Sean Connery       Terence Young       543.8    12.6                1.6
# 2   1964    Sean Connery        Guy Hamilton       820.4    18.6                3.2

bond = pd.read_csv('data/jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

# Retrieve cell, row by .loc[] accessor | access row by index label
bond.loc['Goldfinger']
# Returns Series on x axis:
# Year                         1964
# Actor                Sean Connery
# Director             Guy Hamilton
# Box Office                  820.4
# Budget                       18.6
# Bond Actor Salary             3.2
# Name: Goldfinger, dtype: object

bond.loc['Casino Royale']
# Returns a dataframe because now 2D worth of data
#                Year         Actor         Director  Box Office  Budget  Bond Actor Salary
# Film
# Casino Royale  2006  Daniel Craig  Martin Campbell       581.5   145.3                3.3
# Casino Royale  1967   David Niven       Ken Hughes       315.0    85.0                NaN

bond.loc['Diamonds Are Forever':'From Russia with Love']
#                       Year           Actor       Director  Box Office  Budget  Bond Actor Salary
# Film
# Diamonds Are Forever   1971    Sean Connery   Guy Hamilton       442.5    34.7                5.8
# Die Another Day        2002  Pierce Brosnan   Lee Tamahori       465.4   154.2               17.9
# Dr. No                 1962    Sean Connery  Terence Young       448.8     7.0                0.6
# For Your Eyes Only     1981     Roger Moore      John Glen       449.4    60.2                NaN
# From Russia with Love  1963    Sean Connery  Terence Young       543.8    12.6                1.6
bond.loc['Diamonds Are Forever':'From Russia with Love':2]
#                        Year         Actor       Director  Box Office  Budget  Bond Actor Salary
# Film
# Diamonds Are Forever   1971  Sean Connery   Guy Hamilton       442.5    34.7                5.8
# Dr. No                 1962  Sean Connery  Terence Young       448.8     7.0                0.6
# From Russia with Love  1963  Sean Connery  Terence Young       543.8    12.6                1.6
bond.loc[['Dr. No', 'Goldfinger', 'Skyfall']]
# Film
# Dr. No      1962  Sean Connery  Terence Young       448.8     7.0                0.6
# Goldfinger  1964  Sean Connery   Guy Hamilton       820.4    18.6                3.2
# Skyfall     2012  Daniel Craig     Sam Mendes       943.5   170.2               14.5

# Get exact cell(s) will loc
bond.loc['Casino Royale', 'Actor']
# Film
# Casino Royale    Daniel Craig
# Casino Royale     David Niven
# Name: Actor, dtype: object
bond.loc['Dr. No', 'Actor']
# Sean Connery
bond.loc['Moonraker', ['Director', 'Box Office']]
# Director      Lewis Gilbert
# Box Office            535.0
# Name: Moonraker, dtype: object
bond.loc[['Moonraker', 'Dr. No'], ['Director', 'Box Office']]
bond.loc['Moonraker', 'Director':'Budget']
bond.loc['Moonraker':'Skyfall', 'Director':'Budget']

bond = pd.read_csv('data/jamesbond.csv')
#                               Film  Year           Actor            Director  Box Office  Budget  Bond Actor Salary
# 0                            Dr. No  1962    Sean Connery       Terence Young       448.8     7.0                0.6
# 1             From Russia with Love  1963    Sean Connery       Terence Young       543.8    12.6                1.6
# 2                        Goldfinger  1964    Sean Connery        Guy Hamilton       820.4    18.6                3.2

# Retrieve rows by index position | iloc
bond.iloc[3]
# Film                   Thunderball
# Year                          1965
# Actor                 Sean Connery
# Director             Terence Young
# Box Office                   848.1
# Budget                        41.9
# Bond Actor Salary              4.7
# Name: 3, dtype: object
bond.iloc[[4, 7]]
#                    Film  Year         Actor      Director  Box Office  Budget  Bond Actor Salary
# 4         Casino Royale  1967   David Niven    Ken Hughes       315.0    85.0                NaN
# 7  Diamonds Are Forever  1971  Sean Connery  Guy Hamilton       442.5    34.7                5.8
bond.iloc[4:8]
bond.iloc[19:]
bond.iloc[:15]
# Even if index is non-numerical you will still be able to access index by number
bond.iloc[3, 5]
# 41.9
bond.iloc[3, 2:4]
# Actor        Sean Connery
# Director    Terence Young
# Name: 3, dtype: object


bond = pd.read_csv('data/jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

# Set new values for specified cell(s)
bond.loc['Dr. No', 'Actor'] = 'Sir Sean Connery'
bond.loc['Dr. No']
# Year                             1962
# Actor                Sir Sean Connery
# Director                Terence Young
# Box Office                      448.8
# Budget                            7.0
# Bond Actor Salary                 0.6
# Name: Dr. No, dtype: object
bond.loc['Dr. No', ['Box Office', 'Budget', 'Bond Actor Salary']] = [448000000, 7000000, 6000000]
# Year                             1962
# Actor                Sir Sean Connery
# Director                Terence Young
# Box Office                448000000.0
# Budget                      7000000.0
# Bond Actor Salary           6000000.0
# Name: Dr. No, dtype: object

its_sean = bond['Actor'] == 'Sean Connery'
bond.loc[its_sean, 'Actor'] = 'Sir Sean Connery'
#                                  Year             Actor            Director   Box Office     Budget  Bond Actor Salary
# Film
# A View to a Kill                 1985       Roger Moore           John Glen        275.2       54.5                9.1
# Casino Royale                    2006      Daniel Craig     Martin Campbell        581.5      145.3                3.3
# Casino Royale                    1967       David Niven          Ken Hughes        315.0       85.0                NaN
# Diamonds Are Forever             1971  Sir Sean Connery        Guy Hamilton        442.5       34.7                5.8
# Die Another Day                  2002    Pierce Brosnan        Lee Tamahori        465.4      154.2               17.9
# Dr. No                           1962  Sir Sean Connery       Terence Young  448000000.0  7000000.0          6000000.0
# For Your Eyes Only               1981       Roger Moore           John Glen        449.4       60.2                NaN
# From Russia with Love            1963  Sir Sean Connery       Terence Young        543.8       12.6                1.6
# ...

# Rename index labels or columns
bond.rename(mapper={"Casino Royale": "Ca$in0 R0yal3", 'GoldenEye': 'GoldenTeets'})
#                                  Year             Actor            Director   Box Office     Budget  Bond Actor Salary
# Film
# A View to a Kill                 1985       Roger Moore           John Glen        275.2       54.5                9.1
# Ca$in0 R0yal3                    2006      Daniel Craig     Martin Campbell        581.5      145.3                3.3
# Ca$in0 R0yal3                    1967       David Niven          Ken Hughes        315.0       85.0                NaN
# Diamonds Are Forever             1971  Sir Sean Connery        Guy Hamilton        442.5       34.7                5.8
# Die Another Day                  2002    Pierce Brosnan        Lee Tamahori        465.4      154.2               17.9
# Dr. No                           1962  Sir Sean Connery       Terence Young  448000000.0  7000000.0          6000000.0
# For Your Eyes Only               1981       Roger Moore           John Glen        449.4       60.2                NaN
# From Russia with Love            1963  Sir Sean Connery       Terence Young        543.8       12.6                1.6
# GoldenTeets                      1995    Pierce Brosnan     Martin Campbell        518.5       76.9                5.1

bond.rename(columns={'Year': 'Release Date', 'Box Office': 'Revenue'})
#                                  Release Date             Actor            Director      Revenue     Budget  Bond Actor Salary
# Film
# A View to a Kill                         1985       Roger Moore           John Glen        275.2       54.5                9.1

print(bond.columns)
# Index(['Year', 'Actor', 'Director', 'Box Office', 'Budget', 'Bond Actor Salary'], dtype='object')
bond.columns = ['Release Date', 'Actor', 'Director', 'Box Office', 'Cost', 'Salary']
# Index(['Release Date', 'Actor', 'Director', 'Box Office', 'Cost', 'Salary'], dtype='object')


# Drop rows or columns
bond.drop(['Casino Royale', 'Dr. No', 'From Russia with Love'])
bond.drop(['Release Date', 'Actor'], axis='columns')
#                                           Director   Box Office       Cost     Salary
# Film
# A View to a Kill                          John Glen        275.2       54.5        9.1
# Casino Royale                       Martin Campbell        581.5      145.3        3.3
# Casino Royale                            Ken Hughes        315.0       85.0        NaN

# Remove entire column and store in a series for later use
actor = bond.pop("Actor")

# retrieve random single row
bond.sample()
# retrieve 5 random rows
bond.sample(n=5)
# retrieve percentage of rows randomly
bond.sample(frac=.25)
# retrieve random column
bond.sample(axis=1)



# Advanced Conditional Statements

bond = pd.read_csv('data/jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)
bond.rename(columns={'Bond Actor Salary': 'Salary'}, inplace=True)
#                                  Year           Actor            Director  Box Office  Budget  Bond Actor Salary
# Film
# A View to a Kill                 1985     Roger Moore           John Glen       275.2    54.5                9.1
# Casino Royale                    2006    Daniel Craig     Martin Campbell       581.5   145.3                3.3
# Casino Royale                    1967     David Niven          Ken Hughes       315.0    85.0                NaN
# Diamonds Are Forever             1971    Sean Connery        Guy Hamilton       442.5    34.7                5.8
# Die Another Day                  2002  Pierce Brosnan        Lee Tamahori       465.4   154.2               17.9
# Dr. No                           1962    Sean Connery       Terence Young       448.8     7.0                0.6
# For Your Eyes Only               1981     Roger Moore           John Glen       449.4    60.2                NaN

# Advanced Conditions
bond['Salary'].fillna(0, inplace=True)

conditions = [
    (bond['Director'] == 'Ken Hughes'),
    (bond['Actor'] == 'Roger Moore')]

calc = round((bond['Salary'] / bond['Budget']) * 100, 2)
choices = ['None for Ken', 'None for Roger']
bond['color'] = np.select(conditions, choicelist=choices, default=calc)

# IMPORTANT OUTPUT
#                                  Year           Actor            Director  Box Office  Budget  Salary           color
# Film
# A View to a Kill                 1985     Roger Moore           John Glen       275.2    54.5     9.1  None for Roger
# Casino Royale                    2006    Daniel Craig     Martin Campbell       581.5   145.3     3.3            2.27
# Casino Royale                    1967     David Niven          Ken Hughes       315.0    85.0     0.0    None for Ken
# Diamonds Are Forever             1971    Sean Connery        Guy Hamilton       442.5    34.7     5.8           16.71
# Die Another Day                  2002  Pierce Brosnan        Lee Tamahori       465.4   154.2    17.9           11.61
# Dr. No                           1962    Sean Connery       Terence Young       448.8     7.0     0.6            8.57
# For Your Eyes Only               1981     Roger Moore           John Glen       449.4    60.2     0.0  None for Roger
# From Russia with Love            1963    Sean Connery       Terence Young       543.8    12.6     1.6            12.7
# GoldenEye                        1995  Pierce Brosnan     Martin Campbell       518.5    76.9     5.1            6.63
# Goldfinger                       1964    Sean Connery        Guy Hamilton       820.4    18.6     3.2            17.2
# Licence to Kill                  1989  Timothy Dalton           John Glen       250.9    56.7     7.9           13.93
# Live and Let Die                 1973     Roger Moore        Guy Hamilton       460.3    30.8     0.0  None for Roger
# Moonraker                        1979     Roger Moore       Lewis Gilbert       535.0    91.5     0.0  None for Roger
# Never Say Never Again            1983    Sean Connery      Irvin Kershner       380.0    86.0     0.0             0.0
# Octopussy                        1983     Roger Moore           John Glen       373.8    53.9     7.8  None for Roger
# On Her Majesty's Secret Service  1969  George Lazenby       Peter R. Hunt       291.5    37.3     0.6            1.61
# Quantum of Solace                2008    Daniel Craig        Marc Forster       514.2   181.4     8.1            4.47
# Skyfall                          2012    Daniel Craig          Sam Mendes       943.5   170.2    14.5            8.52
# Spectre                          2015    Daniel Craig          Sam Mendes       726.7   206.3     0.0             0.0
# The Living Daylights             1987  Timothy Dalton           John Glen       313.5    68.8     5.2            7.56
# The Man with the Golden Gun      1974     Roger Moore        Guy Hamilton       334.0    27.7     0.0  None for Roger
# The Spy Who Loved Me             1977     Roger Moore       Lewis Gilbert       533.0    45.1     0.0  None for Roger
# The World Is Not Enough          1999  Pierce Brosnan       Michael Apted       439.5   158.3    13.5            8.53
# Thunderball                      1965    Sean Connery       Terence Young       848.1    41.9     4.7           11.22
# Tomorrow Never Dies              1997  Pierce Brosnan  Roger Spottiswoode       463.2   133.9    10.0            7.47
# You Only Live Twice              1967    Sean Connery       Lewis Gilbert       514.2    59.9     4.4            7.35
import pandas as pd

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

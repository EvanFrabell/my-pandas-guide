import pandas as pd

# Abstracting subsets based on conditions
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('data/employees.csv')
#     First Name  Gender  Start Date Last Login Time  Salary  Bonus % Senior Management                  Team
# 0      Douglas    Male    8/6/1993        12:42 PM   97308    6.945              True             Marketing
# 1       Thomas    Male   3/31/1996         6:53 AM   61933    4.170              True                   NaN
# 2        Maria  Female   4/23/1993        11:17 AM  130590   11.858             False               Finance
# 3        Jerry    Male    3/4/2005         1:00 PM  138705    9.340              True               Finance
# 4        Larry    Male   1/24/1998         4:47 PM  101004    1.389              True       Client Services


# Always start with memory optimization
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 8 columns):
#  #   Column             Non-Null Count  Dtype
# ---  ------             --------------  -----
#  0   First Name         933 non-null    object
#  1   Gender             855 non-null    object
#  2   Start Date         1000 non-null   object
#  3   Last Login Time    1000 non-null   object
#  4   Salary             1000 non-null   int64
#  5   Bonus %            1000 non-null   float64
#  6   Senior Management  933 non-null    object
#  7   Team               957 non-null    object
# dtypes: float64(1), int64(1), object(6)
# memory usage: 62.6+ KB
#
# Process finished with exit code 0

# Set to date and time
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['Last Login Time'] = pd.to_datetime(df['Last Login Time'])
# Parse rest of data
df['Senior Management'] = df['Senior Management'].astype('bool')
df['Gender'] = df['Gender'].astype('category')

# FASTER SETUP
df = pd.read_csv('data/employees.csv', parse_dates=['Start Date', 'Last Login Time'])
df['Senior Management'] = df['Senior Management'].astype('bool')
df['Gender'] = df['Gender'].astype('category')

# Filter on Condition

print(df['Gender'] == 'Male')
# 0       True
# 1       True
# 2      False
# 3       True
# 4       True

# Only Male rows will appear as passed in as boolean True
print(df[df['Gender'] == 'Male'])
#     First Name Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management                  Team
# 0      Douglas   Male 1993-08-06 2021-01-19 12:42:00   97308    6.945               True             Marketing
# 1       Thomas   Male 1996-03-31 2021-01-19 06:53:00   61933    4.170               True                   NaN
# 3        Jerry   Male 2005-03-04 2021-01-19 13:00:00  138705    9.340               True               Finance
# 4        Larry   Male 1998-01-24 2021-01-19 16:47:00  101004    1.389               True       Client Services
# 5       Dennis   Male 1987-04-18 2021-01-19 01:35:00  115163   10.125              False                 Legal
# ..         ...    ...        ...                 ...     ...      ...                ...                   ...

bool_condition = df['Team'] == 'Finance'
print(df[bool_condition])
#     First Name  Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management     Team
# 2        Maria  Female 1993-04-23 2021-01-19 11:17:00  130590   11.858              False  Finance
# 3        Jerry    Male 2005-03-04 2021-01-19 13:00:00  138705    9.340               True  Finance
# 7          NaN  Female 2015-07-20 2021-01-19 10:43:00   45906   11.598               True  Finance
# 14    Kimberly  Female 1999-01-14 2021-01-19 07:13:00   41426   14.543               True  Finance

print(df[df['Team'] != 'Marketing'])
#     First Name  Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management                  Team
# 1       Thomas    Male 1996-03-31 2021-01-19 06:53:00   61933    4.170               True                   NaN
# 2        Maria  Female 1993-04-23 2021-01-19 11:17:00  130590   11.858              False               Finance
# 3        Jerry    Male 2005-03-04 2021-01-19 13:00:00  138705    9.340               True               Finance
# 4        Larry    Male 1998-01-24 2021-01-19 16:47:00  101004    1.389               True       Client Services
df[df['Salary'] > 110000]
df[df['Start Date'] <= "1985-01-01"]

# Filter multiple conditions

# Get all males on the marketing team
mask1 = df['Gender'] == 'Male'
mask2 = df['Team'] == 'Marketing'
# df[(df['Gender'] == 'Male') & (df['Team'] == 'Marketing')]
df[mask1 & mask2]
#     First Name Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management       Team
# 0      Douglas   Male 1993-08-06 2021-01-19 12:42:00   97308    6.945               True  Marketing
# 21     Matthew   Male 1995-09-05 2021-01-19 02:12:00  100612   13.645              False  Marketing
# 26       Craig   Male 2000-02-27 2021-01-19 07:45:00   37598    7.757               True  Marketing
# 74      Thomas   Male 1995-06-04 2021-01-19 14:24:00   62096   17.029              False  Marketing

mask1 = df['Senior Management']
mask2 = df['Start Date'] < "1990-01-01"
df[mask1 | mask2]

mask1 = df['First Name'] == 'Robert'
mask2 = df['Team'] == 'Client Services'
mask3 = df['Start Date'] > "2016-06-01"
df[(mask1 & mask2) | mask3]


# Filter with .isin() method
mask = df['Team'].isin(['Legal', 'Sales', 'Product'])
df[mask]
#     First Name  Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management     Team
# 5       Dennis    Male 1987-04-18 2021-01-19 01:35:00  115163   10.125              False    Legal
# 6         Ruby  Female 1987-08-17 2021-01-19 16:20:00   65476   10.012               True  Product
# 11       Julie  Female 1997-10-26 2021-01-19 15:19:00  102508   12.637               True    Legal
# 13        Gary    Male 2008-01-27 2021-01-19 23:40:00  109831    5.831              False    Sales
# 15     Lillian  Female 2016-06-05 2021-01-19 06:09:00   59414    1.256              False  Product

# Filter if null
mask = df['Team'].isnull()
df[mask]
#       First Name  Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management Team
# 1         Thomas    Male 1996-03-31 2021-01-19 06:53:00   61933    4.170               True  NaN
# 10        Louise  Female 1980-08-12 2021-01-19 09:01:00   63241   15.132               True  NaN
# 23           NaN    Male 2012-06-14 2021-01-19 16:19:00  125792    5.042               True  NaN
# 32           NaN    Male 1998-08-21 2021-01-19 14:27:00  122340    6.417               True  NaN
df[df['Team'].notnull()]
#     First Name  Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management                  Team
# 0      Douglas    Male 1993-08-06 2021-01-19 12:42:00   97308    6.945               True             Marketing
# 2        Maria  Female 1993-04-23 2021-01-19 11:17:00  130590   11.858              False               Finance
# 3        Jerry    Male 2005-03-04 2021-01-19 13:00:00  138705    9.340               True               Finance


# Filter inbetween values
df[df['Salary'].between(65000, 66000)]
#     First Name  Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management             Team
# 6         Ruby  Female 1987-08-17 2021-01-19 16:20:00   65476   10.012               True          Product
# 285       Judy  Female 1997-09-16 2021-01-19 00:10:00   65931    2.304              False  Human Resources
# 353        NaN    Male 1997-04-22 2021-01-19 21:36:00   65078    3.095               True        Marketing
# 433      Wanda  Female 2008-07-20 2021-01-19 13:44:00   65362    7.132               True            Legal
# 579     Harold    Male 2010-10-18 2021-01-19 20:45:00   65673    1.187               True            Legal
# 580      Harry    Male 1985-01-27 2021-01-19 20:18:00   65482   18.089              False              NaN
# 614       Eric    Male 2004-11-12 2021-01-19 21:16:00   65168   11.513              False     Distribution
# 704     Thomas    Male 1991-09-07 2021-01-19 09:51:00   65251   11.211              False     Distribution


# DUPLICATES
df.sort_values('First Name', inplace=True)
df[df['First Name'].duplicated(keep='first')]
# Shows all duplicates other than first
# 327      Aaron    Male 1994-01-29 2021-01-19 18:48:00   58755    5.097               True        Marketing
# 440      Aaron    Male 1990-07-22 2021-01-19 14:53:00   52119   11.343               True  Client Services
# 937      Aaron     NaN 1986-01-22 2021-01-19 19:39:00   63126   18.424              False  Client Services
df[df['First Name'].duplicated(keep=False)]
# Shows all duplicates including first and last
~df['First Name'].duplicated(keep=False)
# Changes all True to False in order to show unique values

# Drop Duplicates
df.drop_duplicates(subset=['First Name'], keep='first')

df.drop_duplicates(subset=['First Name', 'Team'], keep='first')
# Will drop only if both columns have repeated values
#   First Name  Gender Start Date     Last Login Time  Salary  Bonus %  Senior Management                  Team
# 101      Aaron    Male 2012-02-17 2021-01-19 10:20:00   61602   11.849               True             Marketing
# 440      Aaron    Male 1990-07-22 2021-01-19 14:53:00   52119   11.343               True       Client Services
# 137       Adam    Male 2011-05-21 2021-01-19 01:45:00   95327   15.120              False          Distribution
# 141       Adam    Male 1990-12-24 2021-01-19 20:57:00  110194   14.727               True               Product
# 302       Adam    Male 2007-07-05 2021-01-19 11:59:00   71276    5.027               True       Human Resources


# Playing with unique values

df['Gender'].unique()
# [902 rows x 8 columns]
# ['Male', NaN, 'Female']
# Categories (2, object): ['Male', 'Female']

df['Gender'].nunique(dropna=False)
# [902 rows x 8 columns]
# 3
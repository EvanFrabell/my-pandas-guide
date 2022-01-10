import pandas as pd
import numpy as np

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


print(bond)

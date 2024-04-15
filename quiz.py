import pandas as pd
import numpy as np

data = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding='latin-1')

# Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the 7th lowest sum in 2017?
q1 = data[['Y2017','Area']].groupby('Area').sum()
print(q1.sort_values(by='Y2017').iloc[6])

# What is the mean and standard deviation across the whole dataset for the year 2017 to 2 decimal places?
q2 = data['Y2017'].mean()
q2a = data['Y2017'].std()
print(round(q2, 2))
print(round(q2a, 2))

# If you have the following list
# lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30 , 'Brazil', 92]]
# col = [‘Age’,’Nationality’,’Overall’]
# How do you create a pandas DataFrame using this list, to look like the table below?
lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30 , 'Brazil', 92]]
col = ['Age','Nationality','overall']
pd1 = pd.DataFrame(lst,columns=col, index=[1,2,3])
print(pd1)

# Perform a groupby operation on ‘Element’.  What year has the highest sum of Stock Variation?
q5 = data.groupby('Element').sum().loc['Stock Variation'].loc['Y2014':]
print(q5.sort_values(ascending=False).head(1))

# Perform a groupby operation on ‘Element’.  What is the total number of the sum of Processing in 2017?
q6 = data.groupby('Element').sum().loc['Processing']['Y2017']
print(q6)

# Given the following numpy array 
# array  = ([[94, 89, 63],
#              [93, 92, 48],
#              [92, 94, 56]])
# How would you select  the elements in bold and italics from the array?
array  = ([[94, 89, 63],
           [93, 92, 48],
           [92, 94, 56]])
a = np.array(array)
print(a[:2,1:])

# Consider the following list of tuples:
# y = [(2, 4), (7, 8), (1, 5, 9)]
# How would you assign element 8 from the list to a variable x?
y = [(2, 4), (7, 8), (1, 5, 9)]
print(y[1][1])

# How would you check for the number of rows and columns in a pandas DataFrame named df?
print(data.shape)

# Which of the following dataframe methods can be used to access elements across rows and columns?
print(data.iloc[:])

# What is the total number and percentage of missing data in 2014 to 3 decimal places?
print(data['Y2014'].isna().sum())
percent = (data['Y2014'].isna().sum()/len(data)) * 100
print(round(percent, 3))

# Which year had the least correlation with ‘Element Code’?
b = data[['Element Code', 'Y2014', 'Y2015', 'Y2016', 'Y2017']].corr()
print(b['Element Code'].sort_values().head(1))

# Answer the following questions based on the African food production dataset provided by the FAO website already provided
# What is the total sum of Wine produced in 2015 and 2018 respectively?
# Hint:
# Perform a groupby sum aggregation on ‘Item’
c = data.groupby('Item').sum().loc['Wine']
print(c['Y2015'])
print(c['Y2018'])

# What is the total number of unique countries in the dataset?
print(data.groupby('Area').sum().count())

# What is the total Protein supply quantity in Madagascar in 2015?
d = data.groupby(['Element','Area']).sum().loc['Protein supply quantity (g/capita/day)']['Y2015']
print(d.loc['Madagascar'])

# What would be the output for?
# S = [['him', 'sell'], [90, 28, 43]]
# S[0][1][1]
S = [['him', 'sell'], [90, 28, 43]]
print(S[0][1][1])

# Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the highest sum in 2017?
b = data[['Y2017', 'Area']].groupby('Area').sum()
print(b.sort_values(by='Y2017', ascending=False).head(1))
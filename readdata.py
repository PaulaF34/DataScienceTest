import pandas as pd

df = pd.read_csv('dataset.csv')

#print data
#print(df)

# print the first 5 rows
#print(df.head())

# print the last 5 rows
#print(df.tail())

# print the data frame info
#print(df.info())

# print the data frame description
# print(df.describe())

#print the sum of null values in each column
# print(df.isnull().sum())

#check the data types of each column
# numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
# categorical_cols = df.select_dtypes(include=['object']).columns
# print("Numerical columns: ", numerical_cols)
# print("Categorical columns: ", categorical_cols)

#drop the rows with missing values
df = df.dropna(axis=0)  # axis=0 means row, axis=1 means column


import pandas as pd

#read the data from the csv file
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
# df = df.dropna(axis=0)  # axis=0 means row, axis=1 means column



#Handle Duplicate Records
#read the data from data object
# data = {
#     'Name': ['Tom', 'Nick', 'John', 'Nick'],
#     'Age': [20, 21, 19, 21],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Los Angeles']
# }

# df = pd.DataFrame(data)
# print("Original data frame:")
# print(df)

#Detect duplicate rows
# duplicates = df.duplicated()
# print("Duplicate rows:")
# print(df[duplicates])

#count the number of duplicate rows
# print("Number of duplicate rows: ")
# print(df.duplicated().sum())

#drop duplicate rows
# df = df.drop_duplicates()
# print("Data frame after dropping duplicates:")
# print(df)

#drop duplicate rows based on specific columns
# df_no_duplicates_specific_columns = df.drop_duplicates(subset=['Name'])
# print("Data frame after dropping duplicates based on Name column:")
# print(df_no_duplicates_specific_columns)

#drop duplicate rows, keep the first row
# df_keep_first = df.drop_duplicates(keep='first')
# print("Data frame after dropping duplicates, keep first:")
# print(df_keep_first)

#drop duplicate rows, keep the last row
# df_keep_last = df.drop_duplicates(keep='last')
# print("Data frame after dropping duplicates, keep last:")
# print(df_keep_last)




#Insconsistency in data

data = {
    'Name': ['Tom', 'Nick', 'John', 'Nick', 'Paula'],
    'City': ['New York ', 'Los Angeles', 'Chicago', 'LA' , ' los angeles'],
    'Income': [70000, 80000, 120000, 90000, 100000]
}

df = pd.DataFrame(data)
print("Original data frame:")
print(df)

#Standardize the data in the City column to lowercase
df['City'] = df['City'].str.lower()
print("Data frame after standardizing the City column:")
print(df)

#remove leading and trailing whitespaces
df['City'] = df['City'].str.strip()
print("Data frame after removing leading and trailing whitespaces:")
print(df)

#replace the values in the City column
city_mapping = {
    'la': 'los angeles'
}
df['City'] = df['City'].replace(city_mapping)
print("Data frame after replacing values in the City column:")
print(df)

#Validate unique values in the City column
unique_categories = df['City'].unique()
print("Unique values in the City column:")
print(unique_categories)
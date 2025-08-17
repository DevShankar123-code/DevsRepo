import pandas as pd  

# Step 1: Load the dataset
Data = pd.read_csv('Telecom_Customers_Churn.csv') 

# Step 2: Clean column names (remove spaces, make lowercase)
Data.columns = Data.columns.str.strip()             
Data.columns = Data.columns.str.lower()             
Data.columns = Data.columns.str.replace(' ', '_')    

# Step 3: Remove duplicate rows
Data = Data.drop_duplicates()

# Step 4: Convert 'totalcharges' to numbers (some values may be blank)
Data['totalcharges'] = pd.to_numeric(Data['totalcharges'], errors='coerce')

# Step 5: Fill missing 'totalcharges' with monthlycharges × tenure
Data['totalcharges'] = Data['totalcharges'].fillna(Data['monthlycharges'] * Data['tenure'])

# Step 6: Drop any remaining missing values
Data = Data.dropna()

# Step 7: Convert 'seniorcitizen' from 0/1 to 'No'/'Yes'
Data['seniorcitizen'] = Data['seniorcitizen'].apply(lambda x: 'Yes' if x == 1 else 'No')

# Step 8: Remove extra spaces from text columns
for col in Data.select_dtypes(include='object').columns:
    Data[col] = Data[col].str.strip()

# Step 9: Save the cleaned data to a new CSV file
Data.to_csv('Telecom_Customers_Cleaned.csv', index=False)

# Step 10: Show summary
print(" Dataset cleaned successfully!")
print("Missing values after cleaning:")
print(Data.isnull().sum())
print("Total rows and columns:", Data.shape)
print("First few rows of the cleaned dataset:")
print(Data.head())
# Step 11: Display data types of each column
print("Data types of each column:")
print(Data.dtypes)
# Step 12: Display unique values for categorical columns
for col in Data.select_dtypes(include='object').columns:
    print(f"Unique values in '{col}': {Data[col].unique()}")
# Step 13: Display basic statistics of numerical columns
print("Basic statistics of numerical columns:")
print(Data.describe())
# Step 14: Display the cleaned dataset
print("Cleaned dataset:")
print(Data)
# Step 15: Save the cleaned dataset to a new CSV file
Data.to_csv('Telecom_Customers_Cleaned.csv', index=False)
# Step 16: Display the final shape of the cleaned dataset       
print("Final shape of the cleaned dataset:", Data.shape)
# Step 17: Display the first few rows of the cleaned dataset
print("First few rows of the cleaned dataset:")
print(Data.head())
# Step 18: Display the last few rows of the cleaned dataset 
print("Last few rows of the cleaned dataset:")
print(Data.tail())
# Step 19: Display the column names of the cleaned dataset
print("Column names of the cleaned dataset:")
print(Data.columns.tolist())
# Step 20: Display the number of unique values in each column
print("Number of unique values in each column:")
print(Data.nunique())
# Step 21: Display the memory usage of the cleaned dataset
print("Memory usage of the cleaned dataset:")
print(Data.memory_usage(deep=True)) 
# Step 22: Display the first 10 rows of the cleaned dataset
print("First 10 rows of the cleaned dataset:")
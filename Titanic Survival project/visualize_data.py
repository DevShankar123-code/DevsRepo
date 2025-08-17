import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="d@shankar",   
    database="titanic_db"
)

#  Pull data directly from MySQL
query = "SELECT Survived, Pclass, Sex, Age FROM passengers WHERE Age IS NOT NULL"
cursor = connection.cursor()
cursor.execute(query)
data = cursor.fetchall()

#  Column headers
columns = ['Survived', 'Pclass', 'Sex', 'Age']
df = pd.DataFrame(data, columns=columns)

# Format data
df['Survived'] = df['Survived'].map({0: 'No', 1: 'Yes'})
df['Sex'] = df['Sex'].map({'male': 'Male', 'female': 'Female'})

#  Visualization: Survival rate by Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("🔍 Survival Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title='Survived')
plt.tight_layout()
plt.show()

# Visualization: Age distribution of survivors vs non-survivors
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', hue='Survived', kde=True, bins=30)
plt.title("📊 Age Distribution of Survivors vs Non-Survivors")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#  Close MySQL connection
cursor.close()
connection.close()
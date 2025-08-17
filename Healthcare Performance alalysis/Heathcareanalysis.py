import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='d@shankar',
    database='Hospital_Patient_Care_Performance_Analysis'
)
# 2. Query data into a DataFrame
query = "SELECT * FROM modified_healthcare_dataset;"
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# 3. Convert dates
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], errors='coerce')

# 4. Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df, palette='viridis')
plt.title("Gender Distribution of Patients")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.show()

# 5. Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=10, kde=True, color='skyblue')
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 6. Admission Trends Over Time
admissions_per_month = df.groupby(df['Date of Admission'].dt.to_period('M')).size()
plt.figure(figsize=(8,4))
admissions_per_month.plot(kind='line', marker='o')
plt.title("Monthly Patient Admissions")
plt.xlabel("Month")
plt.ylabel("Number of Admissions")
plt.grid(True)
plt.show()

# 7. Top 10 Diseases
top_diseases = df['Medical Condition'].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(x=top_diseases.values, y=top_diseases.index, palette='plasma')
plt.title("Top 10 Diseases")
plt.xlabel("Number of Cases")
plt.ylabel("Disease")
plt.show()

# 8. Average Length of Stay by Disease
avg_stay = df.groupby('Medical Condition')['Length of Stay'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,4))
sns.barplot(x=avg_stay.values, y=avg_stay.index, palette='coolwarm')
plt.title("Average Length of Stay (Top 10 Diseases)")
plt.xlabel("Average Days")
plt.ylabel("Disease")
plt.show()

# 9. Billing Amount vs Length of Stay
plt.figure(figsize=(6,4))
sns.scatterplot(x='Length of Stay', y='Billing Amount', hue='Gender', data=df)
plt.title("Billing Amount vs Length of Stay")
plt.xlabel("Length of Stay (days)")
plt.ylabel("Billing Amount")
plt.legend(title="Gender")
plt.show()

# 10. Patients handled per Doctor
patients_per_doctor = df['Doctor'].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(x=patients_per_doctor.values, y=patients_per_doctor.index, palette='cubehelix')
plt.title("Top 10 Doctors by Number of Patients")
plt.xlabel("Number of Patients")
plt.ylabel("Doctor")
plt.show()


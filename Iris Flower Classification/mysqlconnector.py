import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='d@shankar',
    database='iris_flower_classification'
)

query = "SELECT * FROM iris_data"
df = pd.read_sql(query, conn)

print("Data fetched successfully!")

print("This Header is from mysqlconnector.py")
print(df.head())

print("this is the datatype of the data")
print(df.info())       

print("this is the stats of the data")
print(df.describe())    

print("this is the missing Value of the data if no missing value it will show 0")
print(df.isnull().sum()) 

print(" Encode Target Labels")
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['label'] = le.fit_transform(df['species'])
print("Encoded labels:")
print(df['label'].head())

print("Feature and Target Variables selection")
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['label']
print("Feature Variables:")
print(X.head()) 
print("Target Variable:")
print(y.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Data split into training and testing sets successfully!")
print("x_train Training Features:")
print(X_train.head())
print("x_test Testing Features:")
print(X_test.head())
print("y_test Training Labels:")
print(y_train.head())   
print("y_test Testing Labels:")
print(y_test.head())  
print("Data split completed successfully!")


print("Algorithm: K-Nearest Neighbors (KNN)")
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print("Model trained successfully!")



print("Model evaluation: Accuracy Score")
from sklearn.metrics import accuracy_score
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

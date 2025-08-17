import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mysql.connector
# 🛠️ Connect to MySQL database
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="d@shankar",    
    database="titanic_db"
)

# 📥 Read data from MySQL
query = """
    SELECT Survived, Pclass, Sex, Age, SibSp, Parch, Fare
    FROM passengers
    WHERE Age IS NOT NULL AND Fare IS NOT NULL
"""
df = pd.read_sql(query, mysql_connection)

# 🔄 Encode categorical column
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 🧠 Split data
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 📈 Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 🧪 Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"✅ Model Accuracy: {accuracy:.2%}")


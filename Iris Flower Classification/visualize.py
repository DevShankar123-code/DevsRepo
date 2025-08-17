# visualize.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector


df = mysql.connector.connect(
    host='localhost',
    user='root',
    password='d@shankar',
    database='iris_flower_classification'
)
query = "SELECT * FROM iris_data"
df = pd.read_sql(query, df)
# 🔹 1. Species Count Bar Chart
def species_distribution():
    df['species'].value_counts().plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
    plt.title("Species Count")
    plt.xlabel("Species")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 🔹 2. Sepal Length vs Width (Scatter)
def sepal_scatter():
    colors = {
    'Iris-setosa': 'blue',
    'Iris-versicolor': 'green',
    'Iris-virginica': 'red'
}
    plt.figure(figsize=(6,5))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.scatter(subset['sepal_length'], subset['sepal_width'],
                    label=species, color=colors[species])
    plt.title("Sepal Length vs Width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 🔹 3. Petal Length Histogram
def petal_histogram():
    df['petal_length'].plot(kind='hist', bins=20, color='plum', edgecolor='black')
    plt.title("Petal Length Histogram")
    plt.xlabel("Petal Length")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 🔹 4. Petal Width Boxplot by Species
def petal_boxplot():
    plt.figure(figsize=(7,5))
    sns.boxplot(x='species', y='petal_width', data=df, palette=['skyblue', 'lightgreen', 'salmon'])
    plt.title("Petal Width Distribution by Species")
    plt.tight_layout()
    plt.show()

# 🔹 5. Feature Correlation Heatmap
def heatmap():
    numeric_df = df.select_dtypes(include='number')
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.close()

# 🔹 6. Pair Plot
def pair_plot():
    sns.pairplot(df, hue='species', palette=['skyblue', 'lightgreen', 'salmon'])
    plt.show()

# ✅ Run all charts
if __name__ == "__main__":
    species_distribution()
    sepal_scatter()
    petal_histogram()
    petal_boxplot()
    heatmap()
    pair_plot()
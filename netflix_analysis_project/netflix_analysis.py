# netflix_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
df = pd.read_csv("netflix_data.csv")
print("Dataset Preview:")
print(df.head())

# Movie vs TV Show count
type_counts = df['Type'].value_counts()
print("\nContent Type Counts:")
print(type_counts)

# Plot: Movie vs TV Show
plt.figure(figsize=(6, 4))
type_counts.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Number of Movies vs TV Shows")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("content_type_bar.png")
plt.show()

# Plot: Genre distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, y='Genre', order=df['Genre'].value_counts().index, palette='pastel')
plt.title("Genre Distribution")
plt.tight_layout()
plt.savefig("genre_distribution.png")
plt.show()

# Plot: Content count by country
plt.figure(figsize=(8, 5))
top_countries = df['Country'].value_counts().head(5)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm')
plt.title("Top 5 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.savefig("country_content.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
df = pd.read_csv("data.csv")

# Display basic summary statistics
print(df.describe())

# Create a bar chart
plt.figure(figsize=(8, 5))
df["column_name"].value_counts().plot(kind="bar", color="skyblue")
plt.xlabel("Categories")
plt.ylabel("Count")
plt.title("Bar Chart of Column Data")

# Show the plot
plt.show()

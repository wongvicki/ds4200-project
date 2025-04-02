# Python code for Heatmap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("housing-subset.csv")

# Prepare data for heatmap
heatmap_data = df[["median_income", "housing_median_age", "population", "median_house_value"]]
correlation_matrix = heatmap_data.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap: Income, Age, Population vs House Value")
plt.tight_layout()
plt.savefig("heatmap_output.png")
plt.show()

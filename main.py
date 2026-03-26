import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/sales.csv")

# Clean column names
df.columns = df.columns.str.replace('"', '').str.strip()

# Create BMI
df["BMI"] = df["Weight(Pounds)"] / (df["Height(Inches)"]**2) * 703

# Categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["BMI_Category"] = df["BMI"].apply(bmi_category)

# Analysis
print("\nSummary Stats:")
print(df.describe())

print("\nBMI Category Counts:")
counts = df["BMI_Category"].value_counts()
print(counts)

# Visualization
counts.plot(kind='bar')
plt.title("BMI Distribution")
plt.xlabel("Category")
plt.ylabel("Count")

# Save output
plt.savefig("output/bmi_chart.png")

plt.show()
df.to_csv("output/bmi_results.csv", index=False)
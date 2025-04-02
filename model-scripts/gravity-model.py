import pandas as pd
import matplotlib.pyplot as plt

# Data for each city based on the collected parameters:
data = {
    "City": ["Mumbai", "Gurgaon", "Nagpur", "Hyderabad", "Mangalore", 
             "Bangalore", "Pune", "Ahmedabad", "Noida", "Chandigarh", "Jaipur", "Kolkata", "Bhopal"],
    "Water": [50, 50, 21.5, 80, 80, 68.5, 21.5, 30, 40, 20, 30, 25, 20],         # ₹ per 1000 L
    "Energy": [7.5, 6.75, 7.0, 6.3, 7.0, 7.15, 7.0, 7.5, 8.2, 7.0, 7.5, 8.1, 7.0],   # ₹ per kWh
    "Workforce": [803000, 771000, 550000, 746000, 550000, 891000, 720000, 720000, 771000, 700000, 640000, 643000, 550000],  # Annual salary in ₹
    "Renewable": [45, 29, 45, 42.9, 70.8, 70.8, 45, 59.5, 18.3, 36.5, 74.6, 13.5, 32],  # % of power from renewable sources
    "LandCost": [3000, 2500, 475, 1200, 800, 2000, 1500, 1000, 2500, 1200, 800, 1000, 500],  # ₹ per sq ft
    "LandAvail": [3, 6, 9, 8, 7, 5, 7, 8, 7, 6, 8, 6, 9],  # Index from 1 (scarce) to 10 (abundant)
    "Network": [10, 8, 5, 8, 6, 9, 7, 6, 9, 6, 6, 6, 5],  # Connectivity index (1-10)
    "Climate": [5, 7, 8, 8, 6, 7, 8, 7, 7, 7, 8, 6, 9]   # Climate resilience index (1-10)
}

df = pd.DataFrame(data)

# Define weights for each parameter:
weights = {
    "Water": 0.05,      # cost: lower is better
    "Energy": 0.20,     # cost: lower is better
    "Workforce": 0.05,  # cost: lower is better
    "LandCost": 0.15,   # cost: lower is better
    "Renewable": 0.10,  # benefit: higher is better
    "LandAvail": 0.05,  # benefit: higher is better
    "Network": 0.20,    # benefit: higher is better
    "Climate": 0.10     # benefit: higher is better
}

# Identify which parameters are cost factors and which are benefit factors:
cost_params = ["Water", "Energy", "Workforce", "LandCost"]
benefit_params = ["Renewable", "LandAvail", "Network", "Climate"]

# Normalize each parameter using min-max normalization:
for param in weights.keys():
    min_val = df[param].min()
    max_val = df[param].max()
    if param in cost_params:
        # For cost parameters, lower is better: invert the scale.
        df[param + "_norm"] = (max_val - df[param]) / (max_val - min_val)
    else:
        # For benefit parameters, higher is better.
        df[param + "_norm"] = (df[param] - min_val) / (max_val - min_val)

# Compute the composite gravity model score:
df["Score"] = 0
for param, weight in weights.items():
    df["Score"] += df[param + "_norm"] * weight

# Sort by score in descending order (higher score = more attractive)
df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)

# Display the computed scores:
print("Composite Attraction Scores for Data Center Site Selection:")
print(df[["City", "Score"]])

# Plot the scores for visualization:
plt.figure(figsize=(10, 6))
plt.bar(df["City"], df["Score"], color="skyblue")
plt.xlabel("City")
plt.ylabel("Attraction Score")
plt.title("Gravity Model Scores for Data Center Location")
plt.xticks(rotation=45)
for i, score in enumerate(df["Score"]):
    plt.text(i, score + 0.005, f"{score:.3f}", ha="center", va="bottom")
plt.tight_layout()
plt.show()

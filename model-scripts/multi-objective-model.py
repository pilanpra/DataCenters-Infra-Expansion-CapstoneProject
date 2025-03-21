import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, value
import random

# -----------------------------
# 1. Create Dummy Data
# -----------------------------
# Candidate sites (these are examples taken from generic North American data center attributes)
data = {
    'Site': ['A', 'B', 'C', 'D', 'E'],
    # Total cost (millions USD) – lower is better
    'Cost': [10, 12, 9, 11, 13],
    # Renewable energy availability (fraction, higher is better)
    'Renewable': [0.5, 0.6, 0.55, 0.45, 0.7],
    # Network Connectivity Score (0-100, higher is better)
    'Connectivity': [80, 75, 90, 85, 70],
    # Climate Risk Index (lower is better)
    'Risk': [0.3, 0.4, 0.2, 0.25, 0.35]
}

df = pd.DataFrame(data)
print("Dummy Data:")
print(df)

# -----------------------------
# 2. Clustering Analysis
# -----------------------------
# Clustering on a subset of features: Cost and Connectivity
subset_features = df[['Cost', 'Connectivity']]
kmeans_subset = KMeans(n_clusters=2, random_state=42).fit(subset_features)
df['Cluster_Subset'] = kmeans_subset.labels_

# Clustering on all features: Cost, Renewable, Connectivity, Risk
all_features = df[['Cost', 'Renewable', 'Connectivity', 'Risk']]
kmeans_all = KMeans(n_clusters=2, random_state=42).fit(all_features)
df['Cluster_All'] = kmeans_all.labels_

print("\nClustering Results:")
print(df)

# Plotting clustering results for visualization
plt.figure(figsize=(10,4))

# Plot for subset features
plt.subplot(1,2,1)
plt.scatter(df['Cost'], df['Connectivity'], c=df['Cluster_Subset'], cmap='viridis', s=100)
for i, txt in enumerate(df['Site']):
    plt.annotate(txt, (df['Cost'][i], df['Connectivity'][i]))
plt.xlabel("Cost (Millions USD)")
plt.ylabel("Connectivity Score")
plt.title("Clustering: Cost vs Connectivity")

# Plot for all features (example: Cost vs Risk)
plt.subplot(1,2,2)
plt.scatter(df['Cost'], df['Risk'], c=df['Cluster_All'], cmap='viridis', s=100)
for i, txt in enumerate(df['Site']):
    plt.annotate(txt, (df['Cost'][i], df['Risk'][i]))
plt.xlabel("Cost (Millions USD)")
plt.ylabel("Risk Index")
plt.title("Clustering: Cost vs Risk")
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Multi-Objective Placement Model via Weighted Sum
# -----------------------------
# For demonstration, we combine the following objectives:
# - Minimize Cost
# - Maximize Renewable (by subtracting it)
# - Maximize Connectivity (by subtracting it)
# - Minimize Risk (by adding it)
# We define the weighted sum objective as:
#    Minimize: w_cost * Cost - w_renewable * Renewable - w_connectivity * Connectivity + w_risk * Risk
#
# We also add a constraint that the chosen site must have Connectivity >= 80.

# Weight parameters (adjustable)
w_cost = 1.0
w_renewable = 5.0
w_connectivity = 0.1
w_risk = 100.0

# Create the MILP model
model = LpProblem("DataCenterPlacement", LpMinimize)

# Decision variables: x[s] = 1 if site s is selected, 0 otherwise.
sites = df['Site'].tolist()
x = {s: LpVariable(f"x_{s}", cat=LpBinary) for s in sites}

# Objective function: sum of weighted scores for each candidate site.
# Note: Since renewable and connectivity are desirable, we subtract them.
objective_terms = []
for s in sites:
    cost = df.loc[df['Site'] == s, 'Cost'].values[0]
    renewable = df.loc[df['Site'] == s, 'Renewable'].values[0]
    connectivity = df.loc[df['Site'] == s, 'Connectivity'].values[0]
    risk = df.loc[df['Site'] == s, 'Risk'].values[0]
    term = (w_cost * cost - w_renewable * renewable - w_connectivity * connectivity + w_risk * risk) * x[s]
    objective_terms.append(term)
model += lpSum(objective_terms)

# Constraint: Exactly one site must be selected
model += lpSum(x[s] for s in sites) == 1, "SelectOneSite"

# Constraint: The selected site's connectivity must be at least 80
for s in sites:
    connectivity = df.loc[df['Site'] == s, 'Connectivity'].values[0]
    if connectivity < 80:
        model += x[s] == 0, f"ConnectivityConstraint_{s}"

# Solve the optimization model
model.solve()

print("\nOptimization Results:")
selected_site = None
for s in sites:
    if x[s].varValue == 1:
        selected_site = s
        break

if selected_site:
    print(f"Selected Site: {selected_site}")
    print(f"Objective Value: {value(model.objective):.2f}")
    print("Attributes of the Selected Site:")
    print(df[df['Site'] == selected_site])
else:
    print("No feasible site selected.")

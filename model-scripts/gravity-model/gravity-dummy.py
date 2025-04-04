import numpy as np
import pandas as pd

# -----------------------------
# 1. Create Dummy Data
# -----------------------------
# Candidate site data (dummy values; replace with real data as available)
data = {
    'Site': ['Site1', 'Site2', 'Site3'],
    'Cost': [10, 8, 12],            # Lower is better (in arbitrary cost units)
    'EFF': [0.9, 0.85, 0.95],         # Energy efficiency rating (higher is better)
    'RE': [0.6, 0.7, 0.5]             # Renewable energy availability (fraction)
}
candidates = pd.DataFrame(data)

# Demand point data: assume 3 demand points with demand weights B_i
demand = pd.DataFrame({
    'DemandPoint': ['D1', 'D2', 'D3'],
    'B': [100, 150, 120]  # demand weights (e.g., population, IT load)
})

# Distance matrix (in km); rows: demand points, columns: candidate sites
# For example, distance from D1 to Site1 = 20 km, etc.
distances = pd.DataFrame({
    'Site1': [20, 35, 30],
    'Site2': [25, 30, 40],
    'Site3': [30, 40, 20]
}, index=['D1', 'D2', 'D3'])

# -----------------------------
# 2. Define Model Parameters
# -----------------------------
# Weights for the attractiveness function
theta1 = 1.0  # weight for cost
theta2 = 1.0  # weight for energy efficiency
theta3 = 1.0  # weight for renewable energy availability

# Distance decay parameter (lambda)
lambda_decay = 1.0

# -----------------------------
# 3. Compute Attractiveness (A_j) for each candidate site
# -----------------------------
# Higher attractiveness is better.
candidates['A'] = theta1 * (1.0 / candidates['Cost']) + theta2 * candidates['EFF'] + theta3 * candidates['RE']

# -----------------------------
# 4. Compute Distance Decay Term (D_j) for each candidate site
# -----------------------------
decay = {}
for site in candidates['Site']:
    # Extract the distances for this candidate site from all demand points.
    d = distances[site].values.astype(float)
    # Compute the decay term: sum of (B_i * d^(-lambda)) for each demand point.
    decay[site] = np.sum(demand['B'].values * (d ** (-lambda_decay)))
    
candidates['D'] = candidates['Site'].map(decay)

# -----------------------------
# 5. Compute Overall Optimality Score (S_j)
# -----------------------------
candidates['Score'] = candidates['A'] * candidates['D']

print("Candidate Scores:")
print(candidates[['Site', 'Cost', 'EFF', 'RE', 'A', 'D', 'Score']])

# -----------------------------
# 6. Optimization: Choose the candidate with maximum Score.
# -----------------------------
optimal_site = candidates.loc[candidates['Score'].idxmax()]
print("\nOptimal Site Selected:")
print(optimal_site)

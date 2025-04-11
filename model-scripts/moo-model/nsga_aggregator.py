import pandas as pd
import matplotlib.pyplot as plt
import random
from deap import base, creator, tools, algorithms

# Load dataset
df = pd.read_csv("data-final.csv")
df["SERVICE_AVAILABILITY_SCORE"] = df[[
    "FULL_CABINETS", "PARTIAL_CABINETS", "SHARED_RACKSPACE", "CAGES",
    "SUITES", "BUILD_TO_SUIT", "FOOTPRINTS", "REMOTE_HANDS"
]].astype(int).sum(axis=1)
df["FACILITY_AGE"] = 2025 - df["YEAR_OPERATIONAL"]

# Constraint check for eligibility of data centers
# Constraint: IT_POWER ≥ 1, AREA ≥ 10,000 sqft, SERVICE_SCORE ≥ 4
def is_valid(row):
    return (
        row["IT EQUIPMENT POWER"] >= 1 and
        row["AREA"] >= 10000 and
        row["SERVICE_AVAILABILITY_SCORE"] >= 4
    )

# Multi-objective fitness function
# Let S be the set of selected, valid data centers:
# f1 (minimize) = ∑ PUE_i
# f2 (maximize) = -∑ IXP_Count_i  [negated to convert to minimization]
# f3 (maximize) = -∑ Service_Score_i [negated to convert to minimization]
# f4 (minimize) = mean(Facility_Age_i)
def evaluate(ind):
    selected = df[[bool(x) for x in ind]]
    valid = selected[selected.apply(is_valid, axis=1)]
    if valid.empty:
        return (99999.0,) * 4
    return (
        valid["State_Aggregated_PUE"].sum(),
        -valid["State_Aggregated_IXP_Count"].sum(),
        -valid["SERVICE_AVAILABILITY_SCORE"].sum(),
        valid["FACILITY_AGE"].mean()
    )

# DEAP configuration for NSGA-II
N = len(df)
random.seed(42)
creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMulti)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, N)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selNSGA2)

# Run NSGA-II optimization
pop = toolbox.population(n=50)
for ind in pop:
    ind.fitness.values = toolbox.evaluate(ind)
for gen in range(50):
    offspring = algorithms.varAnd(pop, toolbox, cxpb=0.7, mutpb=0.2)
    for ind in offspring:
        ind.fitness.values = toolbox.evaluate(ind)
    pop = toolbox.select(pop + offspring, k=50)

# Extract Pareto-optimal solutions
pareto_front = tools.sortNondominated(pop, len(pop), first_front_only=True)[0]

# Collect Pareto-optimal data centers into a DataFrame
rows = []
for i, ind in enumerate(pareto_front):
    selected = df[[bool(x) for x in ind]]
    for _, row in selected.iterrows():
        rows.append({
            "Solution #": i + 1,
            "Location": row["LOCATION"],
            "City": row["CITY"],
            "State": row["STATE"],
            "PUE": row["State_Aggregated_PUE"],
            "IXP Count": row["State_Aggregated_IXP_Count"],
            "Service Score": row["SERVICE_AVAILABILITY_SCORE"],
            "Facility Age": 2025 - row["YEAR_OPERATIONAL"]
        })

result_df = pd.DataFrame(rows)

# Weights for final scoring (user-defined)
weights = {
    "PUE": 0.4,
    "IXP Count": 0.3,
    "Service Score": 0.2,
    "Facility Age": 0.1
}

# Normalization for weighted score:
# norm(x) = (x - min(x)) / (max(x) - min(x))
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

# Weighted score calculation:
# Final_Score = -w1*norm(PUE) + w2*norm(IXP_Count) + w3*norm(Service_Score) - w4*norm(Facility_Age)
norm_df = result_df.copy()
for col in weights:
    norm_df[col + "_norm"] = normalize(result_df[col])

norm_df["Weighted Score"] = (
    norm_df["PUE_norm"] * (-weights["PUE"]) +
    norm_df["IXP Count_norm"] * weights["IXP Count"] +
    norm_df["Service Score_norm"] * weights["Service Score"] +
    norm_df["Facility Age_norm"] * (-weights["Facility Age"])
)

# Display the results
print("\nWeighted Scores for All Data Centers:")
print(norm_df[[
    "Solution #", "Location", "City", "State", "PUE", "IXP Count",
    "Service Score", "Facility Age", "Weighted Score"
]].to_string(index=False))
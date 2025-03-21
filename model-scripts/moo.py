# Multi-objective Data Center Site Selection (simplified example)
import pyomo.environ as pyo

# Define candidate sites and example data (normally loaded from datasets)
sites = ['Mumbai', 'Hyderabad', 'Chennai', 'Delhi']
energy_cost = {'Mumbai': 0.10, 'Hyderabad': 0.08, 'Chennai': 0.09, 'Delhi': 0.07}    # Electricity $/kWh
renew_pct   = {'Mumbai': 0.50, 'Hyderabad': 0.60, 'Chennai': 0.40, 'Delhi': 0.30}    # Grid renewable fraction
land_cost   = {'Mumbai': 5.0, 'Hyderabad': 3.0, 'Chennai': 4.0, 'Delhi': 6.0}       # Land+build cost (relative)
latency_to_users = {'Mumbai': 10, 'Hyderabad': 20, 'Chennai': 15, 'Delhi': 25}      # Latency (ms) to key user base
power_capacity  = {'Mumbai': 100, 'Hyderabad': 120, 'Chennai': 90, 'Delhi': 110}    # Power capacity (MW) available
required_capacity = 150   # Total required capacity (MW) for the project

# Initialize Pyomo model
model = pyo.ConcreteModel()
model.SITES = pyo.Set(initialize=sites)
model.select = pyo.Var(model.SITES, within=pyo.Binary)  # x_i variables

# Objective weights for weighted sum approach (tunable)
w_cost = 1.0    # weight for cost
w_energy = 0.1  # weight for energy (lower this if cost is more important)
w_renew = 1.0   # weight for renewable (higher weight means model favors renewable use)

# Define components of objectives
total_infra_cost = sum(land_cost[s] * model.select[s] for s in model.SITES)
total_energy_use = sum( (50.0 * energy_cost[s]) * model.select[s] for s in model.SITES)
# ^ assume each site uses 50 (arbitrary units) of energy load for illustration
total_renewable  = sum( renew_pct[s] * (50.0 * model.select[s]) for s in model.SITES )

# Combined objective: minimize cost + energy - renewable (negative because we want to maximize renewable)
model.objective = pyo.Objective(
    expr = w_cost*total_infra_cost + w_energy*total_energy_use - w_renew*total_renewable,
    sense = pyo.minimize
)

# Constraints:
# 1) Capacity: ensure selected sites can supply at least the required capacity
model.capacity_constr = pyo.Constraint(
    expr = sum(power_capacity[s] * model.select[s] for s in model.SITES) >= required_capacity
)
# 2) Latency: at least one site with latency <= 20ms must be selected to serve nearby users
model.latency_constr = pyo.Constraint(
    expr = sum(model.select[s] for s in model.SITES if latency_to_users[s] <= 20) >= 1
)
# 3) Budget example: limit number of sites (for simplicity, at most 2 sites can be chosen)
model.site_count_constr = pyo.Constraint(expr = sum(model.select[s] for s in model.SITES) <= 2)

# Solve the model (using an open-source MILP solver, e.g., GLPK or CBC)
solver = pyo.SolverFactory('glpk')
solution = solver.solve(model, tee=False)

# Output selected sites
selected_sites = [s for s in model.SITES if pyo.value(model.select[s]) == 1]
print("Selected site(s):", selected_sites)

# NSGA-II Model for Multi-Objective Data Center Selection

## 1. Overview of the NSGA-II Model

The Non-Dominated Sorting Genetic Algorithm II (NSGA-II) is a powerful evolutionary optimization technique used to solve multi-objective decision-making problems. In the context of data center site selection, the NSGA-II model enables the identification of optimal combinations of data center facilities that balance various competing criteria such as energy efficiency, connectivity, service availability, and infrastructure age.

Unlike single-objective optimization models, NSGA-II produces a **Pareto front**: a set of non-dominated solutions where no single solution is superior across all objectives. This approach is particularly valuable in infrastructure planning, where trade-offs between cost, performance, and risk must be carefully evaluated.

## 2. Collected Parameters and Objective Functions

The data used in this model includes a wide range of attributes for each data center facility. These attributes are derived from publicly available databases and provider information.

**Key Parameters and Objective Functions:**

- **State Aggregated PUE** (Power Usage Effectiveness): Total energy efficiency score *(minimize)*
- **State Aggregated IXP Count**: Total number of Internet Exchange Points *(maximize)*
- **Service Availability Score**: Sum of availability indicators like cages, racks, suites, etc. *(maximize)*
- **Facility Age**: Calculated as $(2025 - \text{Year Operational})$ *(minimize)*

**Constraints:**

- IT equipment power $\geq 1$ MW  
- Floor area $\geq 10{,}000$ sqft  
- Service availability score $\geq 4$

## 3. Justification of Objective Weights in the Final Scoring

| Objective            | Type     | Weight | Justification                                                                 |
|----------------------|----------|--------|------------------------------------------------------------------------------|
| PUE                  | Cost     | 0.40   | Directly influences energy cost and environmental sustainability.            |
| IXP Count            | Benefit  | 0.30   | Reflects network performance and customer experience.                        |
| Service Availability | Benefit  | 0.20   | Indicates operational flexibility and quality of services provided.          |
| Facility Age         | Cost     | 0.10   | Older facilities may require upgrades; newer ones offer modern infrastructure.|

*The total sum of weights is 1.0 to ensure a balanced scoring framework aligned with strategic priorities.*

## 4. Normalization Strategy

To fairly compare data across differing units and ranges, **min-max normalization** is used for all scoring metrics.

### Normalization Methods

- **For cost-type objectives (lower is better):**

 ### $$x'_i = \frac{\max(x) - x_i}{\max(x) - \min(x)}$$

- **For benefit-type objectives (higher is better):**

 ### $$x'_i = \frac{x_i - \min(x)}{\max(x) - \min(x)}$$

### Why Normalize?

- Ensures scale-invariant comparison across metrics (e.g., PUE vs. IXP)
- Prevents any one metric from dominating due to its magnitude
- Supports intuitive interpretation of weights

### 5. Final Scoring Formula

Once normalization is applied, a weighted score is calculated for each solution on the Pareto front.

### General Formula

![Alt text](https://quicklatex.com/cache3/af/ql_24b321d31300626ba51b19665a42a1af_l3.png)

Where:  
- $\text{Score}_i$ = Final weighted score for solution $i$  
- $w_j$ = Weight of objective $j$  
- $\text{norm}(x_{ij})$ = Normalized value of objective $j$ for solution $i$

### Expanded Example

$$\text{Score}_i = -0.4 \cdot \text{norm}(PUE_i) +
                 0.3 \cdot \text{norm}(IXP_i) +
                 0.2 \cdot \text{norm}(Service_i) -
                 0.1 \cdot \text{norm}(Age_i)$$

*Negative weights are applied for objectives to be minimized.*

## 6. Conclusion

The NSGA-II model provides a strategic, data-driven framework for selecting optimal data center combinations under multiple constraints and goals. It empowers decision-makers to visualize trade-offs and tailor selections to organizational priorities such as energy savings, connectivity, flexibility, and infrastructure modernization. The weighted scoring extension adds clarity and adaptability for final selection, turning a complex multi-objective optimization into an actionable business decision.

$$\text{Score}_i = \sum_j (w_j \cdot \text{norm}(x_{ij}))$$

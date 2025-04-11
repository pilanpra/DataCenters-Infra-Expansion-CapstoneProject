
# Multi-Objective Optimization Model for Data Center Selection

## Overview

This project implements a multi-objective optimization model using **NSGA-II** (Non-dominated Sorting Genetic Algorithm II) to identify optimal data center sites based on multiple criteria:

- Energy Efficiency (PUE)
- Connectivity (IXP Count)
- Service Availability
- Facility Age

The optimization is done using the DEAP library in Python.

---

## Objectives

We aim to minimize or maximize the following objectives:

1. **Minimize Power Usage Effectiveness (PUE)**  
   Lower PUE implies better energy efficiency.
   $$
   f_1 = \sum_{i \in S} PUE_i
   $$

2. **Maximize Internet Exchange Point (IXP) Count**  
   Higher IXP count suggests better connectivity.
   $$
   f_2 = -\sum_{i \in S} IXP_i
   $$

3. **Maximize Service Availability Score**  
   Summation of various service features at the site.
   $$
   f_3 = -\sum_{i \in S} ServiceScore_i
   $$

4. **Minimize Facility Age**  
   Newer data centers are often more efficient.
   $$
   f_4 = \frac{1}{|S|} \sum_{i \in S} Age_i
   $$

---

## Constraints

A data center is considered **valid** if it satisfies:

- IT Equipment Power ≥ 1
- AREA ≥ 10,000 sqft
- Service Availability Score ≥ 4

Mathematically:
$$
Valid(i) = 
\begin{cases}
1 & \text{if } Power_i \geq 1 \land Area_i \geq 10000 \land ServiceScore_i \geq 4 \\
0 & \text{otherwise}
\end{cases}
$$

---

## Weighted Scoring

After obtaining the Pareto front, each solution is scored using a weighted normalization method for business prioritization:

Weights:
- PUE: 0.4 (to minimize)
- IXP Count: 0.3 (to maximize)
- Service Score: 0.2 (to maximize)
- Facility Age: 0.1 (to minimize)

The final weighted score for each data center is:
$$
WeightedScore_i = -0.4 \cdot norm(PUE_i) + 0.3 \cdot norm(IXP_i) + 0.2 \cdot norm(ServiceScore_i) - 0.1 \cdot norm(Age_i)
$$

---

## Tools and Libraries

- Python
- DEAP (Distributed Evolutionary Algorithms in Python)
- pandas, matplotlib

---

## Business Use-Case

This model enables infrastructure teams to:

- Select optimal data centers that balance efficiency, connectivity, and service capability.
- Improve long-term planning by prioritizing newer, well-connected, and energy-efficient facilities.
- Customize weights to reflect business priorities (e.g., emphasize energy savings or compliance).

---

## Outputs

- Weighted normalized scores for comparison

---

## How to Run

```bash
python nsga_aggregator.py
```

Make sure to have `data-final.csv` in the working directory.


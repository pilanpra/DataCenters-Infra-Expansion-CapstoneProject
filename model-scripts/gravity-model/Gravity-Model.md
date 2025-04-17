# Gravity Model for Data Center Site Selection in India

## 1. Overview of the Gravity Model

The **gravity model** is a quantitative method used to estimate the attractiveness or suitability of different locations for establishing a data center. Inspired by Newton's law of gravity, where the attraction between two bodies is proportional to their mass and inversely proportional to the square of the distance, the model in our context adapts this concept for evaluating potential data center sites.

Instead of physical distance, we assess multiple **influencing factors** such as cost, infrastructure, environmental risk, and regulatory support. The goal is to compute an **attraction score** for each location, where a higher score indicates a more suitable site for data center deployment.

---

## 2. Collected Parameters and Their Estimation

The data for this model was collected for 13 Indian cities based on real-world, publicly available sources. Each parameter was chosen based on its relevance to data center infrastructure and operations.

### Key Parameters and Estimation Methods:

- **Water Supply Cost (₹/1000L):** Estimated from industrial water tariffs published by local municipal bodies or state industrial development corporations.
- **Energy Supply Cost (₹/kWh):** Based on industrial/commercial electricity tariffs provided by state electricity boards.
- **Technical Workforce Cost (₹/year):** Estimated from average IT/engineering salary data for each city, sourced from job portals and government salary reports.
- **Renewable Energy Availability (%):** Proportion of electricity derived from renewable sources in each state, sourced from national power dashboards and state energy development agencies.
- **Land Cost (₹/sqft):** Derived from commercial real estate listings and government land allotment rates in industrial or IT zones.
- **Land Availability Index (1–10):** A qualitative index based on the availability of industrial land parcels or designated IT zones.
- **Network Resilience Index (1–10):** A score based on the presence of Internet Exchange Points (IXPs), submarine cable connectivity, and fiber penetration.
- **Climate Resilience (1–10):** Evaluated based on natural disaster risks like floods, earthquakes, and heatwaves, using data from environmental risk studies.

Each parameter was chosen for its direct impact on the feasibility and long-term operational efficiency of a data center.

---

## 3. Weight Estimation in the Gravity Model

Weights were assigned to parameters based on their **relative importance** in determining the overall viability and cost-effectiveness of a data center:

| Parameter                | Type    | Weight | Justification                                                 |
| ------------------------ | ------- | ------ | ------------------------------------------------------------- |
| Energy Supply Cost       | Cost    | 0.20   | Electricity is the largest operational cost for data centers. |
| Network Resilience Index | Benefit | 0.20   | Critical for data transmission and uptime.                    |
| Land Cost                | Cost    | 0.15   | Major initial capital expense.                                |
| Renewable Energy Avail.  | Benefit | 0.10   | Supports sustainability and future cost efficiency.           |
| Regulatory/Climate Index | Benefit | 0.10   | Reduces deployment risks and speeds up approvals.             |
| Technical Workforce Cost | Cost    | 0.05   | Smaller impact post-setup; moderate importance.               |
| Water Supply Cost        | Cost    | 0.05   | Important for cooling, but relatively low in cost.            |
| Land Availability Index  | Benefit | 0.05   | Determines how easily a site can be acquired.                 |

The total sum of weights is 1.0 to ensure balanced scoring.

---

## 4. Why Min-Max Normalization?

We use **min-max normalization** to bring all parameters onto a comparable 0 to 1 scale. This is essential because different parameters (e.g., water cost vs. land availability index) are measured in different units and ranges.

### Benefits of Min-Max Normalization:

- Prevents any one parameter from dominating due to scale.
- Ensures that higher normalized values always represent more favorable conditions.
- Allows both cost and benefit parameters to be incorporated uniformly.

### Two Forms of Normalization:

- For **cost parameters** (lower is better):


$x'_i = (max(x) - x_i) / (max(x) - min(x))$


- For **benefit parameters** (higher is better):


$x'_i = (x_i - min(x)) / (max(x) - min(x))$


---

## 5. Gravity Model Scoring Formula

We calculate the **composite attraction score** for each city using the following weighted sum:

### General Formula:


$Score_i = ∑ (w_j * norm(x_ij))$


Where:

- $Score_i$ = Final gravity score for city _i_
- $w_j$ = Weight assigned to parameter _j_
- $norm(x_ij)$ = Normalized value of parameter _j_ for city _i_

### Expanded Example:

$$Score_i = 0.05 * norm(Water_i) +
          0.20 * norm(Energy_i) +
          0.05 * norm(Workforce_i) +
          0.10 * norm(Renewable_i) +
          0.15 * norm(LandCost_i) +
          0.05 * norm(LandAvail_i) +
          0.20 * norm(Network_i) +
          0.10 * norm(Climate_i)$$

Each city's normalized parameter values are multiplied by their respective weights and summed to give a final score. Cities are ranked based on this score to identify the most suitable data center location.

---

## 6. Conclusion

This gravity model provides a robust and data-driven method for selecting optimal data center locations in India. By incorporating real-world constraints and industry-relevant weights, it offers a practical framework for infrastructure planning that can be refined with more granular data and localized insights.

---

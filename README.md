# Data Centers Infra Expansion and Optimization of Costs and Renewable Energy

## 🧠 Project Overview

This project focuses on optimizing the **expansion of data center infrastructure** by balancing **infrastructure and energy costs** with the integration of **renewable energy sources**. As data centers are pivotal to the digital economy, ensuring their sustainability and efficiency is essential for both performance and environmental impact.

---

## 🎯 Objectives

- **Optimize Costs:** Reduce capital and operational costs in expanding or upgrading data center infrastructure.
- **Integrate Renewables:** Maximize the use of renewable energy sources while maintaining reliability.
- **Improve Efficiency:** Identify and categorize high-performing data centers based on power usage, ecosystem connectivity, and service availability.

---

## 🧰 Methodology

1. **Data Collection:**
   - Gathered global data center information including capacity, energy usage, service offerings, and connectivity.

2. **Data Cleaning & Preprocessing:**
   - Removed irrelevant or missing values.
   - Standardized units and handled missing data via imputation.

3. **Exploratory Data Analysis (EDA):**
   - Analyzed the distribution of features such as PUE, power usage, IXPs, and tenant count.

4. **Clustering Analysis:**
   - Performed K-Means clustering using scaled numerical features to group similar data centers.
   - Visualized clusters using PCA.

5. **Optimization Modeling:**
   - Developed linear and gravity-based optimization models (planned next).
   - Models will incorporate cost, efficiency, renewable availability, and connectivity.

---

## ✅ Progress Summary

| Task                      | Status     |
|---------------------------|------------|
| Data Collection           | ✅ Complete |
| Data Cleaning             | ✅ Complete |
| Clustering Analysis       | ✅ Complete |
| Exploratory Data Analysis | 🟡 In Progress |
| Optimization Modeling     | 🔜 Upcoming |
| Reporting & Deployment    | 🔜 Upcoming |

---

## 🗺️ Next Steps

- [ ] Perform deeper EDA per cluster to understand traits of efficient vs. costly data centers.
- [ ] Implement gravity-based optimization to score potential locations based on proximity to demand, cost, and renewables.
- [ ] Formulate multi-objective MILP model for new data center placement.
- [ ] Include a recommendation engine for site selection under cost and energy constraints.
- [ ] Build a visual dashboard for decision-making and reporting.

---

## 📁 Repository Structure

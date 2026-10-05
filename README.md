# AI Warehouse Digital Twin

A warehouse decision-support prototype combining **machine-learning demand forecasting**, **forecast-informed replenishment rules**, **inventory simulation**, and an **interactive Streamlit dashboard**.

The project demonstrates how historical demand data can be transformed into forecasts, replenishment decisions, simulated inventory outcomes, and actionable product-level recommendations.

---

## Project Overview

Traditional inventory management often relies only on current stock levels and static reorder thresholds.

This project extends that approach by combining:

- Historical demand analysis
- Machine-learning demand forecasting
- Forecast-informed replenishment logic
- Inventory simulation
- Stockout and service-level analysis
- Rule-based decision recommendations
- Interactive dashboard visualization

The objective is to build an end-to-end decision-support workflow that helps evaluate inventory actions before applying them.

---

## System Architecture

```text
Products + Orders + Inventory
            |
            v
      Data Exploration
            |
            v
Historical Demand Generation
            |
            v
   Demand Forecasting
            |
            v
Replenishment Decisions
            |
            v
 Inventory Simulation
            |
            v
    Decision Engine
            |
            v
   Streamlit Dashboard
```

---

## Project Phases

### Phase 1 — Data Exploration

The initial datasets were explored and validated.

Main data sources:

- Products
- Orders
- Inventory

The analysis focused on:

- Demand patterns
- Current stock levels
- Reorder points
- Maximum stock levels
- Basic replenishment rules

A simple baseline reorder logic was used to understand the initial inventory situation.

---

### Phase 2 — Historical Demand Generation

A synthetic historical demand dataset was created to simulate one year of product demand.

Dataset size:

- 10 products
- 365 days
- 3,650 product-day observations

The generated demand includes:

- Weekly demand patterns
- Monthly effects
- Long-term trend
- Random variation

Final dataset structure:

```text
date
product_id
actual_demand
```

---

### Phase 3 — Demand Forecasting

Demand forecasting was implemented using lag-based supervised learning.

Features used:

```text
lag_1
lag_2
lag_7
```

Models compared:

- Naive Forecast
- Linear Regression
- Random Forest Regressor

Example results for product P001:

| Model | MAE | RMSE |
|---|---:|---:|
| Naive Forecast | 1.027 | 1.329 |
| Linear Regression | 0.748 | 0.937 |
| Random Forest | 1.210 | 1.480 |

For the tested product, Linear Regression achieved the best performance.

A recursive **14-day demand forecast** was then generated for all products.

---

## Phase 4 — Replenishment Decision Support

Forecast results were combined with current inventory data to generate replenishment indicators.

The system calculates:

- Average daily forecast
- Days of Supply
- Inventory risk
- Reorder requirement
- Forecast-based reorder quantity
- Replenishment priority

Priority levels include:

```text
Critical
High
Medium
Low
```

The replenishment logic is designed as a transparent forecast-informed decision baseline.

It is not presented as a full mathematical optimization model.

---

## Phase 5 — Inventory Digital Twin Simulation

A simplified inventory simulation was built to test replenishment decisions over a 14-day planning horizon.

For each product and day, the simulation calculates:

```text
Starting Stock
Forecast Demand
Fulfilled Demand
Stockout Quantity
Ending Stock
```

### Current Policy Results

- Total forecast demand: **1,286 units**
- Fulfilled demand: **277 units**
- Stockout quantity: **1,009 units**
- Warehouse service level: **21.54%**
- Products experiencing stockout: **10**

The simulation showed that the current replenishment policy was insufficient for the forecasted demand.

---

## Scenario Analysis

A second what-if scenario was tested by increasing replenishment quantities enough to cover the complete 14-day forecast.

| Scenario | Service Level | Stockout Quantity |
|---|---:|---:|
| Current Policy | 21.54% | 1,009 |
| Improved Scenario | 100% | 0 |

The improved scenario is a simplified what-if experiment.

It is **not claimed to be an optimal inventory policy**, because it does not include constraints such as supplier lead time, holding cost, ordering cost, capacity limits, or safety stock.

---

## Phase 6 — Decision Engine

Simulation results and replenishment indicators are combined to generate actionable recommendations.

Possible recommendations include:

```text
Replenish Immediately
Increase Reorder Quantity
Monitor and Replenish Soon
Replenish
Maintain Current Policy
```

The decision engine considers:

- Days of Supply
- Replenishment priority
- Service level
- Stockout quantity
- Stockout days
- Reorder requirements

Products are then ranked according to urgency.

Example high-priority products:

```text
P002
P006
P010
P004
P008
```

---

## Phase 7 — Interactive Dashboard

An interactive dashboard was developed using **Streamlit** and **Plotly**.

Dashboard features include:

- Warehouse KPI cards
- Product selector
- Scenario performance comparison
- Service-level visualization
- Stockout comparison
- Product-level recommendations
- 14-day demand forecast
- Inventory evolution
- Recommendation distribution
- Highest-priority product table
- Final product decision table

The user can select a product and explore its current stock situation, forecast, simulation results, and recommended inventory action.

---

## Key Results

The project produced several useful insights:

- Linear Regression outperformed the naive baseline for the tested product.
- The current replenishment policy produced a low warehouse service level.
- All 10 products experienced stockouts under the current simulated policy.
- The simulation clearly showed where current reorder quantities were insufficient.
- The final decision engine transformed technical metrics into clear product-level recommendations.

---

## Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Plotly
- Jupyter Notebook
- Git
- GitHub

---

## Project Structure

```text
ai-warehouse-digital-twin/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── products.csv
│   ├── orders.csv
│   ├── inventory.csv
│   ├── historical_demand.csv
│   ├── future_forecasts_14d.csv
│   ├── forecast_summary_14d.csv
│   ├── replenishment_decisions.csv
│   ├── current_policy_simulation.csv
│   ├── improved_policy_simulation.csv
│   ├── product_simulation_summary.csv
│   ├── scenario_comparison.csv
│   ├── final_decisions.csv
│   ├── recommendation_summary.csv
│   └── top_priority_products.csv
│
└── notebooks/
    ├── 01_data_exploration.ipynb
    ├── 02_historical_data_generation.ipynb
    ├── 03_demand_forecasting.ipynb
    ├── 04_replenishment_optimization.ipynb
    ├── 05_inventory_simulation.ipynb
    └── 06_decision_engine.ipynb
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/youcy03/ai-warehouse-digital-twin.git
```

Move into the project directory:

```bash
cd ai-warehouse-digital-twin
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

Then open the local Streamlit URL displayed in the terminal.

---

## Requirements

The main dependencies are:

```text
pandas
numpy
matplotlib
scikit-learn
streamlit
plotly
```

---

## Key Concepts Demonstrated

This project demonstrates several important concepts in machine learning and decision-support systems:

- Time-series data should be split chronologically.
- Baseline forecasting models should be evaluated before using more complex models.
- More complex models do not always perform better.
- Lag features can transform time-series forecasting into supervised learning.
- Forecasts can be converted into operational inventory indicators.
- Simulation can test inventory policies before real-world implementation.
- Machine learning and rule-based business logic can be combined in one decision-support workflow.
- Dashboard applications can make technical results easier to interpret.

---

## Current Limitations

This project is a prototype and uses simplified assumptions.

Current limitations include:

- Synthetic historical demand data
- No supplier lead-time modeling
- No safety-stock optimization
- No inventory holding-cost model
- No ordering-cost model
- No warehouse capacity constraints
- No demand uncertainty intervals
- Replenishment rules are heuristic
- The improved scenario assumes enough inventory can be ordered to cover forecast demand
- Recursive forecasting can propagate prediction errors

---

## Future Improvements

Possible future extensions include:

- Lead-time-aware replenishment
- Safety-stock optimization
- Economic Order Quantity models
- Inventory holding and ordering costs
- Supplier constraints
- Warehouse capacity constraints
- Forecast uncertainty intervals
- Automated model selection
- More advanced forecasting models
- Real warehouse database integration
- Real-time inventory updates
- Cloud deployment
- Authentication and user roles

---

## Final Workflow

```text
Data
  ↓
Demand Forecast
  ↓
Inventory Decision
  ↓
Simulation
  ↓
Recommendation
  ↓
Interactive Dashboard
```

The project shows how machine-learning forecasts can be integrated into a broader warehouse decision-support system rather than being treated as an isolated prediction task.
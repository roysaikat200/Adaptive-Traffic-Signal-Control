# Adaptive Traffic Signal Control System 🚦

This project presents an **Adaptive Traffic Signal Control System** using **Gradient Boosting Regressor (GBR)** to dynamically optimize green light duration at intersections based on current and incoming traffic.

> 📝 Submitted to: Artificial Intelligence and Soft Computing 2024 (ICAISC 2024)

## 🔍 Overview

Traditional static traffic lights can’t handle real-time traffic changes. This system leverages **machine learning** to adjust signal timings dynamically, reducing excess green time and boosting vehicle throughput.

We propose:

* **ATSC**: *Adaptive Traffic Signal Control* using present traffic data.
* **AATSC**: *Advanced Adaptive Traffic Signal Control* using present **and** upcoming vehicle data.


## ⚙️ Methodology

### 💡 Model Used

* **Gradient Boosting Regression (GBR)** — ensemble ML technique using sequential decision trees.

### 📥 Input Features

* Vehicle count per lane
* Waiting time
* Time of day
* Flow ratio
* (AATSC only) Upcoming vehicle count

### 📤 Output

* Optimal green time per lane


## 🧠 Algorithm Sketch

1. Train GBR model on multivariate traffic dataset.
2. For each signal cycle:

   * Predict green time for NS/EW lanes using trained model.
   * Adjust based on real-time and (in AATSC) forecasted traffic.
3. Update waiting times and repeat for next cycle.


## 📊 Results

| Metric                 | Static | ATSC   | AATSC  |
| ---------------------- | ------ | ------ | ------ |
| **Excess Green Time**  | High   | Lower  | Lowest |
| **Vehicle Throughput** | Low    | Better | Best   |

* **ATSC** reduced green time waste and increased flow.
* **AATSC** achieved superior throughput by factoring upcoming traffic.


## 🧪 Simulated Using

* **Python** with gradient boosting models (e.g., scikit-learn)
* Custom traffic simulation inputs (both even & uneven scenarios)

## 📄 Paper Link

👉 [Read the Full Paper (PDF)](./Final_Adaptive_Paper.pdf)

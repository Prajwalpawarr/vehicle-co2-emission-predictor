# 🚗 CO₂ Emission Predictor

### End-to-End Machine Learning Web Application for Vehicle Emission Estimation

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.1-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Project Objectives](#-project-objectives)
- [Dataset](#-dataset)
- [ML Pipeline](#-ml-pipeline)
- [Model Performance](#-model-performance)
- [Web Application](#-web-application)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Key Takeaways](#-key-takeaways)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🔍 Overview

A complete data science project that predicts **vehicle CO₂ emissions** using a trained **Ridge Regression** model and serves real-time predictions through an interactive **Flask web application**. The project covers the full ML lifecycle — from raw data exploration and feature engineering to model deployment.

> **TL;DR:** Input vehicle specs → Get instant CO₂ emission prediction in g/km

---

## 🎯 Problem Statement

Transportation is one of the **largest contributors to global carbon emissions**. Understanding how vehicle specifications impact CO₂ output is critical for:

- 🏭 **Manufacturers** — designing eco-friendly vehicles
- 📜 **Regulators** — setting emission standards
- 🌱 **Consumers** — making environmentally conscious purchase decisions

This project builds a predictive model that estimates CO₂ emissions based on a vehicle's technical specifications, enabling **data-driven sustainability decisions**.

---

## 🏆 Project Objectives

| # | Objective | Status |
|---|-----------|--------|
| 1 | Analyze and explore vehicle emissions dataset | ✅ Done |
| 2 | Engineer and select predictive features | ✅ Done |
| 3 | Train and evaluate multiple regression models | ✅ Done |
| 4 | Deploy best model through a Flask web app | ✅ Done |
| 5 | Provide real-time CO₂ emission predictions | ✅ Done |

---

## 📊 Dataset

| Property | Details |
|----------|---------|
| **Features Used** | Engine Size, Transmission Type, Fuel Type, Combined Fuel Consumption (mpg) |
| **Target Variable** | CO₂ Emissions (g/km) |
| **Records** | 7,000+ vehicle entries |

### Feature Details:

| Feature | Type | Description |
|---------|------|-------------|
| Engine Size (L) | Numerical | Engine displacement in litres |
| Transmission | Categorical | Type of transmission (automatic, manual, etc.) |
| Fuel Type | Categorical | Petrol, diesel, hybrid, etc. |
| Combined MPG | Numerical | Combined fuel consumption (miles per gallon) |
| **CO₂ Emissions** | **Target** | **Carbon dioxide emissions in grams per kilometre** |

---

## ⚙️ ML Pipeline

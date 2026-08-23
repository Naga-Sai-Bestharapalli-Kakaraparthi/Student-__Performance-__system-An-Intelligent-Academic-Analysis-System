# Personalized Learning Data Analytics Platform

[![Data Pipeline CI](https://github.com/Naga-Sai-Bestharapalli-Kakaraparthi/Student-__Performance-__system-An-Intelligent-Academic-Analysis-System/actions/workflows/ci.yml/badge.svg)](https://github.com/Naga-Sai-Bestharapalli-Kakaraparthi/Student-__Performance-__system-An-Intelligent-Academic-Analysis-System/actions)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)

An end-to-end data processing and educational analytics platform designed to ingest raw student interaction metrics, execute automated ETL feature engineering, predict learning outcomes, and present real-time diagnostic insights via an interactive dashboard.

---

## 📌 System Architecture & Data Flow

```text
  ┌────────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
  │  Student Interaction   │ ───►  │  Automated ETL        │ ───►  │ Predictive Risk       │
  │  Raw Dataset (CSV)     │       │  Transformation Engine│       │  Modeling (Scikit)    │
  └────────────────────────┘       └───────────────────────┘       └───────────────────────┘
                                                                               │
  ┌────────────────────────┐       ┌───────────────────────┐                   │
  │ Streamlit Analytics UI │ ◄───  │ Dynamic Intervention  │ ◄─────────────────┘
  │ Dashboard              │       │ Study Plan Engine     │     (Risk Stratification)
  └────────────────────────┘       └───────────────────────┘
